from aiohttp import web


@web.middleware
class LimitMiddleware:
    def __init__(self, *, requests):
        self.max_requests = requests
        self._request_count = 0

    async def __call__(self, request, handler):
        if self._request_count == self.max_requests:
            raise web.HTTPServiceUnavailable(reason="concurrent request limit reached")

        self._request_count += 1

        try:
            response = await handler(request)
        except Exception as ex:
            raise ex
        else:
            return response
        finally:
            self._request_count -= 1
