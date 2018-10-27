import datetime as dt
import subprocess as sp
import csv
import ipgetter as ipg
import os

def log():
    with open('log.txt', 'a', newline='') as saida:
        escrever = csv.writer(saida)
        escrever.writerow([date, ip, resp])

address = "www.uol.com.br"
res = sp.call(['ping', '-c', '3', address])
date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ip = ipg.myip()

if res == 0:    
    print("ping to", address, "OK")
    print(date, ip)
    resp = 'PING OK'
    log()
elif res == 2:
    print("no response from", address)
    print(date, ip)
    resp = 'SEM INTERNET'
    log()
else:
    print("ping to", address, "failed!")
    print(date, ip)
    resp = 'PING FALHOU'
    log()