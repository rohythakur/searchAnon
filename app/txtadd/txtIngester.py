import os

from app.models import Item
from app import db
from datetime import datetime

folderPath = '/home/logic/Documents/data'

timestamp = datetime.today()
def add_bot():
        print "Searching for new Files ..."
        for txt_files in os.listdir(folderPath):
            if txt_files.endswith('.txt'):
                with open(os.path.join(folderPath, txt_files)) as txt:
                    for line in enumerate(txt):
                        if '.onion' in line:
                            if 'reddit' not in line:
                                if 'xmh57' not in line:
                                    print line
                                    try:

                                        links = Item(link=line,
                                                     title='',
                                                     description='',
                                                     click_count='',
                                                     member_since=timestamp)
                                        db.session.add(links)
                                        db.session.commit()
                                        print "adding " + line

                                    except Exception as e:
                                        print str(e)
                                        db.session.rollback()
                                        db.session.flush()
                                        continue



                path = os.path.join(folderPath, txt_files)
                target = os.path.join(folderPath, txt_files + '.old')
                os.rename(path, target)
add_bot()


