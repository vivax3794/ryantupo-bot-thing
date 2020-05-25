from .irc_protocol import Irc


class TwitchClient:
    """
    The twitch interface.
    """
    def __init__(self) -> None:
        self._irc = Irc()
        self.channel: str

    async def start_bot(self, username: str, token: str, channel: str) -> None:
        """
        Connect to twitch and start the bot.
        """
        await self._irc.connect(username, token, "irc.twitch.tv")
        await self._irc.join_channel(channel)

        self.channel = channel

        await self._irc.start_loop(self.on_message)

    async def on_message(self, user: str, msg: str) -> None:
        print(f"{user}: {msg}")
