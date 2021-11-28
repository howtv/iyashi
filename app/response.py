from slackbot.bot import listen_to

import animal
from slackbot_settings import IMAGE_UPLOADED_CHANNEL, in_channel
from file import File


NO_PICTURE_MESSAGE = (
    'Please post pictures on "{}" and it will be registered automatically!'.format(
        IMAGE_UPLOADED_CHANNEL
    )
)


@listen_to("iyashi")
def iyashi(message):
    try:
        file = File()
        row = file.get_by_random()
        message.send(row.url)
    except:
        message.send(NO_PICTURE_MESSAGE)


@listen_to("cat|nyan|にゃーん|ニャーン")
def cat(message):
    try:
        file = File()
        row = file.get_by_animal(animal.CAT)
        message.send(row.url)
    except:
        message.send(NO_PICTURE_MESSAGE)


@listen_to("dog|wanwan|わんわん|ワンワン")
def dog(message):
    try:
        file = File()
        row = file.get_by_animal(animal.DOG)
        message.send(row.url)
    except:
        message.send(NO_PICTURE_MESSAGE)


@listen_to("chinchilla|チンチラ|ちんちら")
def chinchilla(message):
    try:
        file = File()
        row = file.get_by_animal(animal.CHINCHILLA)
        message.send(row.url)
    except:
        message.send(NO_PICTURE_MESSAGE)


@listen_to("hedgehog|ハリネズミ|はりねずみ")
def hedgehog(message):
    try:
        file = File()
        row = file.get_by_animal(animal.HEDGEHOG)
        message.send(row.url)
    except:
        message.send(NO_PICTURE_MESSAGE)


@listen_to("owl|フクロウ|ふくろう|ほーほー|ホーホー")
def owl(message):
    try:
        file = File()
        row = file.get_by_animal(animal.OWL)
        message.send(row.url)
    except:
        message.send(NO_PICTURE_MESSAGE)


@listen_to(".*")
@in_channel(IMAGE_UPLOADED_CHANNEL)
def post(message):
    if "files" in message.body.keys():
        labels = set()
        for file in message.body["files"]:
            label = animal.predict(file["url_private_download"])
            if label is not None:
                f = File()
                f.add(file["permalink"], label)
                labels.add(label)

        for l in labels:
            message.react(animal.get_emoji(l))
