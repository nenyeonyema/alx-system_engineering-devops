#!/usr/bin/python3
""" Reddit API """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list containing the titles of all hot articles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
