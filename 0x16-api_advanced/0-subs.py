#!/usr/bin/python3
"""
0-subs.py

A script to query the Reddit API and retrieve the number of subscribers for a
given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 404:
            # Handle case where subreddit does not exist
            return 0
        else:
            # Handle other status codes (e.g., 403 for forbidden)
            return 0
    except requests.RequestException:
        # Handle request exceptions (e.g., connection timeout)
        return 0


# Ensure proper PEP8 compliance
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
