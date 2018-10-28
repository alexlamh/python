import Helper.Helper as h
import csv
import datetime
import os

URLCRIPTO = 'https://m.investing.com/crypto/'
URLDOLAR = 'https://m.investing.com/currencies/usd-brl'
h.get(URLCRIPTO)

hora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
lista = h.listxpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr')
tamanholista = len(lista)

for i in range(0,tamanholista):
    rank = h.xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr['+str(i+1)+']/td[1]').text
    nomeMoeda = h.xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr['+str(i+1)+']/td[2]').text
    valor = str(h.xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr['+str(i+1)+']/td[3]').text)
    valor = valor.replace(',','')

    file_exists = os.path.isfile("Cripto.csv")
    with open("Cripto.csv", 'a', newline='') as saida:
        headers = ['Rank', 'NomeMoeda', 'Valor-USD','Hora']
        writer = csv.DictWriter(saida, delimiter=';', lineterminator='\n', fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'Rank': rank, 'NomeMoeda': nomeMoeda, 'Valor-USD': valor, 'Hora': hora})



h.get(URLDOLAR)
cotacaoDolar = str(h.xpath('//*[@id="siteWrapper"]/div[1]/section[2]/div[4]/div[2]/span[1]').text)


file_exists = os.path.isfile("Cotacao.csv")
with open("Cotacao.csv", 'a', newline='') as saida:
    headers = ['Moeda', 'Cotacao','Hora']
    writer = csv.DictWriter(saida, delimiter=';', lineterminator='\n', fieldnames=headers)
    if not file_exists:
        writer.writeheader()
    writer.writerow({'Moeda': 'USD-BRL', 'Cotacao': cotacaoDolar,'Hora': hora})




