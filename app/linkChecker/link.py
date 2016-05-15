from app.models import Item
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from search.definebrowser import *
from search.general import *
from search.urlPrint import *


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

            #search page!!!!!!!







    if __name__ == '__main__':
        startcrawl()