import asyncio
from datetime import datetime
import click


async def sleep_five():
    await asyncio.sleep(5)
    print("sleep five done")


async def sleep_three_then_five():
    await asyncio.sleep(3)
    await sleep_five()


async def main():
    results = await asyncio.gather(sleep_five(), sleep_three_then_five())
    print(results)


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
