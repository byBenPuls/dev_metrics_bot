from src.domain.entities.command import Command
from src.domain.entities.telegram import TelegramUpdate
from src.gateways.telegram.models import ResponseMessage


async def handle_any(update: TelegramUpdate, command: Command):
    return ResponseMessage(
        update.message.chat.id, "Check available commands using /help"
    )
