# from twython import Twython
# import numpy as np
# from time import sleep
# import datetime
# import urllib
# from urllib.error import URLError
# from urllib.request import urlopen
import twitter

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

api = twitter.Api(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token_key,
    access_token_secret=access_token_secret
)
# twitter = Twython(
#     consumer_key,
#     consumer_secret,
#     access_token,
#     access_token_secret
# )

# def tweetout(message, id):
#     while not internet_on():
#         print("waiting for internet connection (time out 1 min)")
#         sleep(60)
#     twitter.update_status(status='#bottruths' + str(int(id)) + '\n' + message)
#     print("Tweeted: " + message)
#     id += 1
#     sav = []
#     sav.append(id)
#     np.savetxt('id_data.dat', sav)
#     del tweets[0]
#     updateQueue(tweets)

# def updateQueue(tweets):
#     f = open("./queued-posts.txt", "w+")
#     for t in tweets:
#         f.write(t+'\n')
#     f.close()

# def internet_on():
#     try:
#         print("testing connection")
#         urlopen('http://216.58.192.142', timeout=1)
#         print("connection ok")
#         return True
#     except urllib.error.URLError as err: 
#         return False

# # load id number
# id = (np.loadtxt('id_data.dat'))

# tweets = []
# # load queued tweets
# f = open('./queued-posts.txt', "r")
# if f.mode == "r":
#     lines = f.read()

# for l in lines.split('\n'):
#     tweets.append(l)
twitter_handle='@fxlmo_'

# upload tweet (be careful that not more than an hour has elapsed)
# tweetout(tweets[0],id)
# if len(tweets) < 10:
#     print("---WARNING: <10 tweets queued---")

# send a message
send_msg = api.PostDirectMessage(msg, user_id=None, screen_name=twitter_handle)
