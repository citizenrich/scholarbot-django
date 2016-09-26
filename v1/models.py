from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Contacts(models.Model):
    """
    only saves searches if consent given by user, otherwise no way to tell
    """

    uuid = models.CharField(max_length=36, unique=True, db_index=True)
    subject_pref = models.TextField()
    journal_pref = models.TextField()

    search1 = models.TextField()
    search1_date = models.DateTimeField()
    search2 = models.TextField()
    search2_date = models.DateTimeField()
    search3 = models.TextField()
    search3_date = models.DateTimeField()

    def __str__(self):
        return (self.uuid,
                self.subject_pref,
                self.journal_pref,
                self.search1,
                self.search1_date,
                self.search2,
                self.search2_date,
                self.search3,
                self.search3_date)


@python_2_unicode_compatible
class Journals(models.Model):

    name = models.TextField()
    subject = models.TextField()

    def __str__(self):
        return self.name, self.subject


@python_2_unicode_compatible
class SearchCrossRef(models.Model):

    keywords = models.TextField()
    result_url = models.TextField()
    result_doi = models.TextField()
    pubdate = models.DateTimeField()

    def __str__(self):
        return self.keywords, self.result_url, self.result_doi, self.pubdate


@python_2_unicode_compatible
class SearchJToC(models.Model):

    keywords = models.TextField()
    result_url = models.TextField()
    result_doi = models.TextField()
    pubdate = models.DateTimeField()

    def __str__(self):
        return self.keywords, self.result_url, self.result_doi, self.pubdate


@python_2_unicode_compatible
class SearchArXiv(models.Model):

    keywords = models.TextField()
    result_url = models.TextField()
    result_doi = models.TextField()
    pubdate = models.DateTimeField()

    def __str__(self):
        return self.keywords, self.result_url, self.result_doi, self.pubdate
