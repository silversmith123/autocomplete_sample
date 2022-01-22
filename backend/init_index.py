import json
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

with open('my_suggest.json') as f:
  configuration = json.load(f)

es.indices.create('my_suggest', body=configuration)

with open('sample.json') as f:
  sample = json.load(f)

for doc in sample:
  es.create('my_suggest',doc.pop('id'), doc)
