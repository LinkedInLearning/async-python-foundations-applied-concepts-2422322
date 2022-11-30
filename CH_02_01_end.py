from datetime import datetime
from pprint import pprint
import asyncio

import aiohttp
import click

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


async def fetch_args(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return data["args"]


async def main():
    async with aiohttp.ClientSession() as session:
        # create a collection of coroutines(can be done with comprehension )
        fetch_coroutines = []
        for url in urls:
            fetch_coroutines.append(fetch_args(session, url))
        # wake up coroutines with gather
        data = await asyncio.gather(*fetch_coroutines)
        pprint(data)


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
