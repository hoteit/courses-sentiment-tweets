# sentiment analyzer of tweets using Google Cloud AutoMl

import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from tweets.models import TwitterText
import re
import django.core.exceptions as djangoerr


def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    #for index, sentence in enumerate(annotations.sentences):
    #    sentence_sentiment = sentence.sentiment.score
    #    print('Sentence {} has a sentiment score of {}'.format(
     #       index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0


def analyze(text):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Print the results
    print_result(annotations)


def run():
    try:
        get_tweets = TwitterText.objects.all()
        for tweet in get_tweets:
            print (clean_tweet(tweet.tweet))
            analyze(tweet.tweet)
    except djangoerr.ObjectDoesNotExist:
        print ("no tweets are found")

    #analyze("this is a good day")
    #analyze("this is a bad day")

