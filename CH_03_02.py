import asyncio
import aioredis
import click
import json


async def main():
    redis = await aioredis.create_redis_pool("redis://localhost")
    await redis.flushall()
    await redis.set("app", "Chat")
    await redis.rpush("chat", json.dumps({"handle": "first_user", "message": "hey"}))
    await redis.rpush(
        "chat", json.dumps({"handle": "second_user", "message": "What's up?"})
    )
    await redis.rpush(
        "chat", json.dumps({"handle": "first_user", "message": "all good!"})
    )

    app_name = await redis.get("app", encoding="utf-8")
    click.secho(f" {app_name} ", fg="cyan", bold=True, bg="yellow")
    await redis.publish_json("feed", {"name": "Beverage", "price": 3})
    chat_messages = await redis.lrange("chat", 0, -1, encoding="utf-8")
    for message in chat_messages:
        message = json.loads(message)
        click.secho(f'  {message["handle"]} | {message["message"]} ', fg="cyan")
    redis.close()
    await redis.wait_closed()


"""
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
for item in r.scan_iter(match="item:*"):
    print(r.hgetall(item))
"""

asyncio.run(main())
