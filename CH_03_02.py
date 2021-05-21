import asyncio
import aioredis
import click


async def main():
    redis = await aioredis.create_redis_pool("redis://localhost")
    await redis.set("restaurant", "ASYNC PIZZA")
    await redis.hmset_dict("item:1", {"name": "Pizza", "price": 5})
    await redis.hmset_dict("item:2", {"name": "Salad", "price": 4})
    await redis.hmset_dict("item:3", {"name": "Beverage", "price": 3})

    restaurant = await redis.get("restaurant", encoding="utf-8")
    first_item = await redis.hget("item:1", "name", encoding="utf-8")
    first_item_price = await redis.hget("item:1", "price", encoding="utf-8")
    items = await redis.hscan("name")
    print(items)

    click.secho(f"    {restaurant}   ", fg="cyan", bold=True, bg="yellow")
    click.secho(f"  {first_item} | ${first_item_price} ", fg="cyan")
    redis.close()
    await redis.wait_closed()


asyncio.run(main())
