from auth_token.tweepy_auth import *
from dateutil.parser import parse
import tweepy
import pytz
import os
import csv

tz = pytz.timezone('America/Sao_Paulo')

# https://apps.twitter.com
# Criar um APP e pegar as chaves
# CONSUMER KEY e CONSUMER_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# TOKEN ACCESS e TOKE SECRET
auth.set_access_token(TOKEN_ACCESS, TOKEN_SECRET)
api = tweepy.API(auth)


# Converter o horário
def convert_sp(param):
    data = parse(str(param)+' +0000')
    data = data.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
    return data


# Pegar tweets por usuário (max: 3200 tweets)
def get_all_tweets(username, qtd):
    contador=0
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode='extended').items(qtd):
        contador += 1
        list = convert_sp(tweet.created_at), tweet.user.screen_name, tweet.full_text
        print(contador)
        print(tweet.user.screen_name)
        print(convert_sp(tweet.created_at))
        print(tweet.full_text)

        # gravando em csv
        file_exists = os.path.isfile(path)
        with open(path, 'a', newline='') as saida:
            headers = ['timestamp', 'user', 'tweets']
            writer = csv.DictWriter(saida, delimiter=';', lineterminator='\n', fieldnames=headers)
            if not file_exists:
                writer.writeheader()
            writer.writerow({'timestamp': list[0], 'user': list[1], 'tweets': list[2]})


# Buscar no twitter (#hastags e afins)
def get_search(search, qtd):
    results = tweepy.Cursor(api.search, q=search, tweet_mode='extended', lang='pt-br').items(qtd)
    c=0
    for tweet in results:
        c+=1
        print(c)
        print(tweet.user.screen_name)
        print(convert_sp(tweet.created_at))
        print(tweet.full_text)
        print('---')

username = 'infomoney'
search = '#masterchef'
qtd = 5000
path = '/home/lin/Documents/tweepy/{}.csv'.format(username)
if __name__ == '__main__':
    # get_search(search, qtd)
    get_all_tweets(username, qtd)

