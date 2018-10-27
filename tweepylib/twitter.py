import auth_token.tweepy_auth as tk
import tweepy

auth = tweepy.OAuthHandler(tk.CONSUMER_KEY, tk.CONSUMER_SECRET)
auth.set_access_token(tk.TOKEN_ACCESS, tk.TOKEN_SECRET)
api = tweepy.API(auth)

user = 'marcosmion'
hashtag = '#masterchef'
count = 10


def get_tweets(user, count):
    results = api.user_timeline(id=user, count=count, tweet_mode='extended')
    tweets = []
    for tweet in results:
        tweets.append(tweet.full_text)
        print(tweet.user.screen_name)
        print(tweet.created_at)
        print(tweet.full_text)
        print('---')
    return tweets


def get_hashtags(hashtag, count):
    results = api.search(q=hashtag, count=count, tweet_mode='extended')
    tweets = []
    for tweet in results:
        tweets.append(tweet)
        print(tweet.user.screen_name)
        print(tweet.created_at)
        print(tweet.full_text)
        print('---')
    return tweets


get_tweets(user, count)

get_hashtags(hashtag, count)

