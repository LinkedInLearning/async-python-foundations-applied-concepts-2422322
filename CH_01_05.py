import asyncio
from datetime import datetime
import click


async def sleep_five():
    pass  # your code here


async def sleep_three_then_five():
    pass  # your code here


async def main():
    results = "your code"
    print(results)


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
