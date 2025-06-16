import asyncio
from dataclasses import dataclass

from src.domain.entities.github import GitHubMetrics
from src.domain.services.github import IGitHubService


@dataclass
class GetGitHubMetricsUseCase:
    github: IGitHubService

    async def execute(self, username: str) -> GitHubMetrics:
        (
            issues,
            pull_requests,
            discussion_comments,
            (lines_added, lines_deleted),
            stars,
            forks,
        ) = await asyncio.gather(
            self.github.get_count_of_opened_issues(username),
            self.github.get_count_of_pr(username),
            self.github.count_discussion_messages(username),
            self.github.get_count_lines_changed(username),
            self.github.get_count_of_stars(username),
            self.github.get_count_of_forks(username),
        )

        return GitHubMetrics(
            username=username,
            issues=issues,
            pull_requests=pull_requests,
            lines_added=lines_added,
            lines_deleted=lines_deleted,
            discussion_comments=discussion_comments,
            stars=stars,
            forks=forks,
        )
