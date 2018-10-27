import helpers.selenium_handler as h
import csv
import datetime
import os

URLCRIPTO = 'https://m.investing.com/crypto/'
h.get(URLCRIPTO)

hora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
lista = h.xpathList('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr')
tamanholista = len(lista)

for i in range(0,tamanholista):
    rank = h.xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr[{}]/td[1]'.format(i+1)).text
    nomeMoeda = h.xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr[{}]/td[2]'.format(i+1)).text
    valor = str(h.xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr[{}]/td[3]'.format(i+1)).text)
    valor = valor.replace(',','')

    file_exists = os.path.isfile("/home/lin/Documents/crypto.csv")
    with open("/home/lin/Documents/crypto.csv", 'a', newline='') as saida:
        headers = ['Rank', 'NomeMoeda', 'Valor-USD','Hora']
        writer = csv.DictWriter(saida, delimiter=';', lineterminator='\n', fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'Rank': rank, 'NomeMoeda': nomeMoeda, 'Valor-USD': valor, 'Hora': hora})