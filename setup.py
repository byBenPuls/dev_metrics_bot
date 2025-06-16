import logging

from aiohttp import web

from src.web import init_app

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    web.run_app(init_app(), host="0.0.0.0", port=8080)
