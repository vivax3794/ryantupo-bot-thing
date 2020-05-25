import asyncio
from typing import Callable, Coroutine, Any


class SocketWrapper:
    """
    A better interface to sockets.
    """
    def __init__(self) -> None:
        self._reader: asyncio.StreamReader
        self._writer: asyncio.StreamWriter

    async def connect(self, addr: str, port: int) -> None:
        """
        Connect a socket to a server.
        """
        self._reader, self._writer = await asyncio.open_connection(host=addr, port=port)

    async def send(self, message: str) -> None:
        """
        Send a msg over the socket.
        """
        self._writer.write((message + "\r\n").encode())
        await self._writer.drain()

    async def read_loop(self, callback: Callable[[str], Coroutine[Any, Any, None]]) -> None:
        while True:
            raw_data: bytes = await self._reader.readline()
            data: str = raw_data.decode().rstrip("\r\n")

            asyncio.create_task(callback(data))
