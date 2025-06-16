import logging
from collections.abc import Awaitable, Callable

from src.core.container import get_container
from src.domain.entities.command import Command
from src.domain.entities.telegram import TelegramUpdate
from src.gateways.telegram.client import TelegramApiClient
from src.gateways.telegram.models import ResponseMessage, TelegramResponse

Handler = Callable[[TelegramUpdate, Command], Awaitable[TelegramResponse]]

logger = logging.getLogger(__name__)


class CommandRouter:
    def __init__(self):
        self._routes: dict[str, Handler] = {}
        self._fallback: Handler | None = None

    def add(self, name: str, handler: Handler):
        if name == "*":
            logger.info(f"Registred fallback: {handler.__name__}")
            self._fallback = handler
        else:
            logger.info(f"Registred command: {name} → {handler.__name__}")
            self._routes[name] = handler

    async def dispatch(self, update: TelegramUpdate):
        self._telegram: TelegramApiClient = get_container().resolve(TelegramApiClient)

        message = update.message
        cmd = message.get_command() if message else None

        match cmd:
            case Command() if cmd.name in self._routes:
                handler = self._routes[cmd.name]
                response = await handler(update, cmd)

            case _ if self._fallback:
                response = await self._fallback(update, cmd)

            case _:
                return

        match response:
            case ResponseMessage():
                await self._telegram.send_message(response)
            case _:
                pass
