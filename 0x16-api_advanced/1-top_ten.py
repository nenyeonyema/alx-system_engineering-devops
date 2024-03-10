#!/usr/bin/python3
""" Reddit API """
import requests


def top_ten(subreddit):
    """ Top 10 hot posts """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        posts = data['data']['children']

        if not posts:
            print("No posts found.")
            return

        for post in posts:
            print(post['data']['title'])

    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
