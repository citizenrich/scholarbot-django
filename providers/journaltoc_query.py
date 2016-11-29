from django.utils.dateparse import parse_datetime
from django.utils import timezone

from models import *
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
        # write to keywords only db
        alpha = Keywords(keywords=self.keywords, last_search=timezone.now())
        alpha.save()
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
                        'doi': doit                    }
            self.results.append(result)
            bravo = Results(provider=2, medium=1, date=date, title=title, url=url, doi=doit)
            bravo.save()
            charlie = ResultsKeywords(resultid=bravo, keywordid=alpha)
        # bulk write to results only db is not working.
        # bravo = Results.objects.bulk_create([Results(provider=x['provider'], medium=x['medium'], date=x['date'], title=x['title'], url=x['url'], doi=x['doi']) for x in self.results])
        # bulk write to results/keywords db e.g. bravo[0].id is not working
        # charlie = ResultsKeywords.objects.bulk_create([ResultsKeywords(resultid=x.pk, keywordid=alpha.pk) for x in bravo])
        return self.results




# contacts, contacts/results, and keyword contacts will be done by services/view
# tests
# test = 'China'
# z = JournalTOC(test)
# print z.getjournaltoc()
# print z.url, z.keywords
