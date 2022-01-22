from bottle import route, run, HTTPResponse
import json

@route('/')
def suggest():    
    body =json.dumps([
      {'id':1, 'title':'Vue.js', 'img':'/img/logo.png'},
      {'id':2, 'title':'React.js', 'img':'/img/logo.png'},
      {'id':3, 'title':'Angular.js', 'img':'/img/logo.png'}
      ])
    response = HTTPResponse(status=200, body=body)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, Authorization'
    return response

if __name__ == '__main__':
  run(host='0.0.0.0', port=80)