from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


base = 'https://share.osf.io/api/v2/search/creativeworks/_search'
s = Search(using=Elasticsearch(base))
response = s.execute()
