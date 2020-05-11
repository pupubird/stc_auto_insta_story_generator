import urllib.request
import json


def generate_short_link(url, key):
    shorterner = f"""https://us-central1-stc-insta-link-shortener.cloudfunctions.net/app/api/links/"""
    obj = {
        "token":key,
        "link":url
    }
    res = json.loads(urllib.requests.post('https://httpbin.org/post', json=obj))
    
    return res
