import tweepy

consumer_key = "fAkotcp8vBt6cR3iLXLgppvIW"
consumer_secret = "pYMZVGBSUkwsnD8bw8goF22t1cFKm1AFk2xFWnL4OIGioCRvLW"
access_token = "913237521202638849-DqK1BQAH6CDHj5EINNPXbgJdmN3YdJS"
access_token_secret = "kDXDinKcG9MEX5CGLS8Hv0K0oSvAabSVmAVUlPcUjGGQS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def followers(username):
    user = api.get_user(username)
    api.create_friendship(user_id=user.id, screen_name=user.screen_name)

    for user in tweepy.Cursor(api.followers, screen_name="acnwala").items():
        follower = api.get_user(user.screen_name)
        print(user.screen_name," ",follower.followers_count)

followers("acnwala")
