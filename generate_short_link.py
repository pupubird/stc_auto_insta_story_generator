import requests
import json


def generate_short_link(url, key):
    shorterner = f"""https://us-central1-stc-insta-link-shortener.cloudfunctions.net/app/api/links/"""
    obj = {
        "token": key,
        "link": url
    }
    res = requests.post(shorterner, json=obj)
    res_json = res.json()
    return res
