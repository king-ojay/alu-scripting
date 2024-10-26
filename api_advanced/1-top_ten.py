#!/usr/bin/python3
""" 1-top_ten.py """

import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.top_ten:v1.0 (by u/yourusername)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data")
            posts = data.get("children", [])[:10]
            for post in posts:
                print(post["data"]["title"])
        else:
            print("None")
    except Exception:
        print("None")
