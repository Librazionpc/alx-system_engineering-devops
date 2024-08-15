#!/usr/bin/python3
"""Define number of subscribers function"""
import requests

def number_of_subscribers(subreddit):
    """Query the Reddit API and returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x016.project:v1.0.0 (by /u/ecalvoc)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        subreddit_data = response.json().get("data")
        if subreddit_data:
            return subreddit_data.get("subscribers")
        return 0
    except requests.RequestException as e:
        # Handle network-related errors
        print(f"Request error: {e}")
        return 0
    except ValueError:
        # Handle JSON decoding errors
        print("Error decoding JSON")
        return 0