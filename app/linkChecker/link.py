from app.models import Item
import urllib2
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from search.definebrowser import *
from search.general import *
from search.urlPrint import *
from search.grabHtml import *

link = Item.query.all()


for u in Item.query.with_entities(Item.link):


    urls = (
        ('crawl', u),
    )

    keys, _ = zip(*urls)
    urls_map = dict(urls)

    def startcrawl():
        browser = get_browser(binary=firefox_binary, proxy=proxy)
        for resource in keys:
            browser.get(urls_map.get(resource))
            printUrls(browser)

            printhtml(browser)


    if __name__ == '__main__':
        startcrawl()