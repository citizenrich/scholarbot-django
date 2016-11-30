from django.utils.dateparse import parse_datetime

from doi_tools import DOITools

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
        rsslist = rssdoc.get('entries')
        # cleaning out empty dates and keywords not in title
        rsslist[:] = [x for x in rsslist if not str(x.get('date')) == 'None']
        rsslist[:] = [x for x in rsslist if self.keywords.lower() in x.get('title').lower()]
        for i in rssdoc.get('entries'):
            url = i.get('link')
            title = i.get('title')
            dateall = str(i.get('published'))
            date = parse_datetime(dateall)
            doit = i.get('id') # untested
            result = {
                        'provider': 3,
                        'medium': 1,
                        'date': date,
                        'title': title,
                        'url': url,
                        'doi': doit
                }
            self.results.append(result)
        return self.results


# test = 'Neural networks'
# z = ArXiv(test)
# print z.getarxiv()
