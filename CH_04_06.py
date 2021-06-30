import json
import asyncio

from quart import Quart, websocket, render_template
from quart import g

from quart_redis import RedisHandler, get_redis

app = Quart(__name__)

app.config["REDIS_URI"] = "redis://localhost/"
redis_handler = RedisHandler(app)
connections = set()


@app.websocket("/ws")
async def ws():
    redis = get_redis()
    connections.add(websocket._get_current_object())
    try:
        while True:
            message = await websocket.receive()
            await redis.rpush("chat", json.dumps(message))
            send_coroutines = [connection.send(message) for connection in connections]
            await asyncio.gather(*send_coroutines)
    finally:
        connections.remove(websocket._get_current_object())


@app.route("/")
async def chat():
    redis = get_redis()
    messages = await redis.lrange("chat", 0, -1, encoding="utf-8")
    messages = [json.loads(message) for message in messages]
    return await render_template("chat_redis.html", messages=messages)


# export QUART_APP=chat_app:app
# quart run -h localhost -p 3000
app.run(use_reloader=True)
