import json
import os
import time
from app.models import Item
from app import db

from flask import session

folderPath = '/home/logic/PycharmProjects/onionChaser/onionChaser/logs/Onions/'
searchFor = ['.ONION', '.ONION/']


class checkforjson():
    def add_bot(self):
        print "Searching for new Files ..."
        json_files = [pos_json for pos_json in os.listdir(folderPath)]
        for js in json_files:
            if not js.endswith('.old'):
                with open(os.path.join(folderPath, js)) as json_file:
                    try:
                        json_text = json.load(json_file)
                    except Exception as e:
                        print str(e)
                        continue
                    for idof in json_text:
                        if idof['url'].endswith(tuple(searchFor)):
                            x = idof['url']

                            if x.endswith('/'):
                                ##TODO look and clean data going into dbif session.query(model).filter(some_filter).count():

                                checkwithslash = Item.query.filter_by(link=x).first()
                                if checkwithslash is None:
                                    try:
                                        links = Item(link=x)
                                        db.session.add(links)
                                        db.session.commit()
                                        print "adding " + x
                                        db.session.flush()
                                    except Exception as e:
                                        print str(e)
                                        db.session.rollback()
                                        db.session.flush()
                                        continue


                            else:
                                newx= x + "/"
                                ##TODO look and clean data going into db

                                links = Item(link=newx)
                                try:
                                    db.session.add(links)
                                    db.session.commit()
                                    print "adding " + newx
                                    db.session.flush()
                                except Exception as e:
                                    print str(e)
                                    db.session.rollback()
                                    db.session.flush()
                                    continue

                path = os.path.join(folderPath, js)
                target = os.path.join(folderPath, js + '.old')
                os.rename(path, target)






