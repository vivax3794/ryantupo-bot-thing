import logging

from .core import TwitchClient

from .secret import TOKEN


logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(name)s - %(levelname)s]: \"%(message)s\"",
        datefmt="%H:%M:%S",
        handlers=[
            logging.FileHandler("bot.log"),
            logging.StreamHandler()
            ]
        )

logger = logging.getLogger(__name__)

client = TwitchClient()

client.run(
        "therealvivax",
        TOKEN,
        "upjump"
    )
