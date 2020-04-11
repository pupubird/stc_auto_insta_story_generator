import urllib.request
import json


def generate_short_link(url, key, name):
    url = f"""https://cutt.ly/api/api.php?key={key}&short={url}&name={name}"""
    res = json.loads(urllib.request.urlopen(url).read(1000).decode('utf-8'))
    return res
