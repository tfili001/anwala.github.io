import tweepy
import credentials

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
consumer_key = "fAkotcp8vBt6cR3iLXLgppvIW"
consumer_secret = "pYMZVGBSUkwsnD8bw8goF22t1cFKm1AFk2xFWnL4OIGioCRvLW"
access_token = "913237521202638849-DqK1BQAH6CDHj5EINNPXbgJdmN3YdJS"
access_token_secret = "kDXDinKcG9MEX5CGLS8Hv0K0oSvAabSVmAVUlPcUjGGQS"



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()

class listener(StreamListener):
    self.counter = 0
    self.limit   = 100
    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])

