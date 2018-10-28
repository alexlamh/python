import requests
import sys
import datetime as date
import pytz

USD = 'https://m.investing.com/currencies/usd-brl'
EUR = 'https://m.investing.com/currencies/eur-brl'
HEADER = {'User-Agent':'Mozilla/5.0'}

#-----------datetime------------------------
tz = pytz.timezone('America/Sao_Paulo')
initial_time = date.datetime.now(tz)
def date_convert(var):
    return var.strftime("%Y-%m-%d %H:%M")
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
    cot = str('; '.join(cot))


def txt():
    f = open('/home/lin/Documents/' + filename, 'a')
    f.write(cot + '\n')


if __name__ == '__main__':
    try:
        parameter(sys.argv[1])
        currency()
        txt()
    except:
        print('-----------------------------------------------------------\n'
              'Para capturar a cotacao desejada, insira um dos argumentos:\n'
              'python investing.py 1 -> DOLAR\n'
              'python investing.py 2 -> EURO\n'
              '-----------------------------------------------------------')
