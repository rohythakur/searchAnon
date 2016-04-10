import json
import os
import time


folderPath = '/home/logic/PycharmProjects/onionChaser/onionChaser/spiders/logs/Onions/'
searchFor = ['.ONION', '.ONION/']
print searchFor
print folderPath

def run_bot():

    json_files = [pos_json for pos_json in os.listdir(folderPath)]


    for js in json_files:
        if js.endswith('.old'):
            print "No data"
            continue

        else:
            try:
                with open(os.path.join(folderPath, js)) as json_file:

                    json_text = json.load(json_file)
                    for idof in json_text:
                        if idof['url'].endswith(tuple(searchFor)):
                            x = idof['url']
                            print x
                            #yield x
                            try:
                                path = os.path.join(folderPath, js)
                                target = os.path.join(folderPath, js + '.old')
                                os.rename(path, target)
                            except OSError:
                                pass
            except ValueError:
                time.sleep(10)
                run_bot()
while True:
    run_bot()
    time.sleep(3000)


