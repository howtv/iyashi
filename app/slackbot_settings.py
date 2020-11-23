import os

from dotenv import load_dotenv

import db

if os.environ.get("ENVIRONMENT") is None:
    load_dotenv()

API_TOKEN = os.environ["SLACK_BOT_TOKEN"]

PLUGINS = ["response"]
