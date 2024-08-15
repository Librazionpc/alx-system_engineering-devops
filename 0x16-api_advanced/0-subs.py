#!/usr/bin/python3

"""
query Reddit API and return the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Get the subsrcibers
    """
    url = f"https://www.reddit.com/subreddits/search.json?q={subreddit}"
    response = requests.get(url, allow_redirects=False)
    if (response.status_code != 200):
        return 0
    subscriber = 0
    json_data = response.json()
    children = json_data['data']['children']
    for child in children:
        if (child['data']['title'] == subreddit):
            subscriber = child['data']['subscribers']

    return (int(subscriber))