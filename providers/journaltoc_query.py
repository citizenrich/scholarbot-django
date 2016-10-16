from django.utils.dateparse import parse_datetime
from django.utils import timezone

from journaltoc_query import JournalTOC
from crossref_query import CrossRef
from arxiv_query import ArXiv
from doi_tools import DOITools

import feedparser
import requests



class JournalTOC(object):

    """
    no category, only articles, to=limit, max 300; no timeframe, only recent
    """

    base = 'http://www.journaltocs.ac.uk/api/articles/'
    limit = 10

    def __init__(self, keywords):
        self.keywords = keywords
        self.results = []

    def getjournaltoc(self):
        params = {'to': limit}
        url0 = '%s%s' % (base, self.keywords)
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
        # bulk write to results only db
        bravo = Results.objects.bulk_create([Entry(provider=x['provider'],
                                                    medium=x['medium'],
                                                    date=x['date'],
                                                    title=x['title'],
                                                    url=x['url'],
                                                    doi=x['doi']) for x in results])
        bravo.save()
        # bulk write to results/keywords db e.g. bravo[0].id
        charlie = ResultsKeywords.objects.bulk_create([Entry(resultid=x.pk, keywordid=alpha.pk) for x in bravo])
        charlie.save()
        return self.results




# contacts, contacts/results, and keyword contacts will be done by services/view
# tests
# test = 'China'
# z = JournalTOC(test)
# print z.getjournaltoc()
# print z.url, z.keywords
