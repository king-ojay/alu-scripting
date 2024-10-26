#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API to print the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'My-User-Agent'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                print(post["data"]["title"])
        else:
            print(None)
    except Exception:
        print(None)

