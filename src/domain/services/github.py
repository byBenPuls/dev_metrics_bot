from abc import ABC, abstractmethod


class IGitHubService(ABC):
    @abstractmethod
    async def get_count_of_stars(self, username: str) -> int:
        pass

    @abstractmethod
    async def get_count_of_merged_pr(self, username: str) -> int:
        pass

    @abstractmethod
    async def get_count_of_repos(self, username: str) -> int:
        pass

    @abstractmethod
    async def get_count_of_opened_issues(self, username: str) -> int:
        pass

    @abstractmethod
    async def get_count_of_pr(self, username: str) -> int:
        pass

    @abstractmethod
    async def count_discussion_messages(self, username: str) -> int:
        pass

    @abstractmethod
    async def get_count_lines_changed(self, username: str) -> tuple[int, int]:
        pass

    @abstractmethod
    async def get_count_of_forks(self, username: str) -> int:
        pass
