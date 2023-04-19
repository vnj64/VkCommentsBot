import asyncio

import aiohttp
from config import load_config

config = load_config('.env')


async def get_data(group_id, post_id):
    comments = []
    url = f"https://api.vk.com/method/wall.getComments?owner_id={group_id}&post_id={post_id}&count=10&sort=asc&access_token={config.api.api_token}&v=5.131"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            api_data = await response.json()
            resp = api_data['response']['items']
            for i in resp:
                comments.append([i['text'], i['from_id']])

            return comments


loop = asyncio.get_event_loop()
data = loop.run_until_complete(get_data("-185709218", "63"))
print(data)
