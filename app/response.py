from slackbot.bot import listen_to
import db

import animal

db.init()


@listen_to("iyashi")
def iyashi(message):
    row = db.get_file_by_random()
    if row is not None:
        message.send(row[0])


@listen_to("にゃーん")
def cat(message):
    row = db.get_file_by_animal(animal.CAT)
    if row is not None:
        message.send(row[0])


@listen_to("わんわん")
def dog(message):
    row = db.get_file_by_animal(animal.DOG)
    if row is not None:
        message.send(row[0])


@listen_to("チンチラ")
def chinchilla(message):
    row = db.get_file_by_animal(animal.CHINCHILLA)
    if row is not None:
        message.send(row[0])


@listen_to("ハリネズミ")
def hedgehog(message):
    row = db.get_file_by_animal(animal.HEDGEHOG)
    if row is not None:
        message.send(row[0])


@listen_to("フクロウ")
def owl(message):
    row = db.get_file_by_animal(animal.OWL)
    if row is not None:
        message.send(row[0])


@listen_to("predict")
def post(message):
    if "files" in message.body.keys():
        for file in message.body["files"]:
            label = animal.predict(file["url_private_download"])
            db.add_file(file["permalink"], label)
            message.react(animal.get_emoji(label))
