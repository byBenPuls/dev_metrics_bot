from typing import Any

import aiohttp

from src.gateways.telegram.interface import ITelegramGateway
from src.gateways.telegram.models import ResponseMessage


class TelegramApiClient(ITelegramGateway):
    def __init__(self, bot_token: str):
        self._base_url = f"https://api.telegram.org/bot{bot_token}"
        self._session = aiohttp.ClientSession()

    async def _post(self, method: str, json: dict) -> dict:
        url = f"{self._base_url}/{method}"

        resp = await self._session.post(url, json=json)
        resp.raise_for_status()

        return await resp.json()

    async def _get(self, method: str) -> dict:
        url = f"{self._base_url}/{method}"

        resp = await self._session.get(url)
        resp.raise_for_status()

        return await resp.json()

    async def set_webhook(self, url: str) -> None:
        await self._post("setWebhook", {"url": url})

    async def delete_webhook(self) -> None:
        await self._post("deleteWebhook", {})

    async def get_webhook_info(self) -> dict[str, Any]:
        return await self._get("getWebhookInfo")

    async def send_message(self, message: ResponseMessage) -> None:
        await self._post("sendMessage", message.to_dict())

    async def answer_callback_query(
        self, callback_query_id: str, text: str | None = None
    ) -> None:
        data = {"callback_query_id": callback_query_id}
        if text:
            data["text"] = text
        await self._post("answerCallbackQuery", data)

    async def close(self) -> None:
        await self._session.close()
