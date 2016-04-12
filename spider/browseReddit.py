import json
import os
import time
from app.models import Item
from app import db

folderPath = '/home/logic/PycharmProjects/onionChaser/onionChaser/spiders/logs/Onions/'
searchFor = ['.ONION', '.ONION/']
print "RUN"

def add_bot():

    json_files = [pos_json for pos_json in os.listdir(folderPath)]
    for js in json_files:
        if js.endswith('.old'):
            print "No data"
            continue
        else:

            with open(os.path.join(folderPath, js)) as json_file:

                json_text = json.load(json_file)
                for idof in json_text:
                    if idof['url'].endswith(tuple(searchFor)):
                        x = idof['url']
                        #print x
                        #checkDouble = Item.query.filter(Item.link).first()
                        #print checkDouble
                        ##TODO FIX QUERY SEE IF EXISTS
                        if Item.query(Item.id).filter(Item.link==Item.link).count() > 0:

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
                        else:
                            print x +"  already entered"


                        #path = os.path.join(folderPath, js)
                        #target = os.path.join(folderPath, js + '.old')
                        #os.rename(path, target)





while True:
    add_bot()
    time.sleep(4)




