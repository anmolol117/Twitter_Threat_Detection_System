# twitter_fetcher.py

import tweepy
import time

# Replace with your credentials
BEARER_TOKEN = "ENTER_YOUR_BEARER_TOKEN"
client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

from datetime import datetime
import random

def fetch_tweets_with_tweepy(query="protest", max_results=10):
    try:
        response = client.search_recent_tweets(
            query=query,
            max_results=max_results,
            tweet_fields=["created_at", "author_id", "text"]
        )

        if not response.data:
            print("No tweets found.")
            return []

        results = []
        for i, tweet in enumerate(response.data):
            print("---------")
            print(f"Tweet by user {tweet.author_id} at {tweet.created_at}")
            print(tweet.text)

            tweet_data = {
                "platform": "Twitter",
                "username": f"user_{tweet.author_id}",
                "content": tweet.text,
                "url": f"https://twitter.com/i/web/status/{tweet.id}",
                "timestamp": tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")
            }
            results.append(tweet_data)

        return results

    except tweepy.TooManyRequests:
        print("⚠️ Rate limit reached. Sleeping for 15 minutes...")
        time.sleep(15 * 60)
        return fetch_tweets_with_tweepy(query, max_results)

    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return []

import time
import random
from datetime import datetime

def fetch_tweets_with_tweepy_dummy(query="protest", max_results=10):
    dummy_texts = [
        "Burn it all down! They’ll pay tonight.",
        "Let’s start a revolution tomorrow!",
        "March peacefully and make your voices heard.",
        "Meet me with the supplies. You know where.",
        "Explosives ready. Waiting for the signal.",
        "We are planning a bombing tonight.",
        "The rally starts at 6PM downtown.",
        "Join us in our peaceful protest today.",
        "I need a recipe for smoke bombs lol.",
        "Just chilling at home, nothing suspicious."
    ]

    results = []
    for i in range(max_results):
        text = dummy_texts[i % len(dummy_texts)]
        tweet = {
            "platform": "Twitter",
            "username": f"dummy_user{random.randint(1000, 9999)}",
            "content": text,
            "url": f"https://twitter.com/dummy_user/status/{100000 + i}",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"Tweet by user {tweet['username']} at {tweet['timestamp']}")
        print(tweet['content'])
        results.append(tweet)

    return results

if __name__ == "__main__":
    r = fetch_tweets_with_tweepy_dummy("protest", max_results=10)
    print(r)
