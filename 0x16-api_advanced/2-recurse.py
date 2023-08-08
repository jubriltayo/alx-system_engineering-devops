#!/usr/bin/python3
"""A function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    listed for a given subreddit using recursion
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json?after={}"\
        .format(subreddit, after)
    headers = {"User-Agent": "myApp/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        body = response.json()
        # query `after`
        after = body.get('data').get('after')
        body_list = body.get('data').get('children')
        for item in body_list:
            title = item.get('data').get('title')
            hot_list.append(title)
        if after is not None:
            recurse(subreddit, hot_list, after)
        return (hot_list)
    return (None)
