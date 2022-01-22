import json
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

with open('my_suggest.json') as f:
  configuration = json.load(f)

es.indices.create('my_suggest', body=configuration)

