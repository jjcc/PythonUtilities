from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
import time

def get_transaction_from_page(output_file,driver,c_pg,max_pg):
    """
    parse a scrapped page and get all the transaction information into an output file

    :param output_file: output file handler
    :param driver:  initialized ghost driver
    :param c_pg:    current page
    :param max_pg:  maximum page

    :return: 1 normal return, 0 finish during sanity check,
    """
    # type: (object, object) -> object
    global element
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
        #print i
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
        res_txt = res[i].text.replace('\n', ',')
        line.append(res_txt)
        # stocks.append(s)
        # f.write(''.join(map(json.dumps,stocks)))
        output_file.write(','.join(line))
        output_file.write("###\n")
    # actions = ActionChains(driver).click(next_bt)

    page = "./tmp/page%d.png" % c_pg
    driver.save_screenshot(page)

    new_page = c_pg + 1
    if new_page > max_pg:
        print "<<<Reach max, return"
        return 0


    next_bt = driver.find_element_by_css_selector('#next')
    next_bt.click()
    # driver.implicitly_wait(6)
    print ">>>....Waiting newpage: page%d" % new_page
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.hover.num.on'), str(new_page)))
    page = "./tmp/pageexit%d.png" % c_pg
    driver.save_screenshot(page)
    print "saved %s" % page
    print "<<<Done Waiting"
    return 1


def get_total_no( driver, url ):
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lossDiv")))
    finally:
        print(driver.find_element_by_id("total").text)
    total_txt = driver.find_element_by_id("total").text
    total_no = int(total_txt.replace('/', ''))
    print "page number total(init)is %d" % total_no
    driver.save_screenshot("./tmp/mypageB4Sleep.png")
    time.sleep(3)
    driver.save_screenshot("./tmp/mypageAfterSleep.png")
    table = driver.find_elements_by_class_name("tab08")
    total_page = driver.find_element_by_id('total').text
    print total_page
    total_no = int(total_page.replace('/', ''))
    print "page number total(now) is %d" % total_no

    return total_no