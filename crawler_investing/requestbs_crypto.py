import requests
from bs4 import BeautifulSoup as bs

URL = 'https://m.investing.com/crypto'
HEADER = {'User-Agent':'Mozilla/5.0'}

r = requests.get(URL, headers=HEADER).text

s = bs(r)
c = 1
s = bs(str(s.find_all('tbody')[0]))
tr = s.find_all('tr')
a = bs(str(tr)).find_all('a')
vl = bs(str(tr)).select('td[class*=pid]')

for i in tr:
    print(i)

for i in range(0,25):
    print(c)
    print(a[i].text.strip())
    print(vl[i].text.replace(',',''))
    print('---')
    c+=1


