import codecs
import time
from selenium import webdriver
from helper import get_transaction_from_page, get_total_no
from selenium.webdriver.firefox.options import Options


webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Accept-Language'] = 'en-US,en'
webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.User-Agent'] \
    = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
#ghost = webdriver.PhantomJS(executable_path='E:/Software/phantomjs-2.1.1-windows/bin/phantomjs.exe')

options = Options()
options.add_argument("--headless")
ghost = webdriver.Firefox(firefox_options=options, executable_path="E:\\Software\\geckodriver0_23\\geckodriver.exe")


#Chrome
#E:\Software\chromedriver_win32
ghost = webdriver.Chrome('E:\\Software\\chromedriver_win32\\chromedriver.exe')

if __name__ == '__main__':

#treeContainer > ul:nth-child(2) > li:nth-child(5) > div
#ocument.querySelectorAll('[text="证监会行业"]')

#Array.from(document.querySelectorAll('a'))
#  .find(el => el.textContent === '证监会行业')

    base_url = "http://vip.stock.finance.sina.com.cn/mkt/"
    ghost.get(base_url)
    time.sleep(5)
    #nodeGroups = ghost.find_elements_by_css_selector('##treeContainer.navtree>ul>li')
    lv_1 = ghost.find_elements_by_css_selector('#treeContainer.navtree>ul>li>div.lv_1>dl>dd') 




    ghost.close()
    ofile.close()
