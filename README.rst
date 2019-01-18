#############
aiohttp-limit
#############

.. image:: https://circleci.com/gh/underyx/aiohttp-limit.svg?style=shield
   :target: https://circleci.com/gh/underyx/aiohttp-limit
   :alt: CI Status

An aiohttp_ middleware for limiting connections.
Python 3.5+ is required for usage, 3.7+ is required for tests.

*****
Usage
*****

Just add ``LimitMiddleware`` as a middleware:

.. code-block:: python

    from aiohttp import web
    from aiohttp_limit import LimitMiddleware
    app = web.Application(middlewares=[LimitMiddleware(requests=10)])

This sample usage will restrict requests to 10 per worker.

.. _aiohttp: http://aiohttp.readthedocs.io/en/stable/
