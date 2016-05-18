from app.models import Item
import urllib2
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from search.definebrowser import *
from search.general import *
from search.urlPrint import *
from search.grabHtml import *
from app.models import Item
from app import db

link = Item.query.all()


for u in Item.query.with_entities(Item.link):


    urls = (
        ('crawl', u),
    )

    keys, _ = zip(*urls)
    urls_map = dict(urls)

    def startcrawl():
        ##TODO Update database where link = title, etc
        browser = get_browser(binary=firefox_binary, proxy=proxy)
        for resource in keys:
            browser.get(urls_map.get(resource))
            #printUrls(browser)
            print (str(u))
            html = browser.page_source

            soup = BeautifulSoup(html, "html5lib")
            currentlink = str(u)
            print (currentlink + " this is the currentlink")
            currentrequest = Item.query.filter(Item.link == currentlink)
            print link.member_since
            x = currentrequest.title['a']

            db.session.add(x)
            db.session.commit()


    if __name__ == '__main__':
        startcrawl()