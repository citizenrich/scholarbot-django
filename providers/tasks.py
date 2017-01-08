#probably add database reads, writes here instead of in providers
from __future__ import absolute_import, unicode_literals #absolute_import is for celery

from django.conf import settings

from celery import shared_task

from .arxiv_query import ArXiv
from .crossref_query import CrossRef
from .journaltoc_query import JournalTOC


@shared_task(name='jtoc_only')
def jtoc_only(keywords):
    JournalTOC(keywords=keywords).getjournaltoc()

@shared_task(name='crossref_only')
def jtoc_only(keywords):
    CrossRef(keywords=keywords).getcrossref()

@shared_task(name='arxiv_only')
def arxiv_only(keywords):
    ArXiv(keywords=keywords).getarxiv()



@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)
