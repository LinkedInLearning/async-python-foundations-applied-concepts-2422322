import asyncio
from datetime import datetime
import click


async def sleep_and_print(seconds):
    print(f"starting async {seconds} sleep 😴")
    await asyncio.sleep(seconds)
    print(f"finished async {seconds} sleep ⏰")
    return seconds


async def main():
    print(
        await asyncio.gather(
            sleep_and_print(1),
            sleep_and_print(2),
            sleep_and_print(3),
            sleep_and_print(4),
            sleep_and_print(5),
            sleep_and_print(6),
        )
    )


loop = asyncio.get_event_loop()
start = datetime.now()
loop.run_until_complete(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
