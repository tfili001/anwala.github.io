import tweepy
import requests
import json
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
consumer_key = "fAkotcp8vBt6cR3iLXLgppvIW"
consumer_secret = "pYMZVGBSUkwsnD8bw8goF22t1cFKm1AFk2xFWnL4OIGioCRvLW"
access_token = "913237521202638849-DqK1BQAH6CDHj5EINNPXbgJdmN3YdJS"
access_token_secret = "kDXDinKcG9MEX5CGLS8Hv0K0oSvAabSVmAVUlPcUjGGQS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

public_tweets = api.home_timeline()

#   TODO
#Check if links are in twitter domain
#Check if final URI is unique
file = open("input.txt","r+")
class StreamObj(tweepy.StreamListener):
    k = 0
    URIlist = []
    def on_data(self, data):
        limit = 2000
        out = json.loads(data)
        try:
            if StreamObj.k >= limit:
               return False

            else:
                for url in out["entities"]["urls"]:
                    StreamObj.k += 1
                    StreamObj.URIlist.append(url["expanded_url"])
               #     sys.os.system("clear")
                    print(StreamObj.k)
                    
        except KeyError:
            print("data keys")
            print(data.keys())   




def writeURI(strObj = StreamObj()):
    for x in strObj.URIlist:
        file.write(x+"\n")
        print(x)
        


def checkURI():
    i=0
    # file = open("input.txt","r")
    URI_refine = file.readlines()
    for x in URI_refine:
        i=i+1
        site = requests.get(x)
        #print(i," ",x)
       # print(site.url)
        print("_________________________")
        if "twitter" in site.url:
            print(i," TWITTER FOUND")
        else:
            URI_refine.append(site.url)
            print(i," site.url=",site.url)
       
'''
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
streamObj = StreamObj()
myStream = tweepy.Stream(auth = api.auth, listener=streamObj)

myStream.filter(track=['python'])
writeURI(streamObj)
'''
#file.close()

checkURI()


