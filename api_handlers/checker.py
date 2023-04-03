import requests
from config import token


def all_comments():
    comments = []
    URL = f"https://api.vk.com/method/wall.getComments?owner_id=-185709218&post_id=63&count=100&sort=asc&access_token={token}&v=5.131"
    req = requests.get(URL)
    json_data = req.json()
    resp = json_data['response']['items']

    for i in resp:
        comments.append([i['text'], i['from_id']])

    return comments
