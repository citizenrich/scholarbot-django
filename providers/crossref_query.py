from django.utils.dateparse import parse_datetime

from journaltoc_query import JournalTOC
from crossref_query import CrossRef
from arxiv_query import ArXiv

import requests
import json


class CrossRef(object):
    """
    bdmj: book, dissertation, monograph, journal-article, book-chapter
    20 queries max in one go
    """
    def __init__(self, cat, since, keywords):
        self.cat = cat
        self.since = since
        self.keywords = keywords
        self.results = []
        self.base = 'http://api.crossref.org/works?'
        self.limit = 10
        self.url = ''

    def getcrossref(self):
        payload = {
                    'query.title': self.keywords,
                    'filter': 'type:{bdmj},from-pub-date:{date}'.format(bdmj=self.cat, date=self.since),
                    'rows': self.limit
                }
        x = requests.get(self.base, params=payload)
        self.url = x.url
        xdict = x.json()
        for i in xdict.get('message').get('items'):
            url = i.get('URL')
            title = i.get('title')[0]
            doi = i.get('DOI')
            dateall = str(i.get('deposited').get('date-time'))
            date = parse_datetime(dateall)
            typeof = i.get('type') # clean this up later, to match choices in models
            result = {
                        'provider': 1,
                        'medium': 1,
                        'date': date,
                        'title': title,
                        'url': url
                    }  # fulltitle for title issue
            if self.keywords.lower() not in result.get('title').lower():
                continue
            else:
                self.results.append(result)
                commit = SearchResults(keywords=self.keywords, doi=doit, **result)
                commit.save()
        return self.results

# tests
# stuff = 'journal-article'
# when = '2015-01'
# test = 'cold war'
# z = CrossRef(stuff, when, test)
# print z.getcrossref()
# print z.url
