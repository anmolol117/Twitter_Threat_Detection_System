import snscrape.modules.twitter as sntwitter

for tweet in sntwitter.TwitterSearchScraper("protest").get_items():
    print(f"{tweet.date} - @{tweet.user.username}: {tweet.content}")
    break  # Just fetch one to test
