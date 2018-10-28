import helpers.selenium_handler as h
import csv
import datetime as date
import pytz

URL = 'https://m.investing.com/crypto/'

def timestamp():
    tz = pytz.timezone('America/Sao_Paulo')
    timestamp = date.datetime.now(tz).strftime("%Y-%m-%d %H:%M")
    return timestamp

def csv_write(param1, param2, param3, param4):
    with open('./downloads/crypto2.csv', 'a', newline='') as saida:
        escrever = csv.writer(saida, delimiter=';')
        escrever.writerow([param1, param2, param3, param4])
    return print('{} gravado'.format(param2))


if __name__ == '__main__':
    h.get(URL)

    coin_rank = h.xpathList('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr/td[1]')
    coin_name = h.xpathList('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr/td[2]')
    coin_price = h.xpathList('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr/td[3]')

    for i in coin_price:
        print(i.text)



