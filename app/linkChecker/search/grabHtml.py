
from datetime import datetime
from bs4 import BeautifulSoup
from app import db
from app.models import Item

import urlparse


fname =  datetime.now().strftime("%Y%m%d-%H%M%S") + ".txt"
subdir = '/home/logic/Documents/data'


def printhtml(browser, u):
    html = browser.page_source

    soup = BeautifulSoup(html, "html5lib")

    currentlink = u[0]

    x = Item.query.filter_by(link=currentlink).first()

    try:

        x.title = str(soup.title.string)

        x.description = (soup.get_text("|", strip=True))


    except Exception as e:
        print(str(e))

    db.session.commit()


