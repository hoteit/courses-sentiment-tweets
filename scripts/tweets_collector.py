# script to collect tweets using Tweepy

import tweepy
from tweepy import StreamListener
import courses_sentiment_tweets.local_settings as settings
import time
import json
import sys
from tweets.models import TwitterText, SearchKeywords
import pandas as pd
import django.core.exceptions as djangoerr
import schedule

auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_token_secret)
api = tweepy.API(auth)


def get_tweeter_keywords_to_search():
    try:
        search_enabled_keywords = SearchKeywords.objects.filter(enabled=True)
        keywords = pd.DataFrame(list(search_enabled_keywords.values('keyword')))
        return keywords.to_csv(header=False, line_terminator=',', index=False)
    except djangoerr.ObjectDoesNotExist:
        print("cannot find keywords to search for. Make sure to have some keywords added to the database")
        raise Exception
    except:
        print ("unexpected error:", sys.exc_info()[0])
        raise Exception


def tweet_insert(tweet):
    # take a captured tweet and insert it into the database

    try:
        atweet = TwitterText(tweet=tweet['text'], tweet_username=tweet['user']['screen_name'])
        atweet.save()
    except:
        print("Error in Django insert tweet. error message:", sys.exc_info())
    return


class TwitterListener(StreamListener):

    def __init__(self, api=None, fprefix = 'streamer'):
        super(StreamListener, self).__init__()
        self.api = api or tweepy.API()
        self.counter = 0
        self.time = time.time()
        return

    def on_data(self, data):
        self.counter += 1
        try:
            tweet = json.loads(data)  # convert twitter stream in json into Python dictionary
            if isinstance(tweet, dict):
                if tweet['user']['lang'] != 'en':  # only store english tweets
                    return
                else:
                    tweet_insert(tweet)
                    print("tweets count: %d / %d, tweet: %s " % (self.counter, settings.tweets_max_per_sample,
                                                                 tweet['text']))
        except:
            print("Error in Twitter listener. Error message:", sys.exc_info())

        if self.counter > settings.tweets_max_per_sample:
            self.counter = 0
            return False
        else:
            return

    def on_limit(self, track):
        print(">> limit")
        return

    def on_error(self, status_code):
        print(">>> error: ", str(status_code) + "\n")
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False
        return

    def on_disconnect(self, notice):
        print (">> disconnecting")
        return False

    def on_timeout(self):
        print(">>> timed out ...\n")
        return False

def run_tweeter_listening():
    try:
        time.sleep(30)
        listener = TwitterListener(api, "test")
        stream = tweepy.Stream(auth, listener)
        keywords = get_tweeter_keywords_to_search()
        print("Begin Twitter streaming for ", str(keywords).rstrip(','))
        stream.filter(track=[keywords], languages=["en"], is_async=True)
    except:
        print(sys.exc_info())

def stop_tweeter_listening():
    print("stop")

def run():

    try:#schedule.every(settings.tweets_polling_time).seconds.do(stop_tweeter_listening)
        schedule.every(settings.tweets_polling_time).seconds.do(run_tweeter_listening)

        while True:
            schedule.run_pending()
            time.sleep(1)
    except:
        print(sys.exc_info())
