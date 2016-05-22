
from __future__ import print_function
from datetime import datetime
import os
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker

from app.models import Item
from app import db


fname =  datetime.now().strftime("%Y%m%d-%H%M%S") + ".txt"
subdir = '/home/logic/Documents/data'


def printhtml(browser, u, link):
    html = browser.page_source

    soup = BeautifulSoup(html, "html5lib")
    currentlink = str(u)


    print (currentlink + " this is the currentlink")
    for tag in soup.find_all('title'):
        x = (tag.text)
        #print (x)

        currentrequest = db.session.query(Item).get(currentlink).update({"title": "hello"})
        currentrequest.title = 'hello'
        db.session.commit()





