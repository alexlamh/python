# acessar https://apps.twitter.com para criar uma nova aplicação
# cada aplicação tem suas próprias chaves

import tweepy
import re
import auth_token.tweepy_auth as ac

# acessar a aba "Keys and Access Tokens"
# passa o Consumer Key e o Consumer Secret
auth = tweepy.OAuthHandler(ac.CONSUMER_KEY,ac.CONSUMER_SECRET)

# define o token de acesso
# para criar basta clicar em "Create my access token"
# passa o "Access Token" e o "Access Token Secret"
auth.set_access_token(ac.TOKEN_ACCESS,ac.TOKEN_SECRET)

# cria um objeto api
api = tweepy.API(auth)


# obtém tweets de um dado usuário
def obter_tweets(usuario, limite):
    resultados = api.user_timeline(screen_name=usuario, count=limite, tweet_mode='extended')
    tweets = []  # lista de tweets inicialmente vazia
    for r in resultados:
        # utiliza expressão regular para remover a URL do tweet
        # http pega o início da url
        # \S+ pega os caracteres não brancos (o final da URL)
        tweet = re.sub(r'http\S+', '', r.full_text)
        tweets.append(tweet.replace('\n', ' ')) # adiciona na lista
    return tweets  # retorna a lista de tweets


# escreve os tweets em um arquivo 'tweets.txt'
tweets = obter_tweets('jairbolsonaro', 1)

print(tweets)

# with open('tweets.txt', 'w') as f:
# 	f.write('\n'.join(tweets))