import asyncio
import pytest

from aiohttp import web
import aiohttp_limit as uut


class Handler:
    def __init__(self):
        self.started = False
        self.blocking = True
        self.done = False

    async def __call__(self, *args, **kwargs):
        self.started = True
        while self.blocking:
            await asyncio.sleep(0)
        return True


async def test_no_limiting():
    limiter = uut.LimitMiddleware(requests=10)

    handlers = [Handler() for _ in range(10)]
    tasks = [
        asyncio.create_task(limiter(request=None, handler=handler))
        for handler in handlers
    ]

    await asyncio.sleep(0)  # let the limiters run

    for handler in handlers:
        assert handler.started, "all requests should start"

    for handler in handlers:
        handler.blocking = False

    await asyncio.sleep(0)  # let the limiters run

    for task in tasks:
        assert task.result(), "all handlers should finish"


async def test_limiting():
    limiter = uut.LimitMiddleware(requests=10)

    handlers = [Handler() for _ in range(11)]
    tasks = [
        asyncio.create_task(limiter(request=None, handler=handler))
        for handler in handlers
    ]

    await asyncio.sleep(0)  # let the limiters run

    for handler in handlers[:-1]:
        assert handler.started, "first ten requests should start"
    assert not handlers[-1].started, "last request should not start"
    assert isinstance(
        tasks[-1].exception(), web.HTTPServiceUnavailable
    ), "last request should return HTTP 503 already before other requests finish"

    for handler in handlers:
        handler.blocking = False

    await asyncio.sleep(0)  # let the limiters run

    for task in tasks[:-1]:
        assert task.result(), "first ten handlers should finish"
