
from __future__ import print_function
from datetime import datetime
import os
from bs4 import BeautifulSoup
fname =  datetime.now().strftime("%Y%m%d-%H%M%S") + ".txt"
subdir = '/home/logic/Documents/data'


def printhtml(browser):
    html = browser.page_source

    soup = BeautifulSoup(html, "html5lib")

    for tag in soup.find_all('title'):
        print(tag.text)








