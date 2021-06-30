import asyncio
import click

import websockets


def render_response(message):
    click.clear()
    if "BLASTOFF" in message:
        click.secho(message, blink=True, bold=True, fg="red")
    else:
        click.secho(message, bold=True, fg="blue")


async def astronout():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        is_ready = input("Are you ready? ")

        await websocket.send(is_ready)
        async for message in websocket:
            render_response(message)
            if "BLASTOFF" in message:
                return


async def main():
    await asyncio.gather(astronout(), astronout(), astronout(), astronout())


asyncio.run(main())
