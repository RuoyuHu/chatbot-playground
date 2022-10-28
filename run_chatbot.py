from transformers.utils import logging
from chatbot.chatbot import Chatbot


if __name__ == "__main__":
    logging.set_verbosity_error()
    bot = Chatbot(**Chatbot.load_config()['chatbot'])

    while True:
        try:
            bot.run()
        except KeyboardInterrupt:
            user_choice = input("\nExit? [Y/n]\n>")
            if user_choice == 'Y':
                exit(0)

            bot.reset()
