from typing import Any

import redis.asyncio as redis

from src.gateways.redis.interface import IRedisGateway


class Redis(IRedisGateway):
    def __init__(self, redis_url: str):
        self._redis = redis.from_url(redis_url)

    async def set(self, key: str, value: Any, expire: int | None = None) -> None:
        await self._redis.set(key, value, ex=expire)

    async def get(self, key: str) -> Any:
        return await self._redis.get(key)

    async def delete(self, key: str) -> None:
        await self._redis.delete(key)
