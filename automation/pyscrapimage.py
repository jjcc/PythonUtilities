from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import urllib.request

chrome_path = r"E:\Software\ChromeDriver\chromedriver.exe"
#target_url =
stock1 = "http://www.investertech.com/tkchart/tkchart.asp?logo=&home=/default.asp&banner=&stkname=MSFT+INTC+DELL+CSCO+JDSU+ORCL+AMAT+GOOG+IBM+BRCM+AAPL+SYMC"


#define driver
browser = webdriver.Chrome(chrome_path)
#launch browser
#browser.get("http://ottawa.craigslist.ca")




def get_image_by_url( browser, stock):
    '''
    get images from a url in investertech.com
    :param browser:
    :param stock:
    :return:
    '''
    browser.get(stock)
    # wait up to 10 seconds for page to load
    timeout = 10
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/table[4]/tbody/tr/td[1]/table/tbody/tr[3]/td[3]/img")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    images = browser.find_elements_by_tag_name('img')
    count = 0
    chart_seg = r'chart'
    for img in images:
        imgn = img.get_attribute("src")
        if  not re.search(chart_seg,imgn):
           continue
        print("match" + imgn)
        count += 1
    #    with urllib.request.urlopen(imgn) as url:
    #        with open("data/temp%d.gif"%count , 'wb') as f:
    #            f.write(url.read())

    browser.quit()


# get all of the titles for the financial values
#titles_element = browser.find_elements_by_xpath("//td[@class='C(black)']")
#titles = [x.text for x in titles_element]
#'''
#WRITTEN AS A NORMAL FOR LOOP:
#titles = []
#for x in titles_element:
#    titles.append(x.text)
#'''
#print('titles:')
#print(titles)
#
#
## get all of the financial values themselves
#values_element = browser.find_elements_by_xpath("//td[@class='Ta(end) Fw(b)']")
#values = [x.text for x in values_element]  # same concept as for-loop/list-comprehension above
#print('values:')
#print(values, '\n')
#

# pair each title with its corresponding value using zip function and print each pair
#for title, value in zip(titles, values):
#    print(title + ': ' + value)
if __name__ == "__main__":
    get_image_by_url(browser,stock1)
