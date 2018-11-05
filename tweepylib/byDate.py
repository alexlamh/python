
from auth_token.tweepy_auth import *
import tweepy
import datetime
import pytz
import os
import csv
from dateutil.parser import parse

tz = pytz.timezone('America/Sao_Paulo')

# https://apps.twitter.com
# Criar um APP e pegar as chaves
# CONSUMER KEY e CONSUMER_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# TOKEN ACCESS e TOKE SECRET
auth.set_access_token(TOKEN_ACCESS, TOKEN_SECRET)
api = tweepy.API(auth)
y=0


def convert_utc(param):
    data = parse(str(param) + ' -0300')
    hora = data.astimezone(pytz.utc).strftime("%H")
    hora = int(hora)
    return hora

def convert_sp(param):
    data = parse(str(param)+' +0000')
    data = data.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
    return data


dt_inicio = convert_utc('00:00')
dt_fim = convert_utc('23:00')

#'AgoraNaEconomia', 'EconomiaGV', 'B3_Oficial', 'Dinheirama', 'iGEconomia', 'br_economico'

username = 'AgoraNaEconomia'
startDate = datetime.datetime(2015, 8, 1, dt_inicio)
endDate = datetime.datetime(2018, 11, 1, dt_fim, 59)

tweets = []
path = '/home/lin/Documents/tweepy/{}.csv'.format(username)
contador = 0

for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode='extended').items():
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)


for tweet in tweets:
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
