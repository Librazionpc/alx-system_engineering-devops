#!/usr/bin/python3
"""More On Api
"""
import requests


def recurse(subreddit, hot_list=[]):

    """Function that queries the Reddit API and returns a list
    containing the titles
    of all hot articles for a given subreddit.
    """

    params = {'limit': 100}
    if after:
        params['after'] = after

    headers = {'User-Agent': 'MyRedditApp/0.1'}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])

            after = data['data'].get('after')

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except (requests.RequestException, ValueError, KeyError):
        return None
