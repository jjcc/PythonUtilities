import codecs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
#from helper import get_transaction_from_page, get_total_no


webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Accept-Language'] = 'en-US,en'
webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.User-Agent'] \
    = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
ghost = webdriver.PhantomJS(executable_path='E:/software/phantomjs-2.1.1-windows/bin/phantomjs.exe')

def get_param( driver, url ):
    driver.get(url)
    total_txt = driver.find_element_by_id("total").text
    
    #try:
    return total_txt

if __name__ == '__main__':

    cid = 566921
    url_address = "https://iknow.jp/courses/%d"%cid
    total = get_param(ghost,url_address)
    # f = open("record.txt","wt+",encoding="UTF-8")
    #ofile_name = "record_%d.txt"%cid
    #ofile = codecs.open(ofile_name, "w", "utf-8")


    #for j in range(0, total):
    current_page = ghost.find_element_by_css_selector('.items').text
    print "current page:" + current_page
    k = 0
    #    get_transaction_from_page(ofile, ghost, int(current_page), total)

    ghost.close()
    #ofile.close()
