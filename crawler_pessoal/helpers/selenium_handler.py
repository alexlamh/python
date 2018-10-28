from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
drv = webdriver.Chrome(executable_path='/home/lin/python/chromedriver', chrome_options=options)

def get(url):
    return drv.get(url)

def css(param):
    return drv.find_element_by_css_selector(param)

def cssList(param):
    return drv.find_elements_by_css_selector(param)

def cssClass(param,classe):
    return drv.find_element_by_css_selector(param).find_element_by_class_name(classe)

def cssClassAttr(param,classe,atributo):
    return drv.find_element_by_css_selector(param).find_element_by_class_name(classe).get_attribute(atributo)

def cssAttr(param,atributo):
    return drv.find_element_by_css_selector(param).get_attribute(atributo)

def xpath(param):
    return drv.find_element_by_xpath(param)

def xpathList(param):
    return drv.find_elements_by_xpath(param)

def quit():
    return drv.quit()