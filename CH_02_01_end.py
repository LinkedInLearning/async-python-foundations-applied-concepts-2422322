from datetime import datetime
from pprint import pp
import asyncio

import aiohttp
import click
import requests

urls = [
    "http://httpbin.org/get?text=python",
    "http://httpbin.org/get?text=is",
    "http://httpbin.org/get?text=fun",
    "http://httpbin.org/get?text=and",
    "http://httpbin.org/get?text=useful",
    "http://httpbin.org/get?text=you",
    "http://httpbin.org/get?text=can",
    "http://httpbin.org/get?text=almost",
    "http://httpbin.org/get?text=do",
    "http://httpbin.org/get?text=anything",
    "http://httpbin.org/get?text=with",
    "http://httpbin.org/get?text=it",
]


async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return data["args"]


start = datetime.now()


async def main():
    async with aiohttp.ClientSession() as session:
        data = await asyncio.gather(*[fetch(session, url) for url in urls])
        pp(data)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
