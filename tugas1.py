
import tweepy
import datetime
from tweepy import OAuthHandler, Stream, StreamListener
from main import yangini

def inisekalimi(api):
    akun = str(input('Akunnya Siapa Bede : '))
    tweets=api.home_timeline()
    for tweet in tweets:
        print(tweet.text)
    user_tweets = api.user_timeline(screen_name=akun, count=200, tweet_mode="extended")
    for tweet in user_tweets:
        print(tweet._json)
    the_list = []
    tweet_jokowi = api.user_timeline(screen_name=akun, count=200, tweet_mode="extended")
    startDate = datetime.datetime(2019, 10, 22, 00, 00, 00)
    endDate =   datetime.datetime(2019, 10, 24, 00, 00, 00)
    for tweet in tweet_jokowi:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            the_list.append(tweet._json)
    import pandas
    myData=pandas.DataFrame(the_list)
    myData
api=yangini()    
inisekalimi(api)    