#!/usr/bin/python3
"""A function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "myApp/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        body = response.json()
        body_list = body.get('data').get('children')
        for item in body_list:
            title = item.get('data').get('title')
            print(title)
    else:
        print(None)
