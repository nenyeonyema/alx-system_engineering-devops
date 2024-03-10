#!/usr/bin/python3
""" a recursive function that queries the Reddit API """
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Parses the title of all hot articles, and prints
    a sorted count of given keywords.
    """
    if not word_list:
        return

    if after is None:
        word_count = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    word_count[word.lower()] += title.count(word.lower())

        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                if count > 0:
                    print(f"{word}: {count}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2].split())
