#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns 0 on Error
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        else:
            return 0
    except Exception:
        return 0
