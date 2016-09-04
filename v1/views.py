import operator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from models import CrossRef, JournalTOC #arXiv not in use for now

def index(request):
    words = request.GET.getlist('words')[0]
    date = request.GET.getlist('date')[0]
    z = []
    toc = JournalTOC(words)
    toc_res = toc.getjournaltoc()
    z.extend(toc_res)
    if z <= 2:
        res = CrossRef('journal-article', date, words)
        res_res = res.getcrossref()
        z.extend(res_res)
    z.sort(key=operator.itemgetter('date'), reverse=True)
    foo = z[:10]
    length = len(foo)
    return JsonResponse({'length': length, 'results': foo})
