#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers.
        Returns 0 if the subreddit is not found.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            return 0
        response.raise_for_status()
        # Raises an HTTPError if the HTTP
        # request returned an unsuccessful status code
        results = response.json().get("data")
        return results.get("subscribers", 0)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
