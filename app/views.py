from flask import render_template, request, redirect, g, url_for
from app import app
import os
import json
import tweepy

@app.route('/', methods=['GET', 'POST'])
def index():
    consumer_key =""
    consumer_secret =""
    access_token =""
    access_token_secret =""
        
        # authentication of consumer key and secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        
        # authentication of access token and secret
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    screen_name = "@ZachsBot2"
    tweets = api.user_timeline(screen_name=screen_name, count=10000, tweet_mode='extended')

    tweet_retweets = 0
    tweet_likes = 0
    tweet_count = 0
    for tweet in tweets:  
        tweet_retweets += tweet._json['retweet_count']
        tweet_likes += tweet._json['favorite_count']
        tweet_count += 1
    print(tweet_retweets)
    print(tweet_likes)
    print(tweet_count)

    likes_dump = json.dumps(tweet_likes)
    retweet_dump = json.dumps(tweet_retweets)
    count_dump = json.dumps(tweet_count)

    return render_template('index.html', likes=likes_dump, retweets=retweet_dump, count=count_dump)