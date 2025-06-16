from src.bot.messages.github import format_github_metrics, get_loading_message
from src.core.container import get_container
from src.domain.entities.command import Command
from src.domain.entities.telegram import TelegramUpdate
from src.domain.use_cases.github import GetGitHubMetricsUseCase
from src.gateways.telegram.client import TelegramApiClient
from src.gateways.telegram.models import ResponseMessage


async def handle_get(update: TelegramUpdate, command: Command) -> ResponseMessage:
    container = get_container()
    telegram: TelegramApiClient = container.resolve(TelegramApiClient)

    if not command.args:
        return ResponseMessage(
            chat_id=update.message.chat.id,
            text="Please provide a GitHub username.\nExample: /get torvalds",
        )

    username = command.args.strip()

    await telegram.send_message(
        ResponseMessage(
            update.message.chat.id, get_loading_message(), parse_mode="HTMl"
        )
    )

    github_use_case: GetGitHubMetricsUseCase = container.resolve(
        GetGitHubMetricsUseCase
    )
    metrics = await github_use_case.execute(username)

    formatted = format_github_metrics(metrics)

    return ResponseMessage(
        chat_id=update.message.chat.id, text=formatted, parse_mode="HTML"
    )
