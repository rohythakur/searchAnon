
from __future__ import print_function
from datetime import datetime
import os

fname =  datetime.now().strftime("%Y%m%d-%H%M%S") + ".txt"
subdir = '/home/logic/Documents/data'


def printUrls(browser):

    elems = browser.find_elements_by_xpath("//a[@href]")
    with open(os.path.join(subdir, fname), 'a') as spreader:
        for elem in elems:

            print ((elem.get_attribute("href")), file=spreader, end='\n')










