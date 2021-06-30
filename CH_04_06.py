import asyncio

from quart import Quart, websocket, render_template
from quart import g


app = Quart(__name__)

app.config["REDIS_URI"] = "redis://localhost/"
redis_handler = RedisHandler(app)
connections = set()


@app.websocket("/ws")
async def ws():
    connections.add(websocket._get_current_object())
    try:
        while True:
            message = await websocket.receive()
            send_coroutines = [connection.send(message) for connection in connections]
            await asyncio.gather(*send_coroutines)
    finally:
        connections.remove(websocket._get_current_object())


@app.route("/")
async def chat():
    return await render_template("chat.html")


# export QUART_APP=chat_app:app
# quart run -h localhost -p 3000
app.run(use_reloader=True)
