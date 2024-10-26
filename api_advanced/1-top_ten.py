#!/usr/bin/python3
"""1-top_ten.py"""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditApp/0.0.1'}

    try:
        # Perform the GET request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if we received a valid response
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            
            # Check if there are posts; if not, print "None"
            if not posts:
                print("None")
            else:
                # Print the titles of the first 10 hot posts
                for post in posts[:10]:
                    print(post.get("data", {}).get("title"))
                    
        else:
            # Print "None" if the status code is not 200 (invalid subreddit or forbidden)
            print("None")
    
    except Exception as e:
        # Print "None" if there is an exception, such as a network error
        print("None")
