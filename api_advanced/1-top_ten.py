#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'My-User-Agent'}
    
    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response status is 200 OK
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        # Print titles of the first 10 posts
        for post in posts:
            print(post.get('data', {}).get('title'))
    else:
        # Print None if the subreddit is invalid
        print(None)

