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
from pprint import pprint
import time


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

            html = browser.page_source
            ##todo get query to work with the string formatting
            soup = BeautifulSoup(html, "html5lib")
            #currentlink = (str(u)[:-5][1:]) + '\n' + "'"
            currentlink = u[0]
            print (u)

            print (currentlink)

           #x = Item.query.filter_by(link=y).first()

            #x =  Item.query.filter_by(link=u'http://32rfckwuorlf4dlv.onion/client-check\n').first()
            x = Item.query.filter_by(link=currentlink).first()
            print x
            try:
                print x.id
                x.title = 'test'
            except Exception as e:
                print(str(e))

            db.session.commit()
            time.sleep(1)


    if __name__ == '__main__':
        startcrawl()