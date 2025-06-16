import asyncio
from dataclasses import dataclass

from src.domain.services.github import IGitHubService
from src.gateways.github.client import GitHub
from src.gateways.github.models import RepoType


@dataclass
class GitHubService(IGitHubService):
    client: GitHub

    async def get_count_of_stars(self, username: str) -> int:
        repos = await self.client.get_repos(username, repo_type=RepoType.OWNER)
        return sum(repo.stargazers_count for repo in repos)

    async def get_count_of_merged_pr(self, username: str) -> int:
        pull_requests = await self.client.get_pull_requests(username, merged=True)
        return len(pull_requests)

    async def get_count_of_repos(self, username: str) -> int:
        repos = await self.client.get_repos(username, repo_type=RepoType.OWNER)
        return len(repos)

    async def get_count_of_opened_issues(self, username: str) -> int:
        issues = await self.client.get_issues(username)
        return len(issues)

    async def get_count_of_pr(self, username: str) -> int:
        pull_requests = await self.client.get_pull_requests(username, merged=False)
        return len(pull_requests)

    async def count_discussion_messages(self, username: str) -> int:
        return -1  # TODO: rewrite

    def _calculate_lines(self, summary: list[tuple[int, int]]) -> tuple[int, int]:
        total_add = 0
        total_del = 0

        for additions, deletions in summary:
            total_add += additions
            total_del += deletions

        return total_add, total_del

    async def _get_count_of_changed_lines_from_pr(self, url: str) -> tuple[int, int]:
        data = await self.client.get_pull_request(url)
        return data.additions, data.deletions

    async def get_count_lines_changed(self, username: str) -> tuple[int, int]:
        pull_requests = await self.client.get_pull_requests(username, merged=False)

        urls = (f"{pr.repository_url}/pulls/{pr.number}" for pr in pull_requests)
        tasks = (self._get_count_of_changed_lines_from_pr(url) for url in urls)

        result = await asyncio.gather(*tasks)

        return self._calculate_lines(result)

    async def get_count_of_forks(self, username: str) -> int:
        repos = await self.client.get_repos(username, repo_type=RepoType.ALL)

        count = 0
        for repo in repos:
            if repo.fork:
                count += 1

        return count
