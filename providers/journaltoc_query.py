from django.utils.dateparse import parse_datetime
from django.utils import timezone

from doi_tools import DOITools

import feedparser
import requests


class JournalTOC(object):

    """
    no category, only articles, to=limit, max 300; no timeframe, only recent
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
        rsslist = rssdoc.get('entries')
        # cleaning out empty dates and keywords not in title
        rsslist[:] = [x for x in rsslist if not str(x.get('date')) == 'None']
        rsslist[:] = [x for x in rsslist if self.keywords.lower() in x.get('title').lower()]
        for i in rsslist:
            url = i.get('link')
            title = i.get('title')
            identifier = i.get('identifier')
            dateall = str(i.get('date'))
            date = parse_datetime(dateall)
            doit = DOITools(url).extract_from_url()
            result = {'provider': 2,
                        'medium': 1,
                        'date': date,
                        'title': title,
                        'url': url,
                        'doi': doit
                }
            self.results.append(result)
        return self.results




# test = 'China'
# z = JournalTOC(test)
# print z.getjournaltoc()
# print z.url, z.keywords
