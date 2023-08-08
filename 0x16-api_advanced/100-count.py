#!/usr/bin/python3
"""A function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    listed for a given subreddit using recursion,
    case-insensitive key and sorted value count
"""
import requests


def count_words(subreddit, word_list, kwargs={}, after=None):
    url = "https://www.reddit.com/r/{}/hot.json?after={}"\
        .format(subreddit, after)
    headers = {"User-Agent": "Chrome/89"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        body = response.json()
        # query `after`
        after = body.get('data').get('after')
        body_list = body.get('data').get('children')
        for item in body_list:
            title_list = item.get('data').get('title').lower().split()
            for title in title_list:
                for word in word_list:
                    if title == word:
                        if word in kwargs:
                            kwargs[word] += 1
                        else:
                            kwargs[word] = 1
        if after is not None:
            count_words(subreddit, word_list, kwargs, after)
        else:
            # sort by value instead of keys via lambda item[1]
            sorted_dict = {k: v for k, v in sorted(kwargs.items(),
                                                   key=lambda item: item[1])}
            [print("{}: {}".format(k, v)) for k, v in sorted_dict.items()]
    else:
        return (None)
