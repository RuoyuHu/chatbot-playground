import os
import json

from enum import Enum, unique

from utils.loaders import load_model_for_generation
from utils.fprint import fprint, fprint_init


class Roles(Enum):
    """
    Enum denoting the roles of different participants in the conversation
    """
    BOT = 0,
    USER = 1,


class Chatbot():
    """
    Chatbot class object - Loads and acts as a wrapper to pretrained
    transformer model to generate responses in a conversational context
    """
    def __init__(self, **kwargs):
        self.tar = kwargs['tar']  # Target output file path for logging
        self.patience = 12  # Maximum number of past utterances to consider in generation

        # Conversation state variables
        self.conversation = []
        self.username = "$USER"
        self.log_file = kwargs['log_file']

        self.display_names = {
            Roles.BOT: kwargs['botname'],
            Roles.USER: self.username
        }

        # Initialist logging file
        fprint_init(self.log_file)

        print(f"Loading prompts...")
        self._load_prompt()

        print(f"Loading model...")
        model, tokenizer, pipeline = load_model_for_generation(**kwargs)
        self.model = model
        self.tokenizer = tokenizer
        self.pipeline = pipeline

        self.model.eval()
        print(f"Loading complete")

    @staticmethod
    def load_config():
        """
        Load and return the configuration variables
        """
        current_dir = __file__
        current_dir = current_dir.rsplit(os.path.sep, maxsplit=1)[0]
        config = json.load(open(os.path.join(current_dir, 'config.json'), 'r'))
        return config

    def _load_prompt(self):
        """
        Load initial prompt as a list of strings from a given file.
        """
        with open(self.tar, 'r') as prompt_file:
            lines = prompt_file.read().splitlines()
            self.conversation = lines

    def _prepare_prompt(self):
        """
        Prepare a prompt from a selection of previous exchanges in the current conversation
        """
        prompt = self.conversation[-self.patience:]
        prompt = "\n".join(prompt)
        prompt += f"\n{self.display_names[Roles.BOT]}:"
        return prompt

    def _prepare_bot_response(self, output):
        """
        Post processing over a bot's generated response before presentation to the user
        """
        utterance = output[0]['generated_text']
        utterance = utterance.split('\n')[0]
        utterance = utterance.lstrip()
        return utterance

    def _conv_log(self, utterance, actor, logging=True):
        """
        Pre-processing utterance before saving to conversation history and log file
        """
        terminator = ""
        if utterance[-1] not in [".", "?", "!"]:
            terminator = "."

        log_str = f"{self.display_names[actor]}: {utterance}{terminator}"

        self.conversation.append(log_str)
        if logging:
            fprint(log_str)

    def _log_conv(self):
        """
        Log the current conversation history in bulk
        """
        for utterance in self.conversation:
            fprint(utterance)

    def reset(self):
        """
        Reset conversation state to allow for brand new conversation without reloading models
        """
        self.conversation = []
        self.username = "$USER"
        self.display_names[self.username] = self.username
        fprint_init(self.log_file)

        print(f"Reseting...")
        print(f"Loading prompts...")
        self._load_prompt()
        print(f"Loading complete")
        print(f"Running with new prompt:")
        print("\n".join(self.conversation))
        print()

    def run(self):
        """
        Run conversation
        """
        conversation_start = True

        intro_utt = f"Hi, my name is {self.display_names[Roles.BOT]}, what\'s your name?"
        self._conv_log(intro_utt, Roles.BOT, logging=False)
        self.username = input(f"Alex: {intro_utt}\n>")
        for i, utterance in enumerate(self.conversation):
            self.conversation[i] = utterance.replace('$USER', self.username)
        self.display_names[Roles.USER] = self.username
        self._log_conv()
        self._conv_log(f"My name is {self.username}", Roles.USER)

        try:
            while conversation_start:
                prompt = self._prepare_prompt()
                config = self._load_config()['generation']

                bot_response = self.pipeline(prompt, **config)
                bot_response = self._prepare_bot_response(bot_response)

                self._conv_log(bot_response, Roles.BOT)
                user_response = input(f"{self.display_names[Roles.BOT]}: {bot_response}\n>")
                self._conv_log(user_response, Roles.USER)

        except KeyboardInterrupt:
            print("---------------------------------------------------------")
            print("---------------------------------------------------------")
            for line in self.conversation:
                print(line)

            raise KeyboardInterrupt
