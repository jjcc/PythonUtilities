from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import urllib.request
import datetime
import time

from  template_process import generate_output , mod_dict, generate_mustache_map

chrome_path = r"E:\Software\ChromeDriver\chromedriver.exe"
#target_url =
#stock1 = "http://www.investertech.com/tkchart/tkchart.asp?logo=&home=/default.asp&banner=&stkname=MSFT+INTC+DELL+CSCO+JDSU+ORCL+AMAT+GOOG+IBM+BRCM+AAPL+SYMC"


#define driver
browser = webdriver.Chrome(chrome_path)
#launch browser
#browser.get("http://ottawa.craigslist.ca")




def get_image_by_url( browser, stock,dir = ""):
    '''
    get images from a url in investertech.com
    :param browser:
    :param stock:
    :return:
    '''
    browser.get(stock)
    # wait up to 10 seconds for page to load
    timeout = 10
    datestring = datetime.date.today().strftime("%Y%m%d")
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/table[4]/tbody/tr/td[1]/table/tbody/tr[1]/td[3]/img")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    images = browser.find_elements_by_tag_name('img')
    count = 0
    chart_seg = r'chart'
    stock_list = []
    for img in images:
        imgn = img.get_attribute("src")
        if  not re.search(chart_seg,imgn):
           continue
        stock_symbolname = img.find_elements_by_xpath("parent::*")[0].text
        m = re.match(r"\(([\w|\$]+)\)", stock_symbolname)
        stock_symbol = ""
        if (m):
            stock_symbol = m.group(1)
            if stock_symbol.find('$') != -1:
                stock_symbol = stock_symbol.replace("$","x")

        print("match" + imgn + ", name:" + stock_symbolname + ",symbol:" + stock_symbol )
        count += 1
        image_name= stock_symbol + datestring + ".gif"
        image_name = dir + image_name
        with urllib.request.urlopen(imgn) as url:
            with open(image_name , 'wb') as f:
                f.write(url.read())
        stock_list.append(stock_symbolname)
    return stock_list


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
    t0 = time.time()
    #prepare directory
    import pathlib
    datestring = datetime.date.today().strftime("%Y%m%d")
    pathlib.Path('data/' + datestring).mkdir(parents=True, exist_ok=True)
    target_dir = 'data/' + datestring + '/'

    import json
    ##Generate a json file of map list for links/text
    # browser.get("http://www.investertech.com/")
    # aa = browser.find_element_by_css_selector("[color='#ff0000']")
    # bb = aa.find_elements_by_xpath(".//a")
    # links = []
    # for i in bb:
    #     print("URL#" + i.get_attribute("href") + ",Title#" + i.text)
    #     link = { "title":i.text, "url":i.get_attribute("href")}
    #     links.append(link)
    #
    # import json
    # with open('data/links.json',"w") as fout:
    #     json.dump(links, fout)

    ##load json into a list
    with open('data/links.json',"r") as fin:
        links = json.load( fin)

    #less loops
    mycount = 0
    for l in links:
        print("title:" + l["title"] + ",url:" + l["url"])
        # if mycount > 4:
        #     break
        # if mycount < 2:
        #     mycount +=1
        #     continue
        stock1 = l["url"]
        list = get_image_by_url(browser,stock1, target_dir)
        bag = {}
        [generate_mustache_map(x, i,bag) for i,x in enumerate(list)]
        bag2 = mod_dict(bag,datestring+"/")
        l["bag"] = bag2
        mycount +=1
        #if mycount > 6:
        #    break
    browser.quit()

    generate_output("data/templateall.html","data/outputall.html",links,"links")
    # bag2 = mod_dict(bag,"20180218/")

    t1 = time.time()
    total = t1 - t0
    print("duration:" + str(total) )