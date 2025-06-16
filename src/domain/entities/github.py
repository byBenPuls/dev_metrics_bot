from dataclasses import dataclass


@dataclass
class GitHubMetrics:
    username: str
    issues: int
    pull_requests: int
    lines_added: int
    lines_deleted: int
    discussion_comments: int
    stars: int
    forks: int
