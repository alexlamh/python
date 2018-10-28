import helpers.selenium_handler as h
import csv
import datetime as date
import pytz
import os


def timestamp():
    tz = pytz.timezone('America/Sao_Paulo')
    timestamp = date.datetime.now(tz).strftime("%Y-%m-%d %H:%M")
    return timestamp


URL = 'https://m.investing.com/crypto/'
path = '/home/lin/Documents/crypto.csv'

if __name__ == '__main__':
    h.get(URL)

    coin_name = h.xpathList('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr/td[2]')
    coin_price = h.xpathList('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr/td[3]')

    for i in range(0,len(coin_name)):
        name = coin_name[i].text
        coin = coin_price[i].text
        coin = coin.replace(',','')  # removendo as vírgulas dos valores

        # gravando em csv
        file_exists = os.path.isfile(path)
        with open(path, 'a', newline='') as saida:
            headers = ['rank', 'coin', 'usd', 'timestamp']
            writer = csv.DictWriter(saida, delimiter=';', lineterminator='\n', fieldnames=headers)
            if not file_exists:
                writer.writeheader()
            writer.writerow({'rank': i+1, 'coin': name, 'usd': coin, 'timestamp': timestamp()})

    h.quit()
