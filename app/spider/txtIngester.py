import os

from app.models import Item
from app import db


folderPath = '/home/logic/Documents/infoCrawler'


def add_bot():
        print "Searching for new Files ..."
        for txt_files in os.listdir(folderPath):
            if txt_files.endswith('.txt'):
                with open(os.path.join(folderPath, txt_files)) as txt:
                    for line in txt:
                        if '.onion' in line:
                            if 'reddit' not in line:
                                if 'xmh57' not in line:
                                    print line
                                    try:
                                        links = Item(link=line)
                                        db.session.add(links)
                                        db.session.commit()
                                        print "adding " + line
                                        db.session.flush()
                                    except Exception as e:
                                        print str(e)
                                        db.session.rollback()
                                        db.session.flush()
                                        continue



                path = os.path.join(folderPath, txt_files)
                target = os.path.join(folderPath, txt_files + '.old')
                os.rename(path, target)
add_bot()


