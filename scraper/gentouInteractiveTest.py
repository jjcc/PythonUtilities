from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import codecs
import json

# http://www.gentou.com.cn/person/ability/38612

webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Accept-Language'] = 'en-US,en'
webdriver.DesiredCapabilities.PHANTOMJS[
    'phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
driver = webdriver.PhantomJS(executable_path='E:/software/phantomjs-2.0.0-windows/bin/phantomjs.exe')
driver.get("http://www.gentou.com.cn/person/ability/38612")

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lossDiv")))
finally:
    print(driver.find_element_by_id("total").text)

total_txt = driver.find_element_by_id("total").text
total_no = int(total_txt.replace('/', ''))
print "page number total is %d" % total_no
# driver.close()
# firstnameField = driver.find_element_by_name("firstname")
# lastnameField = driver.find_element_by_name("lastname")
# submitButton = driver.find_element_by_id("submit")

### METHOD 1 ###
# firstnameField.send_keys("Ryan")
# lastnameField.send_keys("Mitchell")
# submitButton.click()
################

### METHOD 2 ###
# actions = ActionChains(driver).click(firstnameField).send_keys("Ryan").click(lastnameField).send_keys("Mitchell").send_keys(Keys.RETURN)
# actions.perform()
################
# print driver.page_source
driver.save_screenshot("./tmp/mypage.png")

table = driver.find_elements_by_class_name("tab08")

total_page = driver.find_element_by_id('total').text
print total_page

# f = open("record.txt","wt+",encoding="UTF-8")
f = codecs.open("record2.txt", "w", "utf-8")

for j in range(0, 4):
    current_page = driver.find_element_by_css_selector('.hover.num.on').text
    print "current page:" + current_page
    k = 0
    line = []

    stock = driver.find_elements_by_css_selector('table.tab08 td.td1')
    buy = driver.find_elements_by_css_selector('table.tab08 td.td2')
    sell = driver.find_elements_by_css_selector('table.tab08 td.td4')
    no = driver.find_elements_by_css_selector('table.tab08 td.td5')
    res = driver.find_elements_by_css_selector('table.tab08 td.td7')

    leng = len(stock)
    print "list length%d" % leng

    for i in range(0, leng):
        line = []
        print i
        s = {}
        # s['name'] = stock[i].text
        line.append(stock[i].text)
        # s['buy_price'] = buy[i].find_element_by_class_name('s14c3').text
        line.append(buy[i].find_element_by_class_name('s14c3').text)
        # s['buy_dt'] = buy[i].find_element_by_class_name('s12c3').text
        line.append(buy[i].find_element_by_class_name('s12c3').text)
        # s['sell_price'] = sell[i].find_element_by_class_name('s14c3').text
        line.append(sell[i].find_element_by_class_name('s14c3').text)
        # s['sell_dt'] = sell[i].find_element_by_class_name('s12c3').text
        line.append(sell[i].find_element_by_class_name('s12c3').text)
        # s['no'] = no[i].text
        line.append(no[i].find_element_by_class_name('s14c3').text)
        # s['res_no'] = res[i].text
        # res_txt = res[i].text.replace('\n',',')
        line.append(res[i].text)
        # stocks.append(s)
        # f.write(''.join(map(json.dumps,stocks)))
        f.write(','.join(line))
        f.write("###\n")

    next_bt = driver.find_element_by_css_selector('#next')
    # actions = ActionChains(driver).click(next_bt)
    page = "./tmp/page%d.png" % j
    driver.save_screenshot(page)
    next_bt.click()
    #driver.implicitly_wait(6)
    new_page = int(current_page)+1
    print ">>>....Waiting newpage: page%d"%new_page
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.hover.num.on'), str(new_page)))
    page = "./tmp/pageexit%d.png" % j
    driver.save_screenshot(page)

    print "saved %s" % page
    print "<<<Done Waiting"


driver.close()
f.close()
