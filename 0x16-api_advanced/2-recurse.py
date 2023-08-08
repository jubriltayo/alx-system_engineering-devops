#!/usr/bin/python3
"""A function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    listed for a given subreddit using recursion
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = "https://www.reddit.com/r/{}/hot.json"\
        .format(subreddit)
    headers = {"User-Agent": "myApp/1.0"}
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        body = response.json()
        # query `after`
        after = body.get('data').get('after')
        body_list = body.get('data').get('children')
        for item in body_list:
            title = item.get('data').get('title')
            hot_list.append(title)
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return (hot_list)
    return (None)
