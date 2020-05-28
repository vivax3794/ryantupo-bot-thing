from .core.twitch import TwitchClient

from .secret import TOKEN


client = TwitchClient()

client.run(
        "therealvivax",
        TOKEN,
        "vivax3794"
    )
