import helpers.selenium_handler as hp

MOBO='https://www.kabum.com.br/hardware/placas-mae?ordem=3&limite=30&pagina=1'
PROC='https://www.kabum.com.br/hardware/processadores?ordem=3&limite=30&pagina=1'
MEM='https://www.kabum.com.br/hardware/memoria-ram?ordem=3&limite=30&pagina=1'

disponibilidade='https://static.kabum.com.br/conteudo/temas/001/imagens/icones/comprar.png'

def replace_valor(var):
    return var.replace('R$ ','')

def replace_12x(var):
    return var.replace('EM ','').replace('\nOU','')

if __name__ == "__main__":
    #--- CHOOSE YOUR URL ----
    hp.get(PROC)

    try:
        for pages in range(1,999):
            try:
                i = 0
                while i < 999:
                    i+=1
                    item = '#BlocoConteudo > div:nth-child(2) > div > div:nth-child({})'.format(str(5 + i))
                    disp = '#BlocoConteudo > div:nth-child(2) > div > div:nth-child({}) > div.listagem-bots > div > a > img'.format(str(5 + i))
                    if hp.cssAttr(disp,'src') == disponibilidade:
                        prod = hp.cssClass(item,'H-titulo').text
                        preco = hp.cssClass(item,'listagem-precoavista').text
                        preco12x = hp.cssClass(item, 'listagem-preco12x').text
                        avista = hp.cssClass(item,'listagem-preco').text
                        print(prod)
                        print(preco)
                        print(replace_12x(preco12x))
                        print(avista)
                        print('--------------------------------------------------')
            except:
                pass
            hp.xpath('//*[@id="BlocoConteudo"]/div[2]/div/div[2]/form/table/tbody/tr/td[7]/a[1]').click()
    except:
        pass

