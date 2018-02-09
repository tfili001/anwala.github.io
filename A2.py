import tweepy
import credentials
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
consumer_key = "fAkotcp8vBt6cR3iLXLgppvIW"
consumer_secret = "pYMZVGBSUkwsnD8bw8goF22t1cFKm1AFk2xFWnL4OIGioCRvLW"
access_token = "913237521202638849-DqK1BQAH6CDHj5EINNPXbgJdmN3YdJS"
access_token_secret = "kDXDinKcG9MEX5CGLS8Hv0K0oSvAabSVmAVUlPcUjGGQS"

#https://t.co/DyxQbz33eh

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()
count = 10
class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        global count
        out = json.loads(data)
        if count <= 0:
            import sys
            sys.exit()
        else:
            try:
                for url in out["entities"]["urls"]:
                    count -= 1
                    print(count,':', "%s" % url["expanded_url"] + "\r\n\n")
            except KeyError:
                print (data.keys())



#def on_status(self, status):
#print(status.text)


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['python'])


