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
    headers = {'User-agent': 'request'}

    response = requests.get(url, headers=headers, allow_redirect=false)
    if response.status_code == 200:
        data = response.json().get("data")
        subscribers = data.get("subscribers")
        return subscribers
    else:
        return 0
