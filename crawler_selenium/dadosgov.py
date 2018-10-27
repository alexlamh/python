import csv
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('/home/lin/python/helpers/chromedriver')

driver.get('http://dados.gov.br/dataset?_organization_limit=0')

URL = []

for org in range(1,2):
    j = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/aside/div/div/section[1]/nav/ul/li[{}]/a'.format(org)).get_attribute('href')
    URL.append(j)

for z in URL:
    print('----------------------------------------')
    print('{} URL: {}'.format(org,z))
    driver.get(z)
    tituloPag = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/section[1]/div/form/p/span[2]').text)
    print('Organização: {}'.format(tituloPag))

    with open('./downloads/saida.csv', 'a', newline='') as saida:
        escrever = csv.writer(saida, delimiter=';')
        escrever.writerow(["Titulo", "Descricao", "Nome do arquivo", "Link Download", "Formato", z])

    paginas = driver.find_elements_by_xpath('/html/body/div[3]/div/div[3]/div/section[1]/div[2]/ul/li')

    pag = []
    count = 0

    for i in paginas:
        pag.append(i.text)
        count += 1

    print(pag)

    if len(pag) == 6:
        pg = int(pag[4])
    elif len(pag) == 5:
        pg = int(pag[3])
    elif len(pag) == 4:
        pg = int(pag[2])
    elif len(pag) == 3:
        pg = int(pag[1])
    else:
        pg = 1

    print('----- Possuí {} páginas -----'.format(pg))
    pg+=1

    #Setar quantas vezes deve rodar por página
    for i in range(1,pg):
        driver.get(z+'&page={}'.format(i))

        #Pegar a quantidade de linhas da página
        linhas = driver.find_elements_by_xpath('/html/body/div[3]/div/div[3]/div/section[1]/div[1]/ul/li/div/h3/a')
        linhas=len(linhas)
        print('----- {}ª Página contém {} items-----'.format(i, linhas))
        linhas+=1

        #Rodar a quantidade de linhas da página
        for x in range(1,linhas):

            print('- Item {} -'.format(x))
            url2 = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/section[1]/div[1]/ul/li[{}]/div/h3/a'.format(x)).get_attribute('href'))
            driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/section[1]/div[1]/ul/li[{}]/div/h3/a'.format(x)).click()

            count = len(driver.find_elements_by_class_name("resource-url-analytics"))
            count+=1

            #Pegar nome do arquivo, url e formato
            for y in range(1, count):

                titulo = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/article/div/h1').text)
                titulo.replace("/","-")

                #Caso não tenha nome do arquivo, url ou formato
                try:
                    desc = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/article/div/div[1]/p[1]').text)
                except NoSuchElementException:
                    try:
                        desc = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/article/div/div[1]/p').text)
                    except NoSuchElementException:
                        desc = "Sem descrição"

                try:
                    name = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/article/div/section[1]/ul/li[{}]/a'.format(y)).get_attribute('title'))
                    url = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/article/div/section[1]/ul/li[{}]/div/ul/li[2]/a'.format(y)).get_attribute('href'))
                    format = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/article/div/section[1]/ul/li[{}]/a/span'.format(y)).get_attribute('data-format'))
                except NoSuchElementException:
                    try:
                        name = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/article/div/section[2]/ul/li[{}]/a'.format(y)).get_attribute('title'))
                        url = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/article/div/section[2]/ul/li[{}]/div/ul/li[2]/a'.format(y)).get_attribute('href'))
                        format = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/article/div/section[2]/ul/li[{}]/a/span'.format(y)).get_attribute('data-format'))
                    except NoSuchElementException:
                        name = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/article/div/section[2]/ul/li/a').get_attribute('title'))
                        url = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/article/div/section[2]/ul/li/div/ul/li[2]/a').get_attribute('href'))
                        format = str(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/article/div/section[2]/ul/li/a/span').get_attribute('data-format'))

                print('--------------------------')
                print(url2)
                print('Título: {}'.format(titulo))
                print(desc)
                print(name)
                print(url)
                print(format)
                with open('./downloads/saida.csv', 'a', newline='') as saida:
                    escrever = csv.writer(saida, delimiter=';')
                    escrever.writerow([titulo, desc, name, url, format, url2])

            driver.back()

    os.rename('./downloads/saida.csv', './downloads/{}.csv'.format(tituloPag))