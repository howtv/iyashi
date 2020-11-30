import functools
import os

from dotenv import load_dotenv

import db

if os.environ.get("ENVIRONMENT") is None:
    load_dotenv()

API_TOKEN = os.environ["SLACK_BOT_TOKEN"]

PLUGINS = ["response"]

IMAGE_UPLOADED_CHANNEL = os.environ["IMAGE_UPLOADED_CHANNEL"]


def in_channel(allow_channel):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(message, *args, **kargs):
            channel_id = message.body["channel"]
            channel_info = message.channel._client.channels[channel_id]
            channel = channel_info["name"]
            if allow_channel not in (channel, channel_id):
                return
            return func(message, *args, **kargs)

        return wrapper

    return decorator
