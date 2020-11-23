from slackbot.bot import listen_to
import db

import const


db.init()


@listen_to("iyashi")
def iyashi(message):
    row = db.get_file_by_random()
    if row is not None:
        message.send(row[0])


@listen_to("にゃーん")
def cat(message):
    row = db.get_file_by_animal(const.CAT)
    if row is not None:
        message.send(row[0])


@listen_to("わんわん")
def dog(message):
    row = db.get_file_by_animal(const.DOG)
    if row is not None:
        message.send(row[0])
