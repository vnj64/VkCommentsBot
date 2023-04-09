from config import load_config
import requests

config = load_config('.env')


def comments_getter(group_id, post_id):
    comments = []
    try:
        req = requests.get(f"https://api.vk.com/method/wall.getComments?owner_id={group_id}&post_id={post_id}"
                           f"&count=10&sort=asc&access_token={config.api.api_token}&v=5.131")
        json_data = req.json()
        resp = json_data['response']['items']
        for i in resp:
            comments.append([i['text'], i['from_id']])

    except Exception as e:
        return e

    return comments
