from requests_html import HTMLSession
session = HTMLSession()

r = session.get('https://reddit.com') 

for html in r.html:
    print(html)

pass