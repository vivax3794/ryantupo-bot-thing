from .core.twitch import TwitchClient
import asyncio

from .secret import TOKEN


client = TwitchClient()

asyncio.run(client.start_bot(
        "therealvivax",
        TOKEN,
        "ryantupo"
    ))
