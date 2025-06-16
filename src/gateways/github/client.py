from typing import Any

import aiohttp

from src.gateways.github.interface import IGitHubGateway
from src.gateways.github.models import (
    DetailedPullRequest,
    GitHubIssue,
    GitHubRepository,
    GitHubUser,
    PullRequest,
    RepoType,
)


class GitHub(IGitHubGateway):
    BASE_URL = "https://api.github.com"

    def __init__(self, token: str):
        self.session = aiohttp.ClientSession(base_url=self.BASE_URL)
        self._headers = {"Authorization": f"Bearer {token}"}

    async def _get(self, url: str, params: dict[str, Any] | None = None):
        response = await self.session.get(url, headers=self._headers, params=params)
        response.raise_for_status()
        return await response.json()

    async def get_user(self, username: str) -> GitHubUser:
        data = await self._get(f"https://api.github.com/users/{username}")

        return GitHubUser.from_dict(data)

    async def get_repos(
        self,
        username: str,
        repo_type: RepoType | None = None,
        per_page: int = 100,
        page: int = 1,
    ) -> list[GitHubRepository] | list:
        url = f"/users/{username}/repos"
        url += f"?per_page={per_page}&page={page}"
        url += f"&type={str(repo_type)}" if repo_type else ""

        data = await self._get(url)

        return [GitHubRepository.from_dict(repo) for repo in data]

    async def get_issues(self, username: str) -> list[GitHubIssue] | list:
        url = f"/search/issues?q=type:issue+author:{username}"
        data = await self._get(url)
        items = data.get("items", [])

        return [GitHubIssue.from_dict(issue) for issue in items]

    async def get_pull_requests(
        self, username: str, merged: bool = False
    ) -> list[PullRequest] | list:
        url = f"/search/issues?q=is:pr+author:{username}"
        url += "+is:merged" if merged else ""

        data = await self._get(url)
        items = data.get("items", [])

        return [PullRequest.from_dict(item) for item in items]

    async def get_pull_request(self, pr_url: str) -> DetailedPullRequest:
        data = await self._get(pr_url)

        return DetailedPullRequest.from_dict(data)

    async def close(self) -> None:
        await self.session.close()
