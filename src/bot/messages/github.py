from src.bot.messages.formatters import bold, code, italic, link
from src.domain.entities.github import GitHubMetrics


def get_loading_message() -> str:
    return (
        f"⏳ {bold('Fetching your GitHub magic...')}\n\n"
        "We're analyzing repositories, counting stars, reviewing pull requests, and "
        "digging through your code like true open-source archaeologists 🧑‍💻🪄\n\n"
        f"{italic('This may take a few seconds. Stay tuned!')}"
    )


def format_github_metrics(metrics: GitHubMetrics) -> str:
    return (
        f"{bold(f'📊 GitHub Annual Summary — {link(metrics.username, f"https://github.com/{metrics.username}")}')}\n\n"
        f"🐛 {bold('Issues opened:')} {code(metrics.issues)}\n"
        f"🚀 {bold('Pull Requests:')} {code(metrics.pull_requests)}\n"
        f"💬 {bold('Discussion comments:')} {code(metrics.discussion_comments)}\n\n"
        f"🧾 {bold('Lines of code:')} {code(f'+{metrics.lines_added}')} / {code(f'-{metrics.lines_deleted}')}\n"
        f"⭐ {bold('Stars received:')} {code(metrics.stars)}\n"
        f"🍴 {bold('Forks:')} {code(metrics.forks)}\n\n"
        f"{italic('Generated via GitHub Summary Bot')}"
    )
