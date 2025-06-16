from aiohttp.web import Request, Response

from src.bot.handlers.router import router
from src.domain.entities.telegram import TelegramUpdate


async def telegram_view(request: Request):
    raw_data = await request.json()
    data = TelegramUpdate.from_dict(raw_data)

    await router.dispatch(data)

    return Response(text="OK")
