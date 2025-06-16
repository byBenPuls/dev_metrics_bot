from functools import lru_cache

import punq

from src.core.settings import settings
from src.domain.services.github import IGitHubService
from src.domain.use_cases.github import GetGitHubMetricsUseCase
from src.gateways.github.client import GitHub
from src.gateways.redis.client import Redis
from src.gateways.telegram.client import TelegramApiClient
from src.services.github import GitHubService


@lru_cache(1)
def get_container() -> punq.Container:
    return _init_container()


def _init_container() -> punq.Container:
    container = punq.Container()

    container.register(
        Redis,
        scope=punq.Scope.singleton,
        factory=lambda: Redis(
            redis_url=settings.redis_url,
        ),
    )
    container.register(GitHub, factory=lambda: GitHub(token=settings.GITHUB_TOKEN))
    container.register(
        TelegramApiClient,
        factory=lambda: TelegramApiClient(bot_token=settings.BOT_TOKEN),
    )

    container.register(IGitHubService, GitHubService)
    container.register(GetGitHubMetricsUseCase)

    return container
