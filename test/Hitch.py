from multiprocessing.connection import wait
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import time


if __name__ == '__main__':
    driver = uc.Chrome()
    driver.get('https://simple.ripley.com.pe/tecnologia/celulares/ver-todo-celulares?source=menu')
    #driver.set_page_load_timeout(20)
    time.sleep(20)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    eq = soup.select('div.catalog-container > div > a')
    
    loadMore = True
    pageCount = 1

    if len(eq)>0:
        peliculas = list()
    
        for i in eq:
            print("https://simple.ripley.com.pe/" + i['href'])
        pageCount = pageCount+1
    else:
        loadMore = False

    
