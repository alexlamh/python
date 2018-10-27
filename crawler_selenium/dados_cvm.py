import selenium
from selenium import webdriver
import os
import zipfile

driver = webdriver.Chrome("/home/lin/python/helpers/chromedriver")

driver.get("http://dados.gov.br/dataset?_organization_limit=0&organization=comissao-de-valores-mobiliarios-cvm")

links = driver.find_elements_by_xpath('//*[@id="content"]/div[3]/div/section[1]/div/ul/li/div/h3/a')
linkspagina = len(links)

for i in range(1,linkspagina+1):
    driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/section[1]/div/ul/li['+str(i)+']/div/h3/a').click()

    nome = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/article/div/h1').text
    nome = nome.replace(":","")

    newpath = "/home/data/Documents/dadosCvm/"+nome
    if not os.path.exists(newpath):
        os.makedirs(newpath)


    link2 = driver.find_elements_by_xpath('//*[@id="dataset-resources"]/ul/li')
    linkspagina2 = len(link2)
    print(linkspagina2)
    for i in range(1,linkspagina2+1):

        driver.find_element_by_xpath('//*[@id="dataset-resources"]/ul/li['+str(i)+']/a').click()
        try:
            link = driver.find_element_by_xpath('//*[@id="content"]/div[3]/section/div[1]/div[1]/ul/li/a').get_attribute("href")
        except:
            pass

        with open("/home/data/Documents/dadosCvm/"+nome+"/"+nome+".txt", "a") as text_file:
            text_file.write(link+"\n")
        driver.back()


    os.system('wget -i "/home/data/Documents/dadosCvm/{}/{}.txt" -P "/home/data/Documents/dadosCvm/{}//{}"'.format(nome,nome,nome,nome))

    dir = '/home/data/Documents/dadosCvm/{}/{}'.format(nome,nome)
    os.chdir(dir)
    for item in os.listdir(dir):
        if item.endswith('.zip'):
            file_name = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(file_name)
            zip_ref.extractall(dir)
            zip_ref.close()


    driver.back()







