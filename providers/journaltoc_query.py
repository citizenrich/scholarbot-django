from django.utils.dateparse import parse_datetime

from doi_tools import DOITools
from models import SearchResults

import feedparser
import requests



class JournalTOC(object):
    """
    no cat, articles only, to=limit, max 300; no timeframe, just most recent
    """
    def __init__(self, keywords):
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
                date = ''
            else:
                dateall = str(i.get('date'))
                date = parse_datetime(dateall)
            result = {
                        'type': 'journal-article',
                        'date': date,
                        'title': title,
                        'url': url,
                        'source': 'journaltoc'
                    }
            if self.keywords.lower() not in result.get('title').lower():
                continue
            elif not date:
                continue
            else:
                self.results.append(result)
                doit = DOITools(url).extract_from_url()
                commit = SearchResults(
                                        provider='journaltoc',
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
# z = JournalTOC(test)
# print z.getjournaltoc()
# print z.url, z.keywords
