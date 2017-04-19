'''
For scraping Hi-Res celebrities photos
'''


from bs4 import BeautifulSoup
import urllib2
root_url = "https://www.theplace2.ru"

photo_url = root_url + "/photos"


opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')]




def process_individual(name, href):
    """Process individual node
    """
    individual_page = root_url + href
    if name == "Jessica Alba":
        print "Fetching Jessica"
        node_page = opener.open(individual_page).read()

        soup = BeautifulSoup(node_page,"lxml")

        pics = soup.find_all("div", class_="pic_box") # badge, listalka
        # pics[0].findChild("img") => <img alt="Jessica Alba pics" class="pic" src="/archive/jessica_alba/img/kinopoisk_ru-Jessica-Alba-5130_s.jpg"/>
        # pics[0].findChild("img")['src'] => '/archive/jessica_alba/img/kinopoisk_ru-Jessica-Alba-5130_s.jpg'
        # pics[0].findChild("a")['href'] => '/archive/jessica_alba/img/kinopoisk_ru-Jessica-Alba-5130.jpg'

        imglink_list = [ i.findChild("a")['href'] for i in pics]
        simglink_list = [i.findChild("img")['src'] for i in pics]


        badges = soup.find_all("span", class_="badge") #badge, listalka
        total_pics = badges[0].text # total pictures,u'6013'

        pages = soup.find_all("div", class_="listalka")
        total_pages = pages[0].find_all("a")[-1].text #total pages u'216'

        pass

    print "name %s, href %s" % (name, href)

    pass



def process_toplist(top_list):
    '''Process the top list'''
    for item in top_list:
        if item.findChild(attrs={"class": "name"}) != None:
            href = item.findChild(attrs={"class": "model_box"}).attrs['href']
            person_name = item.findChild(attrs={"class": "name"}).text
            process_individual(person_name, href)

        pass


if __name__=="__main__":

    photo_page = opener.open(photo_url).read()
    soup = BeautifulSoup(photo_page,"lxml")

    top_list = soup.find_all("div", class_="col-md-4")
    process_toplist(top_list)



