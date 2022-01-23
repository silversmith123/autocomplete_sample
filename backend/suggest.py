from genericpath import exists
from bottle import request, route, run, HTTPResponse
from elasticsearch import Elasticsearch
import json

@route('/')
def suggest():
    es = Elasticsearch('http://localhost:9200')
    query = { 
     "query": { 
       "bool": { 
         "should": [
           { 
             "match": { 
               "search_word.readingform": { 
                 "query": request.query.text,
                 "fuzziness":"AUTO",
                 "operator": "and" 
               } 
             } 
          } 
         ] 
       }
      },
      "sort": "priority" 
    }
    es_json = es.search(query, 'my_suggest')
    suggest = [{'id': v['_id'], 'text': v['_source']['suggest_word'], 'img': v['_source']['img']} for v in es_json['hits']['hits']]
    unique = []
    exists = []
    for v in suggest:
      if v['text'] not in exists:
        unique.append(v)
        exists.append(v['text'])

    response = HTTPResponse(status=200, body=json.dumps(unique))
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, Authorization'
    return response

if __name__ == '__main__':
  run(host='0.0.0.0', port=80)