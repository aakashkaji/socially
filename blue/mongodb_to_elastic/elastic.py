from elasticsearch import Elasticsearch

es =  Elasticsearch()

print("connected elastic serarch", es.info)