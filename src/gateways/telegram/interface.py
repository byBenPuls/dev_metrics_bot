from abc import ABC, abstractmethod
from typing import Any

from src.gateways.telegram.models import ResponseMessage


class ITelegramGateway(ABC):
    @abstractmethod
    async def set_webhook(self, url: str) -> None:
        pass

    @abstractmethod
    async def delete_webhook(self) -> None:
        pass

    @abstractmethod
    async def get_webhook_info(self) -> dict[str, Any]:
        pass

    @abstractmethod
    async def send_message(self, message: ResponseMessage) -> None:
        pass

    @abstractmethod
    async def answer_callback_query(
        self, callback_query_id: str, text: str | None = None
    ) -> None:
        pass
