from src.bot.messages.start import start_message
from src.domain.entities.command import Command
from src.domain.entities.telegram import TelegramUpdate
from src.gateways.telegram.models import ResponseMessage


async def handle_help(update: TelegramUpdate, command: Command):
    return ResponseMessage(update.message.chat.id, start_message, parse_mode="HTML")
