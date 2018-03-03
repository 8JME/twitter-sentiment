import tweepy
from textblob import TextBlob

# https://textblob.readthedocs.io/en/dev/quickstart.html

# Twitter API

consumer_key = ''
consumer_secret = ''

# Access Token - Generator

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('search-term-here')

for tweet in public_tweets:
    print()  # Space between each output
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
