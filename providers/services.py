from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from models import *

from journaltoc_query import JournalTOC
from crossref_query import CrossRef
from arxiv_query import ArXiv


class SearchOnly(object):
    """
    keyword only search (with no tasking for now)
    """
    def __init__(self, keywords):
        self.keywords = keywords
        self.results = []

    def keyword_lookup(self):
        try:
            # get objects if keywords exist in keyword-only table, case insensitive
            keyobj = Keywords.objects.get(keywords__iexact=self.keywords)
            # follow relations backwards to get from results/keywords table
            res_key_obj = keyobj.resultskeywords_set.distinct('resultid')
            for i in res_key_obj:
                result = {'medium': i.medium,
                    'date': i.date,
                    'title': i.title,
                    'url': i.url,
                    'provider': i.provider}
                self.results.append(result)
            return self.results
        except ObjectDoesNotExist:
            return self.results




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
