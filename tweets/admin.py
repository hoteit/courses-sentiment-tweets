from django.contrib import admin

from .models import SearchKeywords, TwitterText

admin.site.register(SearchKeywords)

admin.site.register(TwitterText)
