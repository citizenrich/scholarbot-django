from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.template import loader

import operator

from providers.crossref_query import CrossRef
from providers.journaltoc_query import JournalTOC
from providers.arxiv_query import ArXiv

def index(request):
    return render(request, 'index.html')

class Search(View):

    def get(self, request):
        words = request.GET.getlist('words')[0]
        date = request.GET.getlist('date')[0]
        try:
            z = []
            toc = JournalTOC(words)
            toc_res = toc.getjournaltoc()
            z.extend(toc_res)
        except:
            pass
        if len(z) <= 2:
            res = CrossRef('journal-article', date, words)
            res_res = res.getcrossref()
            z.extend(res_res)
        z.sort(key=operator.itemgetter('date'), reverse=True)
        foo = z[:10]
        length = len(foo)
        return JsonResponse({'length': length, 'results': foo})
