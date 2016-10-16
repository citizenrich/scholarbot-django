from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Results(models.Model):
    """
    """
    PROVIDER = ((1, 'CrossRef'),
                (2, 'JournalTOCs'),
                (3, 'arXiv'))

    MEDIUM = ((1, 'Article'),
                (2, 'Book'),
                (3, 'Dissertation'))

    provider = models.SmallIntegerField(choices=PROVIDER)
    medium = models.SmallIntegerField(choices=MEDIUM)
    title = models.TextField()
    date = models.DateTimeField()
    url = models.TextField()
    doi = models.TextField()

    def __str__(self):
        return (self.id,
                self.provider,
                self.medium,
                self.title,
                self.date,
                self.url,
                self.doi)


@python_2_unicode_compatible
class Keywords(models.Model):
    """
    """
    keywords = models.TextField(unique=True)
    last_search = models.DateTimeField()

    def __str__(self):
        return (self.id, self.keywords, self.last_search)


@python_2_unicode_compatible
class Contacts(models.Model):
    """
    """
    external_id = models.TextField()
    num_requests = models.IntegerField()
    last_request = models.DateTimeField()

    def __str__(self):
        return (self.id,
                self.external_id,
                self.num_requests,
                self.last_request)


@python_2_unicode_compatible
class ResultsKeywords(models.Model):
    """
    """
    resultid = models.ForeignKey(Results, on_delete=models.CASCADE)
    keywordid = models.ForeignKey(Keywords, on_delete=models.CASCADE)

    def __str__(self):
        return (self.id, self.result, self.keyword)


@python_2_unicode_compatible
class ResultsContacts(models.Model):
    """
    """
    resultid = models.ForeignKey(Results, on_delete=models.CASCADE)
    contactid = models.ForeignKey(Contacts, on_delete=models.CASCADE)

    def __str__(self):
        return (self.id, self.result, self.contact)


@python_2_unicode_compatible
class KeywordsContacts(models.Model):
    """
    """
    keywordid = models.ForeignKey(Keywords, on_delete=models.CASCADE)
    contactid = models.ForeignKey(Contacts, on_delete=models.CASCADE)

    def __str__(self):
        return (self.id, self.keywordid, self.contactid)
