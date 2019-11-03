
from facebook_scraper import get_posts
import re
from textgenrnn import textgenrnn
import os.path
from os import path
from os import listdir
from os.path import isfile, join
import glob, os
import tensorflow as tf
import time
import datetime

websites = ['bristruth']
website = 'bristruth'

texts=[]
i = 0
w = 0
print("Searching for new " + website + "...")
# gather posts from bristruths
for post in get_posts('bristruths',pages=1000,credentials=('josh99@gmx.de','SpHeRiCaL4477')):
    try:
        words = post['text'].split()
        if len(words) > 0:
            x = re.search('^#Bristruth*', words[0])
            if x != None:
                filename = post['text'].splitlines()[0][1:] + ".txt"
                if not(path.exists("./posts/" + filename)):
                    f=open("./posts/"+ filename,"w+")
                    amendpost = post['text'].splitlines()[1]
                    f.write(amendpost)
                    f.close()
                    i+=1
                    texts.append(amendpost)
                    print(filename + " added!")
                # else:
                #     print(filename + " already exists")
            else:
                print("err, post cannot be read")
    except:
        print("none type caught")
print("Added " + str(i) + " new posts.")
w += 1
