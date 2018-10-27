import helpers.selenium_handler as hp


hp.get('https://lista.mercadolivre.com.br/macbook')
try:
    for i in range(1,999):
        try:
            for i in range(1,999):
                x = '#searchResults > li:nth-child({})'.format(i)
                print(hp.selectorClass(x,'main-title'))
                print(hp.selectorClass(x,'item__price'))
                print('---------')
        except:
            pass
        next = '#results-section > div.pagination__container > ul > li.andes-pagination__button.andes-pagination__button--next > a'
        hp.selector().click()
except:
    pass