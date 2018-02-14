from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import urllib.request

chrome_path = r"E:\Software\ChromeDriver\chromedriver.exe"
#target_url =
stock1 = "http://www.investertech.com/tkchart/tkchart.asp?logo=&home=/default.asp&banner=&stkname=MSFT+INTC+DELL+CSCO+JDSU+ORCL+AMAT+GOOG+IBM+BRCM+AAPL+SYMC"

image1 = "body>table:nth-child(6)>tbody>tr>td:nth-child(1)>table>tbody >tr:nth-child(1)>td:nth-child(1)>img"
image2 = "body>table:nth-child(6)>tbody>tr>td:nth-child(1)>table>tbody >tr:nth-child(1)>td:nth-child(2)>img"
image3 = "body>table:nth-child(6)>tbody>tr>td:nth-child(1)>table>tbody >tr:nth-child(1)>td:nth-child(3) > img"
#define driver
browser = webdriver.Chrome(chrome_path)
#launch browser
#browser.get("http://ottawa.craigslist.ca")

browser.get(stock1)
# wait up to 10 seconds for page to load
timeout = 10
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/table[4]/tbody/tr/td[1]/table/tbody/tr[3]/td[3]/img")))
except TimeoutException:
    print("Timed out waiting for page to load")
images = browser.find_elements_by_tag_name('img')
count = 0
for img in images:
    imgn = img.get_attribute("src")
    print("image:" + imgn)
    count += 1
    with urllib.request.urlopen(imgn) as url:
        with open("data/temp%d.gif"%count , 'wb') as f:
            f.write(url.read())

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

