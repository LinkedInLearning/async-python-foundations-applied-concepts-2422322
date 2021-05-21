import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("http://localhost:8765") as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    if msg.data == "close cmd":
                        await ws.close()
                        break
                    else:
                        await ws.send_str(msg.data + "/answer")
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break
    #     ws = await session.ws_connect(
    #         'http://webscoket-server.org/endpoint')
    #     while True:
    #         msg = await ws.receive()

    #         if msg.tp == aiohttp.MsgType.text:
    #             if msg.data == 'close':
    #                 await ws.close()
    #                 break
    #             else:
    #                 ws.send_str(msg.data + '/answer')
    #         elif msg.tp == aiohttp.MsgType.closed:
    #             break
    #         elif msg.tp == aiohttp.MsgType.error:
    #             break


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
