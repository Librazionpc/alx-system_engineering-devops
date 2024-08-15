#!/usr/bin/python3


"""
recursively queries the Reddit API and returns a list
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recursively queries the Reddit API and return a list
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if (response.status_code != 200):
        return None

    json_data = response.json()
    data = json_data.get('data', None)
    if data is None:
        return None

    children = data.get("children", [])
    if not children:
        return None

    for child in children:
        hot_list.append(child['data']['title'])

    after = data.get('after', None)
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)