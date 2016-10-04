from django.utils.dateparse import parse_datetime

from models import SearchResults

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
            typeof = i.get('type')
            result = {
                        'type': typeof,
                        'date': date,
                        'title': title,
                        'url': url,
                        'source': 'crossref'
                    }  # fulltitle for title issue
            if self.keywords.lower() not in result.get('title').lower():
                continue
            else:
                self.results.append(result)
                commit = SearchResults(
                                        provider='crossref',
                                        keywords=self.keywords,
                                        title=title,
                                        url=url,
                                        doi=doi,
                                        pubdate=date
                        )
                commit.save()
        return self.results

# tests
# stuff = 'journal-article'
# when = '2015-01'
# test = 'cold war'
# z = CrossRef(stuff, when, test)
# print z.getcrossref()
# print z.url
