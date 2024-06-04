#!/usr/bin/python3
# Learning about api's usong reddit platform
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns 0 on Error
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditApp/0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']

            return subscribers
        else:
            return 0
    except (requests.RequestException, ValueError, KeyError):
        return 0
