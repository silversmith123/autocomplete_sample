from ast import keyword
from elasticsearch import Elasticsearch
from pykakasi import kakasi
import requests
es = Elasticsearch('http://localhost:9200')

kks = kakasi()
kks.setMode("J","a") 

def _edge_ngram(word):
  return [ word[0: i+1] for i in range(len(word)) ]

def edge_ngram(word):
  keyword = ['']
  last_keyword = ['']
  for b in word:
    buff = last_keyword.copy()
    last_keyword  = []
    for gram in buff:
      keyword.extend([ gram + edge for edge in _edge_ngram(kks.convert(b)[0]['hepburn'] )])
      keyword.append(gram + b)
      last_keyword.append( gram + kks.convert(b)[0]['hepburn'])
      last_keyword.append(gram + b)
  return keyword

search_words = ['ソファ', 'PC', 'パソコン', 'デスク', 'ほんだな']
for w in search_words:
  for text in edge_ngram(w):
    req = requests.get('http://localhost/suggest', params={'text': text})
    print(text)