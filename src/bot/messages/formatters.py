def bold(text) -> str:
    return f"<b>{str(text)}</b>"


def italic(text) -> str:
    return f"<i>{str(text)}</i>"


def underline(text) -> str:
    return f"<u>{str(text)}</u>"


def strikethrough(text) -> str:
    return f"<s>{str(text)}</s>"


def spoiler(text) -> str:
    return f'<span class="tg-spoiler">{str(text)}</span>'


def code(text) -> str:
    return f"<code>{str(text)}</code>"


def pre(text, language="") -> str:
    text = str(text)
    if language:
        return f'<pre language="{str(language)}">{text}</pre>'

    return f"<pre>{text}</pre>"


def link(label, url) -> str:
    return f'<a href="{str(url)}">{str(label)}</a>'
