import auth_token.tweepy_auth as tk
import tweepy

auth = tweepy.OAuthHandler(tk.CONSUMER_KEY, tk.CONSUMER_SECRET)
auth.set_access_token(tk.TOKEN_ACCESS, tk.TOKEN_SECRET)

api = tweepy.API(auth)

user = 'jairbolsonaro'
count = 10

tweets = api.user_timeline(id=user, count=count, tweet_mode='extended')

for tweet in tweets:
    print(tweet.full_text)
    print('---------')