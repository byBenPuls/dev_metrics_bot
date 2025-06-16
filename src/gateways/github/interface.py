from abc import ABC, abstractmethod

from src.gateways.github.models import (
    DetailedPullRequest,
    GitHubIssue,
    GitHubRepository,
    GitHubUser,
    PullRequest,
    RepoType,
)


class IGitHubGateway(ABC):
    @abstractmethod
    async def get_user(self, username: str) -> GitHubUser:
        pass

    @abstractmethod
    async def get_repos(
        self,
        username: str,
        repo_type: RepoType | None = None,
        per_page: int = 100,
        page: int = 1,
    ) -> list[GitHubRepository] | list:
        pass

    @abstractmethod
    async def get_issues(self, username: str) -> list[GitHubIssue] | list:
        pass

    @abstractmethod
    async def get_pull_requests(
        self,
        username: str,
        merged: bool = False,
    ) -> list[PullRequest]:
        pass

    @abstractmethod
    async def get_pull_request(self, pr_url: str) -> DetailedPullRequest:
        pass
