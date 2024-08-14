#!/usr/bin/python3
"""Funtion that fecthes the top ten individual"""
import requests


def top_ten(subreddit):
    """Print title of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }
    result = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if result.status_code == 404:
        print("None")
        return
    results = result.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
