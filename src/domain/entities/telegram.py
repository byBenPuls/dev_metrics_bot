from dataclasses import dataclass
from enum import StrEnum
from typing import Any

from src.domain.entities.command import Command


class MessageEntityType(StrEnum):
    MENTION = "mention"

    HASHTAG = "hashtag"
    CASHTAG = "cashtag"
    BOT_COMMAND = "bot_command"
    URL = "url"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"

    STRIKETHROUGH = "strikethrough"
    SPOILER = "spoiler"

    BLOCKQUOTE = "blockquote"
    EXPANDABLE_BLOCKQUOTE = "expandable_blockquote"
    CODE = "code"
    PRE = "pre"
    TEXT_LINK = "text_link"
    TEXT_MENTION = "text_mention"

    CUSTOM_EMOJI = "custom_emoji"


@dataclass
class TelegramUser:
    id: int
    is_bot: bool
    first_name: str
    last_name: str | None = None
    username: str | None = None
    language_code: str | None = None

    @classmethod
    def from_dict(cls, data: dict) -> "TelegramUser":
        return cls(
            id=data["id"],
            is_bot=data["is_bot"],
            first_name=data["first_name"],
            last_name=data.get("last_name"),
            username=data.get("username"),
            language_code=data.get("language_code"),
        )


@dataclass
class TelegramChat:
    id: int

    type: str

    @classmethod
    def from_dict(cls, data: dict) -> "TelegramChat":
        return cls(
            id=data["id"],
            type=data["type"],
        )


@dataclass
class MessageEntity:
    offset: int
    length: int
    type: MessageEntityType
    url: str | None = None
    user: TelegramUser | None = None
    language: str | None = None
    custom_emoji_id: str | None = None

    @classmethod
    def from_dict(cls, data: dict) -> "MessageEntity":
        return cls(
            offset=data["offset"],
            length=data["length"],
            type=MessageEntityType(data["type"]),
            url=data.get("url"),
            user=TelegramUser.from_dict(data["user"]) if "user" in data else None,
            language=data.get("language"),
            custom_emoji_id=data.get("custom_emoji_id"),
        )


@dataclass
class TelegramMessage:
    message_id: int
    chat: TelegramChat
    user: "TelegramUser"
    date: int
    text: str | None = None
    document: dict[str, Any] | None = None
    entities: list[MessageEntity] | None = None

    @classmethod
    def from_dict(cls, data: dict) -> "TelegramMessage":
        return cls(
            message_id=data["message_id"],
            chat=TelegramChat.from_dict(data["chat"]),
            user=TelegramUser.from_dict(data["from"]),
            date=data["date"],
            text=data.get("text"),
            document=data.get("document"),
            entities=[MessageEntity.from_dict(e) for e in data.get("entities", [])],
        )

    def get_command(self) -> Command | None:
        if not self.text or not self.entities:
            return None

        for e in self.entities:
            if e.type == MessageEntityType.BOT_COMMAND:
                full = self.text[e.offset : e.offset + e.length]
                rest = self.text[e.offset + e.length :].strip() or None

                return Command(name=full, args=rest)

        return None


@dataclass
class TelegramUpdate:
    update_id: int
    message: TelegramMessage

    @classmethod
    def from_dict(cls, data: dict) -> "TelegramUpdate":
        return cls(
            update_id=data["update_id"],
            message=TelegramMessage.from_dict(data["message"]),
        )
