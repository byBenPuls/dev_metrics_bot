from src.bot.handlers.any import handle_any
from src.bot.handlers.get import handle_get
from src.bot.handlers.help import handle_help
from src.bot.handlers.start import handle_start
from src.bot.router import CommandRouter

router = CommandRouter()

router.add("/start", handle_start)
router.add("/help", handle_help)
router.add("/get", handle_get)
router.add("*", handle_any)
