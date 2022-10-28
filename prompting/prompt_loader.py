import json
import os

from utils.fprint import fprint_init, fprint_json, fprint, colourise, TER_COL


class PromptLoader:
    """
    PromptLoader object - Loads prompt and performs single inference steps
    """
    def __init__(self, tar, pipeline=None):
        self._file = tar

        self.pipeline = pipeline
        self.prompt = None

        fprint_init('output.log')

    def load_prompt(self):
        """
        Load prompt from file
        """
        with open(self._file, 'r') as input_file:
            prompt = "".join(input_file.readlines())
            input_file.close()
            self.prompt = prompt
            return prompt

    def run_prompt(self, pipeline=None, prompt=None):
        """
        Load prompt and run single inference
        """
        if prompt is None:
            prompt = self.load_prompt()

        if pipeline is not None:
            return pipeline(prompt)

        current_dir = __file__
        current_dir = current_dir.rsplit(os.path.sep, maxsplit=1)[0]
        config = json.load(open(os.path.join(current_dir, 'config.json'), 'r'))

        fprint(f"Running generation with the following config:")
        fprint_json(config)
        fprint()

        result = self.pipeline(prompt, **config)
        text = result[0]['generated_text']
        fprint(self.prompt, end='')
        fprint(text, colour=TER_COL.GREEN)

        return result
