from dataclasses import dataclass


class TelegramResponse:
    pass


@dataclass
class ResponseMessage(TelegramResponse):
    chat_id: int | str
    text: str
    parse_mode: str | None = None
    message_thread_id: int | None = None
    entities: list | None = None
    link_preview_options: dict | None = None
    disable_notification: bool | None = None
    protect_content: bool | None = None
    allow_paid_broadcast: bool | None = None
    message_effect_id: str | None = None
    reply_parameters: dict | None = None
    business_connection_id: str | None = None

    def to_dict(self) -> dict:
        return {
            key: value
            for key, value in {
                "chat_id": self.chat_id,
                "text": self.text,
                "parse_mode": self.parse_mode,
                "message_thread_id": self.message_thread_id,
                "entities": self.entities,
                "link_preview_options": self.link_preview_options,
                "disable_notification": self.disable_notification,
                "protect_content": self.protect_content,
                "allow_paid_broadcast": self.allow_paid_broadcast,
                "message_effect_id": self.message_effect_id,
                "reply_parameters": self.reply_parameters,
                "business_connection_id": self.business_connection_id,
            }.items()
            if value is not None
        }
