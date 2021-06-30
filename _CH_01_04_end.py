import asyncio

import time
from datetime import datetime

import click


async def sleep_and_print(seconds):
    print(f"starting {seconds} sleep 😴")
    await asyncio.sleep(seconds)
    print(f"finished {seconds} sleep ⏰")
    return seconds

async def main():
    coroutines = []
    for i in range(1, 11):
        coroutines.append(sleep_and_print(i))
    
    results = await asyncio.gather(*coroutines)
    print(results)

start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
