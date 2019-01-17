import codecs
from selenium import webdriver
from helper import get_transaction_from_page, get_total_no


webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Accept-Language'] = 'en-US,en'
webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.User-Agent'] \
    = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
ghost = webdriver.PhantomJS(executable_path='E:/Software/PhantomJs/phantomjs-2.1.1-windows/bin/phantomjs.exe')


#Chrome
#E:\Software\chromedriver_win32
#ghost = webdriver.Chrome('E:\\Software\\chromedriver_win32\\chromedriver.exe')


if __name__ == '__main__':

    cid = 191809#205691#38612
    url_address = "http://www.gentou.com.cn/person/ability/%d"%cid
    total = get_total_no(ghost,url_address)
    # f = open("record.txt","wt+",encoding="UTF-8")
    ofile_name = "record_%d.txt"%cid
    ofile = codecs.open(ofile_name, "w", "utf-8")

    for j in range(0, total):
        current_page = ghost.find_element_by_css_selector('.hover.num.on').text
        print ("current page:" + current_page)
        k = 0
        get_transaction_from_page(ofile, ghost, int(current_page), total)

    ghost.close()
    ofile.close()
