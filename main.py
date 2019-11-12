# -*- coding: utf-8 -*-
"""
"""

import tweepy
from tweepy import OAuthHandler, Stream, StreamListener

def yangini():
    consumer_key="58faqlkmcJqTll1ungomL9ykR"
    consumer_secret="9aHkJmErkazJO3nATnAdjFfIrJP85g9EOucVpP9B4xAMCYTO7N"
    access_token="308820901-hun4cfrSkWvuCtvdvmjZzitLCNQLVMqySrIKh4pO"
    access_token_secret="7q09rWXoMEisC5MrDmvfXpkkvdMIax5fH0PD5lBlZ3d87"
    auth=OAuthHandler(consumer_key, consumer_secret,)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api