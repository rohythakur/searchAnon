import os,sys
import time
import verifyTor
import scrappyIngester
import randomTor
import random


cmdredditOnion = 'cd ~ && cd PycharmProjects/onionChaser/onionChaser && scrapy crawl Onions'
cmdreddittwo = 'cd ~ && cd PycharmProjects/onionChaser/onionChaser && scrapy crawl Onions'



while True:
    try:

        #verifyTor.checkDatabase()
        #scrappyIngester.checkforjson()
        randomTor.randomLink()
        #os.system (random.choice([cmdredditOnion, cmdreddittwo]))
    except Exception:
        continue


