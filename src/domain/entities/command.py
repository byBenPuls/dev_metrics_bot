from dataclasses import dataclass


@dataclass
class Command:
    name: str
    args: str | None
