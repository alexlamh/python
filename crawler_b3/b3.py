import requests
from bs4 import BeautifulSoup
import os
import csv
from datetime import date, timedelta

today = date.today().strftime('%d/%m/%Y')
yesterday = date.today() - timedelta(1)
yesterday = yesterday.strftime('%d/%m/%Y')

path = '/home/lin/Documents/b3_scrap/b3.csv'

URL = 'http://www2.bmf.com.br/pages/portal/bmfbovespa/lumis/lum-retroativo-por-periodo-ptBR.asp'
HEADER = {'User-Agent':'Mozilla/5.0'}

dataInicio = yesterday
dataFim = today

r = requests.post(URL, data={'txtDataInicio': dataInicio, 'txtDataFim': dataFim}).text

soup = BeautifulSoup(r)
try:
    soup = BeautifulSoup(str(soup.find_all('tbody')[0]))
    tr = soup.find_all('tr')

    for i in tr:
        lista = i.text
        lista = lista.strip().split('\n')
        print(lista)

        # gravando em csv
        file_exists = os.path.isfile(path)
        with open(path, 'a', newline='') as saida:
            headers = ['data_contratacao', 'data_liquidacao', 'taxa_abertura', 'cenario_stress', 'qtd_negocios',
                       'vol_contratado_brl', 'vol_contratado_usd', 'taxa_contratada_min', 'taxa_contratada_med',
                       'taxa_contratada_max']
            writer = csv.DictWriter(saida, delimiter=';', lineterminator='\n', fieldnames=headers)
            if not file_exists:
                writer.writeheader()
            writer.writerow({'data_contratacao': lista[0], 'data_liquidacao': lista[1], 'taxa_abertura': lista[2],
                             'cenario_stress': lista[3], 'qtd_negocios': lista[4], 'vol_contratado_brl': lista[5],
                             'vol_contratado_usd': lista[6], 'taxa_contratada_min': lista[7],
                             'taxa_contratada_med': lista[8], 'taxa_contratada_max': lista[9]})
except:
    print('Não há dados para a data consultada.')
