#!/usr/bin/env python3
import requests

base = 'https://share.osf.io/api/v2/search/creativeworks/_search'
body = {
    "query": {
        "query_string": {
            "query": "neural"
        }
    }
}

body2 = {
    "query": {
        "bool": {
            "must": {
                "query_string": {
                    "query": "putin"
                }
            },
            "filter": [
                {
                    "range": {
                        "date": {
                            "gte": "2007-01-26T00:00:00-05:00",
                            "lte": "2017-01-26T00:00:00-05:00"
                        }
                    }
                },
                {
                    "term": {
                        "types.raw": "publication",
                        "types.raw": "preprint"
                    }
                }
            ]
        }
    }
}



body3 = {
    "query": {
        "bool": {
            "must": {
                "query_string": {"query": "putin"}},
            "filter": [{
                    "range": {"date": {
                            "gte": "2007-01-26T00:00:00-05:00",
                            "lte": "2017-01-26T00:00:00-05:00"}}},
                {
                    "term": {
                        "types.raw": "publication",
                        "types.raw": "preprint"}}
]}}}



r = requests.post(url=base, json=body3)
print(r.text)


from elasticsearch_dsl import Q
q = Q("multi_match", query='python django', fields=['title', 'body'])
print(q.to_dict())
