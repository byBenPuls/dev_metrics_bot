from aiohttp import web

from src.bot.view import telegram_view
from src.core.container import get_container
from src.core.settings import settings
from src.gateways.github.client import GitHub
from src.gateways.telegram.client import TelegramApiClient


async def on_startup(app):
    telegram: TelegramApiClient = get_container().resolve(TelegramApiClient)

    url = f"{settings.BOT_WEBHOOK_HOST}{settings.BOT_WEBHOOK_URL}"
    await telegram.set_webhook(url)


async def on_shutdown(app):
    container = get_container()

    telegram: TelegramApiClient = container.resolve(TelegramApiClient)
    github: GitHub = container.resolve(GitHub)

    await telegram.close()
    await github.close()


async def init_app():
    app = web.Application()

    app.router.add_route(
        "*",
        settings.BOT_WEBHOOK_URL,
        telegram_view,
    )

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    return app
