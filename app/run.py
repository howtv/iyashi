from slackbot.bot import Bot
from db import Database
from file import File


def main():
    Database.initialise()
    try:
        file = File()
        file.create_table()
    except:
        pass

    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
