
import tweepy
from main import yangini
def yatawwa(api):
    hashtags = []
    jumlah=5    
    for i in range(jumlah):
       b = str(input('Hastag apa bede Bede : ')) 
       hashtags.append(b)
    for hashtag in hashtags:
        for tweet in tweepy.Cursor(api.search,q=hashtag, count=200, lang="id", since="2019-10-23", until="2019-10-24").items():
            print (tweet.created_at, tweet.text)
api=yangini()
yatawwa(api)