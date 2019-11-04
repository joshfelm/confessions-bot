import glob, os
import re
from os import path

for file in glob.glob("./gentext/gentext*.txt"):
    temp = str(file).split('/')
    filename = temp[len(temp) - 1]
    if not path.exists('./gentext/fixed_' + filename + '.txt'):
        f=open(file,"r")

        lines = []
        punctuation = ['.',')',',','!','?',':']
        capitals = ['.', '?', '!']
        post = ['(','"','\'', '*']
        both= ['-','/','\\']

        if f.mode == 'r':
            fl = f.readlines()
            for l in fl:
                words = l.split()
                i = 0
                l = l[0].upper() + l[1:]
                for c in l:
                    if c == 'i':
                        if l[i-1] == ' ' and l[i+1] == ' ':
                            l = l[:i] + 'I' + l[i+1:]
                    for p in punctuation:
                        if p == c:
                            l = l[:i-1] + l[i:]
                            i-=1
                    for p in post:
                        if p == c:
                            l = l[:i+1] + l[i+2:]
                            i-=1
                    for b in both:
                        if b == c:
                            l = l[:i-1] + l[i:]
                            l = l[:i] + l[i+1:]
                    for k in capitals:
                        if k == c:
                            if (i < (len(l) - 2)):
                                if l[i+2].isalpha():
                                    l = l[:i+2] + l[i+2].upper() + l[i+3:]
                    i += 1
                lines.append(l)
        f.close()
        f=open("./gentext/fixed_" + filename + ".txt","w+")
        print("From file " + filename)
        print("Choose posts to add to queue with y (default is n)")
        print("Type c to process another time")
        quit = False
        queue=open("./twitter-api/queued-posts.txt","a+")
        for l in lines:
            f.write(l)
            if not quit:
                print(l)
                response = str(input())
                response.lower()
                if response == 'y':
                    queue.write(l)
                if response == 'c':
                    quit = True
        f.close()
        queue.close()
