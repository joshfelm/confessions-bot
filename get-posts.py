import time
import threading
import sys
import re
from facebook_scraper import get_posts
import os
from os import path

websites = ['bristruths','cardiffessions','durfess','uobbrumfess','Yorfessions','leedsfess','oxfess','camfession','sheffessions','Swanfess','Newfession','SurFess','TrUWEBristol','readingfess']
regStr = ['^#Bristruth*','^#CardiffConfession*','^#Durfess*','^#Brumfess*','^#Yorfessions*','^#LeedsFess*','^#Oxfess*','^#Camfession*','^#Sheffession*','^#Swanfess*','^#Newfess*','^#SurFess','^#TrUWE*','^#ReadingFess*']


# Print iterations progress
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1: 
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False

w = 0
for website in websites:
    i = 0
    iteration = 0
    # gather posts from website
    posts = get_posts(website,pages=50)
    print("Searching for new " + website + "...")
    with Spinner():
        for post in posts:
            if i < 3000:
                try:
                    words = post['text'].split()
                    if len(words) > 0:
                        x = re.search(regStr[w], words[0])
                        if x != None:
                            filename = post['text'].splitlines()[0][1:] + ".txt"
                            if not(path.exists("./posts/archive/" + filename) or path.exists("./posts/" + filename)):
                                f=open("./posts/"+ filename,"w+")
                                amendpost = post['text'].splitlines()[1]
                                f.write(amendpost)
                                f.close()
                                i+=1
                            #     print(filename + " already exists")
                except:
                    print("err caught")
        print("Added " + str(i) + " new posts.")
        w += 1
