from chatbot.chatbot import Chatbot


if __name__ == "__main__":
    # Create chatbot instance
    bot = Chatbot(**Chatbot.load_config()['chatbot'])

    while True:
        try:
            bot.run()
        except KeyboardInterrupt:
            """
            Allow keyboard interrupt to initiate bot settings reset

            Bot reset starts new conversation with reloaded prompt without
            reloading the pretrained model
            """

            user_choice = input("\nExit? [Y/n]\n>")
            if user_choice == 'Y':
                exit(0)

            bot.reset()
