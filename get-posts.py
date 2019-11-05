import re
from facebook_scraper import get_posts
import os
from os import path

websites = ['bristruths','cardiffessions','ExeHonestly','durfess','uobbrumfess','Yorfessions','leedsfess','oxfess','camfession','sheffessions','Swanfess','Newfession','SurFess','TrUWEBristol','readingfess']
regStr = ['^#Bristruth*','^#CardiffConfession*','^#ExeHonestly*','^#Durfess*','^#Brumfess*','^#Yorfessions*','^#LeedsFess*','^#Oxfess*','^#Camfession*','^#Sheffession*','^#Swanfess*','^#Newfess*','^#SurFess','^#TrUWE*','^#ReadingFess*']

w = 0
for website in websites:
    i = 0
    print("Searching for new " + website + "...")
    # gather posts from website
    for post in get_posts(website,pages=100,credentials=('bottruths@gmail.com','bottisonuh')):
        if i < 3000:
            try:
                words = post['text'].split()
                if len(words) > 0:
                    x = re.search(regStr[w], words[0])
                    if x != None:
                        filename = post['text'].splitlines()[0][1:] + ".txt"
                        if not(path.exists("./posts/archive/" + filename)):
                            f=open("./posts/"+ filename,"w+")
                            amendpost = post['text'].splitlines()[1]
                            f.write(amendpost)
                            f.close()
                            i+=1
                            print(filename + " added!")
                        # else:
                        #     print(filename + " already exists")
                    else:
                        print("err, post cannot be read")
            except:
                print("error caught")
    print("Added " + str(i) + " new posts.")
    w += 1
