#!/usr/bin/python3
"""Module for task 1"""

import json  # Add this line to import the json module
import requests


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()  # Try to parse JSON
        children = data.get("data", {}).get("children", [])

        if not children:
            print("Subreddit '{}' does not exist or has no posts.".format(subreddit))
        else:
            for child in children:
                print(child.get("data", {}).get("title"))

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except json.decoder.JSONDecodeError as json_err:
        print(f"JSON decoding error occurred: {json_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <subreddit>")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
