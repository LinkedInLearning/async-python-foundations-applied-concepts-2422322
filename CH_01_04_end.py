import asyncio
from datetime import datetime
from asyncio.coroutines import coroutine
import click
import time


async def sleep_and_print(seconds):
    print(f"starting async {seconds} sleep 😴")
    await asyncio.sleep(seconds)
    print(f"finished async {seconds} sleep ⏰")
    return seconds


async def main():
    results = await asyncio.gather(sleep_and_print(3), sleep_and_print(6))
    coroutines = []
    for i in range(1, 11):
        coroutines.append(sleep_and_print(i))
    results = await asyncio.gather(*coroutines)
    print(results)


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
