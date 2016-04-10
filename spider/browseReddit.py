import time
import os
import json
from datetime import datetime
import sys, os
import argparse
from os.path import basename


folderPath = '/home/logic/PycharmProjects/onionChaser/logs/Onions/'
searchFor = ['.ONION', '.ONION/']
def run_bot():

        json_files = [pos_json for pos_json in os.listdir(folderPath) if pos_json.endswith('.json')]
        #print json_files  # for me this prints ['foo.json']

        for js in json_files:
            if not js.endswith('.old'):
                with open(os.path.join(folderPath, js)) as json_file:
                    json_text = json.load(json_file)
                    for idof in json_text:
                        if idof['url'].endswith(tuple(searchFor)):
                            x = idof['url']
                            yield x
                    #print json.dumps(json_text, indent=4)


















                    #path = os.path.join(folderPath, js)
                    #target = os.path.join(folderPath, js + '.old')
                    #os.rename(path, target)
                    #print x


