import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6969473829:AAEXkXEr4CuC5bTqt-NbUimf4_8XJ99WKww")

    APP_ID = int(os.environ.get("APP_ID", 20456661))

    API_HASH = os.environ.get("API_HASH", "c698e32d5f5f99a7275458b0c4369639")

    