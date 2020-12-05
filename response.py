from slackbot.bot import listen_to

import animal
import db
from slackbot_settings import IMAGE_UPLOADED_CHANNEL, in_channel


NO_PICTURE_MESSAGE = (
    'Please post pictures on "{}" and it will be registered automatically!'.format(
        IMAGE_UPLOADED_CHANNEL
    )
)

db.init()


@listen_to("iyashi")
def iyashi(message):
    row = db.get_file_by_random()
    if row is not None:
        message.send(row[0])
    else:
        message.send(NO_PICTURE_MESSAGE)


@listen_to("cat|nyan|にゃーん|ニャーン")
def cat(message):
    row = db.get_file_by_animal(animal.CAT)
    if row is not None:
        message.send(row[0])
    else:
        message.send(NO_PICTURE_MESSAGE)


@listen_to("dog|wanwan|わんわん|ワンワン")
def dog(message):
    row = db.get_file_by_animal(animal.DOG)
    if row is not None:
        message.send(row[0])
    else:
        message.send(NO_PICTURE_MESSAGE)


@listen_to("chinchilla|チンチラ|ちんちら")
def chinchilla(message):
    row = db.get_file_by_animal(animal.CHINCHILLA)
    if row is not None:
        message.send(row[0])
    else:
        message.send(NO_PICTURE_MESSAGE)


@listen_to("hedgehog|ハリネズミ|はりねずみ")
def hedgehog(message):
    row = db.get_file_by_animal(animal.HEDGEHOG)
    if row is not None:
        message.send(row[0])
    else:
        message.send(NO_PICTURE_MESSAGE)


@listen_to("owl|フクロウ|ふくろう|ほーほー|ホーホー")
def owl(message):
    row = db.get_file_by_animal(animal.OWL)
    if row is not None:
        message.send(row[0])
    else:
        message.send(NO_PICTURE_MESSAGE)


@listen_to(".*")
@in_channel(IMAGE_UPLOADED_CHANNEL)
def post(message):
    if "files" in message.body.keys():
        for file in message.body["files"]:
            label = animal.predict(file["url_private_download"])
            db.add_file(file["permalink"], label)
            message.react(animal.get_emoji(label))
