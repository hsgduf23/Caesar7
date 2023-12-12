import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6604389549:AAERiYUY_Q0gb6jXeIoq-4nUcz03fIfQrWU")

    APP_ID = int(os.environ.get("APP_ID", 24859739))

    API_HASH = os.environ.get("API_HASH", "9883c3efb0a5a9f0a518893b918c1237")

    