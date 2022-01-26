from elasticsearch import Elasticsearch
import requests
es = Elasticsearch('http://localhost:9200')
search_words = ['ソファ', 'PC', 'パソコン', 'デスク', 'ほんだな']
for w in search_words:
  for token in es.indices.analyze({"analyzer":"readingform_index_analyzer", "text":w}, "my_suggest")['tokens']:
    req = requests.get('http://localhost', params={'text': token['token']})
    print(req.text)