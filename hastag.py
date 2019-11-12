"""
"""
import tweepy
import csv
from tweepy import OAuthHandler, Stream, StreamListener
from main import yangini
def masaweh(api):
    hastag = str(input('Hastag apa bede Bede : '))
    csvFile = open('hastagbaru.csv', 'a')
    csvWriter = csv.writer(csvFile)
    for tweet in tweepy.Cursor(api.search,q=hastag,count=50,lang="id",since="2019-10-20", until="2019-10-27").items():
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
api=yangini() 
masaweh(api)       