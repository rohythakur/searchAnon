import json
import os
import time
from app.models import Item
from app import db


folderPath = '/home/logic/PycharmProjects/onionChaser/onionChaser/spiders/logs/Onions/'
searchFor = ['.ONION', '.ONION/']



def add_bot():
    print "Searching for new Files ..."
    json_files = [pos_json for pos_json in os.listdir(folderPath)]
    for js in json_files:
        if not js.endswith('.old'):
            with open(os.path.join(folderPath, js)) as json_file:

                json_text = json.load(json_file)
                for idof in json_text:
                    if idof['url'].endswith(tuple(searchFor)):
                        x = idof['url']

                        if x.endswith('/'):

                            print "adding " + x
                            links = Item(link=x)
                            db.session.add(links)
                            db.session.commit()

                        else:
                            newx= x + "/"

                            print "adding " + newx
                            links = Item(link=newx)
                            db.session.add(links)
                            db.session.commit()


            path = os.path.join(folderPath, js)
            target = os.path.join(folderPath, js + '.old')
            os.rename(path, target)





while True:
    add_bot()
    time.sleep(4)




