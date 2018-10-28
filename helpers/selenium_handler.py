import selenium
from selenium import webdriver

drv = webdriver.Chrome('/home/lin/python/chromedriver')
# drv = webdriver.PhantomJS('D:\Dropbox\python\helpers\phantomjs.exe')

def get(url):
    drv.get(url)

def css(param):
    drv.find_element_by_css_selector(param)

def cssList(param):
    drv.find_elements_by_css_selector(param)

def cssClass(param,classe):
    drv.find_element_by_css_selector(param).find_element_by_class_name(classe)

def cssClassAttr(param,classe,atributo):
    drv.find_element_by_css_selector(param).find_element_by_class_name(classe).get_attribute(atributo)

def cssAttr(param,atributo):
    drv.find_element_by_css_selector(param).get_attribute(atributo)

def xpath(param):
    drv.find_element_by_xpath(param)

def xpathList(param):
    drv.find_elements_by_xpath(param)
