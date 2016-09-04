from __future__ import unicode_literals
from django.db import models

# Create your models here.
import feedparser
import requests
import json
#import urllib

class arXiv(object):
    """
    """
    def __init__(self, keywords):
        self.keywords = keywords
        self.results = []
        self.base = 'http://export.arxiv.org/api/query?'
        self.limit = 10
        self.url = ''

    def getarxiv(self):
        query = 'all:' + self.keywords
        params = {'search_query': query, 'max_results': self.limit}
        response = requests.get(self.base, params=params)
        self.url = response.url
        rssdoc = feedparser.parse(response.content)
        for i in rssdoc.get('entries'):
            url = i.get('link')
            title = i.get('title')
            dateall = str(i.get('published'))
            date = dateall[:10]
            result = {'type': 'journal-article',
                        'date': date,
                        'title': title,
                        'url': url,
                        'source': 'arxiv'}
            if self.keywords.lower() not in result.get('title').lower():
                continue
            else:
                self.results.append(result)
        return self.results


#tests
# test = 'Neural networks'
# z = arXiv(test)
# print z.getarxiv()
# print z.url, z.keywords, z.results


class CrossRef(object):
    """
    bdmj: book, dissertation, monograph, journal-article, book-chapter, 20 queries max in one go
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
        #addurl = urllib.pathname2url(keywords) #alternative approach to building query.
        payload = {'query.title': self.keywords,
                    'filter': 'type:{bdmj},from-pub-date:{date}'.format(bdmj = self.cat, date = self.since),
                    'rows': self.limit}

        # payload = {'query.title': '\"{key}\"'.format(key = addurl),
        #             'filter': 'type:{bdmj},from-pub-date:{date}'.format(bdmj = cat, date = since),
        #             'rows': 20}

        x = requests.get(self.base, params=payload)
        self.url = x.url
        xdict = x.json()
        for i in xdict.get('message').get('items'):
            url = i.get('URL')
            title = i.get('title')[0]
            # for books, but not really needed otherwise
            # try:
            #     subtitle  = i.get('subtitle')[0]
            #     fulltitle = title + ': ' + subtitle
            # except:
            #     fulltitle = title
            dateall = str(i.get('deposited').get('date-time'))
            date = dateall[:10]
            typeof = i.get('type')
            result = {'type': typeof,
                        'date': date,
                        'title': title,
                        'url': url,
                        'source': 'crossref'} #fulltitle for title issue
            if self.keywords.lower() not in result.get('title').lower():
                continue
            else:
                self.results.append(result)
        return self.results

#tests
# stuff = 'journal-article'
# when = '2015-01'
# test = 'cold war'
# z = CrossRef(stuff, when, test)
# print z.getcrossref()
# print z.url

class JournalTOC(object):
    """
    no category - journal articles only, to= is limit, max is 300; no timeframe - just the most recent
    """
    def __init__(self,keywords):
        self.keywords = keywords
        self.results = []
        self.base = 'http://www.journaltocs.ac.uk/api/articles/'
        self.limit = 10

    def getjournaltoc(self):
        params = {'to': self.limit}
        url0 = '%s%s' % (self.base, self.keywords)
        response = requests.get(url0, params=params)
        self.url = response.url
        rssdoc = feedparser.parse(response.content)
        for i in rssdoc.get('entries'):
            url = i.get('link')
            title = i.get('title')
            if str(i.get('date')) == 'None':
                dateall = ''
            else:
                dateall = str(i.get('date'))
            date = dateall[:10]
            result = {'type': 'journal-article',
                        'date': date,
                        'title': title,
                        'url': url,
                        'source': 'journaltoc'}
            if self.keywords.lower() not in result.get('title').lower():
                continue
            else:
                self.results.append(result)
        return self.results

#tests
# test = 'Neural networks'
# z = JournalTOC(test)
# print z.getjournaltoc()
# print z.url, z.keywords
