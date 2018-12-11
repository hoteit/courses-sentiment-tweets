from django.db import models


class TwitterText(models.Model):
    tweet = models.CharField('tweet', max_length=255, null=True, blank=True)
    tweet_username = models.CharField('username', max_length=30, null=True, blank=True)
    tweet_datetime = models.DateTimeField('time collected', auto_now_add=True)
    sentiment_score = models.DecimalField('sentiment score', decimal_places=2, max_digits=4, null=True, blank=True)
    sentiment_update = models.DateTimeField('sentiment updated', auto_now=True)

    def __str__(self):
        return self.tweet


class SearchKeywords(models.Model):
    keyword = models.CharField('keyword', max_length=64)
    enabled = models.BooleanField('enabled', default=False)

    def __str__(self):
        return self.keyword
