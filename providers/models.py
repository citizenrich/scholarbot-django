from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class SearchResults(models.Model):

    provider = models.TextField()
    keywords = models.TextField()
    title = models.TextField()
    url = models.TextField()
    doi = models.TextField()
    pubdate = models.DateTimeField()

    def __str__(self):
        return (self.provider,
                self.keywords,
                self.title,
                self.url,
                self.doi,
                self.pubdate)
