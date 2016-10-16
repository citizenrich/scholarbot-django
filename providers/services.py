from django.db import models
from django.core.exceptions import ObjectDoesNotExist


from journaltoc_query import JournalTOC
from crossref_query import CrossRef
from arxiv_query import ArXiv


class SearchOnly(object):
    """
    keyword only search (with no tasking for now)
    """
    def __init__(self, keywords):
        self.keywords = keywords

    def keyword_lookup(self):

    get_or_create


        x = []
        # if keywords exist in keyword-only table, case insensitive
        keyobj  = Keywords.objects.get(keywords__iexact=self.keywords)
        # filter out from results/keywords table, then distill into distinct results
        res_key_obj = ResultsKeywords.objects.filter(keywordid=keyobj.id).distinct(resultid)
        try: # initiate the evaluationm, get the results from the results-only table
            for i in res_key_obj:
                j = {'medium': i.medium,
                    'date': i.date,
                    'title': i.title,
                    'url': i.url,
                    'provider': i.provider}
        except ObjectDoesNotExist:
            keyobj = None






# if keywords exist
# get the id of the keywords
# then get results ids from results/keyword
# lookup the results using results ids
# return results ids
# if there are few or date is too far in past, then do a new search
#
# if keywords do not exist
# add keywords and get the keyword ids
# do search
# add results to tables
# return results ids




# ### keyword and contact search
# if keywords exist and contacts exist
# get the id of the keywords
# get the id of the contacts
#
# if keywords exist but contact does not
# get the id of the keywords
# add the contact then get the contact id
#
# if keywords do not exist and contact does
# add keywords and get the keyword ids
# do search
