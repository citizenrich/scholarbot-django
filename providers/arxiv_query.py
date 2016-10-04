from django.utils.dateparse import parse_datetime

from doi_tools import DOITools
from models import SearchResults

import feedparser
import requests



class ArXiv(object):

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
            date = parse_datetime(dateall)
            result = {
                        'type': 'journal-article',
                        'date': date,
                        'title': title,
                        'url': url,
                        'source': 'arxiv'
                }
            if self.keywords.lower() not in result.get('title').lower():
                continue
            else:
                self.results.append(result)
                doit = DOITools(url).extract_from_url()
                commit = SearchResults(
                                        provider='crossref',
                                        keywords=self.keywords,
                                        title=title,
                                        url=url,
                                        doi=doit,
                                        pubdate=date
                        )
                commit.save()
        return self.results


# tests
# test = 'Neural networks'
# z = arXiv(test)
# print z.getarxiv()
# print z.url, z.keywords, z.results