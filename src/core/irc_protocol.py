from typing import Callable, Coroutine, Any
from .socket_wrapper import SocketWrapper


class Irc:
    """
    A wrapper around irc.
    """

    def __init__(self) -> None:
        self._sock = SocketWrapper()
        self._callback: Callable[[str, str], Coroutine[Any, Any, None]]

    async def connect(self, username: str, password: str, server: str, port: int = 6667) -> None:
        """
        Connect to a irc server.
        """
        await self._sock.connect(server, port)
        await self._sock.send(f"PASS {password}")
        await self._sock.send(f"NICK {username}")

    async def join_channel(self, channel_name: str) -> None:
        """
        Join a irc channel, (name is given without the first #)
        """
        await self._sock.send(f"JOIN #{channel_name}")

    async def send_message(self, channel: str, msg: str) -> None:
        """
        Send a message to the given channel.
        """
        await self._sock.send(f"PRIVMSG #{channel} :{msg}")

    async def _socket_event(self, data: str) -> None:
        """
        Called when the socket get's data.
        """
        if "PRIVMSG" in data:
            username, _ = data.split("!", 1)
            *_, msg = data.split(":", 2)


            await self._callback(username[1:], msg)

    async def start_loop(self, message_callback: Callable[[str, str], Coroutine[Any, Any, None]]) -> None:
        self._callback = message_callback
        await self._sock.read_loop(self._socket_event)
