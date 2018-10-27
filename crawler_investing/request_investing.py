import requests
import sys
from slacker import Slacker
import datetime as date
import boto3
import pytz

USD = 'https://m.investing.com/currencies/usd-brl'
EUR = 'https://m.investing.com/currencies/eur-brl'
HEADER = {'User-Agent':'Mozilla/5.0'}

SLACK_TOKEN = '#'
SLACK_CHANNEL = '#random'

#-----------datetime------------------------
tz = pytz.timezone('America/Sao_Paulo')
initial_time = date.datetime.now(tz)
def date_convert(var):
    return var.strftime("%Y-%m-%d %H:%M:%S")
timestamp = date_convert(initial_time)
#-------------------------------------------


def parameter(param):
    global moeda, cotacao, filename, filelog
    if param == '1':
        moeda = USD
        cotacao = 'USD/BRL'
        filename = 'dolar.txt'
        filelog = 'log_dolar.txt'
    elif param == '2':
        moeda = EUR
        cotacao = 'EUR/BRL'
        filename = 'euro.txt'
        filelog = 'log_euro.txt'


def currency():
    r = requests.get(moeda, headers=HEADER).text
    sub = r.find('lastInst'), r.find('quotesChange')
    r = r[sub[0]:sub[1]]
    sub = r.find('>'), r.find('</')
    r = r[sub[0]+1:sub[1]].strip()
    global cot
    cot = timestamp, cotacao, r
    cot = str(', '.join(cot))


def txt():
    f = open('/home/ec2-user/alex/' + filename, 'a')
    f.write(cot + '\n')


def logfile():
    f = open('/home/ec2-user/alex/' + filelog, 'a')
    f.write(log + '\n')
    print(log)


def s3():
    session = boto3.Session(
        aws_access_key_id='#',
        aws_secret_access_key='#',
    )
    s3 = session.resource('s3')
    data = open('/home/ec2-user/alex/{}'.format(filename), 'rb')
    s3.Bucket('s3.datalab-fiap-2018').put_object(Key='Desafio/Alex/{}'.format(filename), Body=data)
    dat = open('/home/ec2-user/alex/{}'.format(filelog), 'rb')
    s3.Bucket('s3.datalab-fiap-2018').put_object(Key='Desafio/Alex/{}'.format(filelog), Body=dat)


def slack():
    slackClient = Slacker(SLACK_TOKEN)
    slackClient.chat.post_message(SLACK_CHANNEL, cot)


def check_hour():
    if initial_time.strftime('%M') == '00':
        s3()
        slack()
        log_act3 = 'Upload no S3 com sucesso e mensagem enviado no Slack'
    else:
        log_act3 = ''
    return log_act3


if __name__ == '__main__':
    parameter(sys.argv[1])
    currency()
    log_act1 = 'Capturando cotacao'
    txt()
    log_act2 = 'Gravando em txt'
    log_act3 = check_hour()
    end_time = date.datetime.now(tz)
    duration = end_time - initial_time
    log = date_convert(initial_time), log_act1, log_act2, log_act3, date_convert(end_time), str(duration.total_seconds())
    log = ', '.join(log)
    logfile()
    try:
        pass
    except:
        print('-----------------------------------------------------------\n'
              'Para capturar a cotacao desejada, insira um dos argumentos:\n'
              'python investing.py 1 -> DOLAR\n'
              'python investing.py 2 -> EURO\n'
              '-----------------------------------------------------------')
