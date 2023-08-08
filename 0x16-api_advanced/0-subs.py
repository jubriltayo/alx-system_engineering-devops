#!/usr/bin/python3
"""A function that queries the Reddit API and
    returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "myApp/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        body = response.json()
        subscribers = body.get('data').get('subscribers')
        return subscribers
    return 0
