import asyncio

import aioreq
import requests
from config import load_config

config = load_config('.env')


async def checker(group_id, post_id, count):
    async with aioreq.Client() as client:
        response = await client.get(f"https://api.vk.com/method/wall.getComments?owner_id={group_id}&post_id={post_id}"
                                    f"&count={count}&sort=asc&access_token={config.api.api_token}&v=5.131")

        print(response.content)

asyncio.run(checker("-185709218", "63", "100"))
