#!/usr/bin/python3
""" Subreddit API number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except Exception as e:
        print(f"Error: {e}")
        return 0


if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    print(number_of_subscribers(subreddit))
