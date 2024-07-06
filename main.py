from flask import Flask, request, render_template, jsonify, send_from_directory
from werkzeug.routing import Rule
from config import Config
import os
import lib.scrape as scrape

app = Flask(__name__)

@app.route('/stalk/tiktok', methods=['GET'])
def tiktok_stalk():
    username = request.args.get('username')
    if not username:
        return jsonify({'error': '[!] Both parameter username is required' }), 400

    response_data = scrape.tiktok_stalk(username)
    
    response = {
        "status": "success",
        "author": Config.author,
        "code": 200,
        "result": response_data
    }
    
    return jsonify(response)
    
def get_routes():
  routes = []
  for rule in app.url_map.iter_rules():
      if rule.endpoint != 'static':
          methods = [method for method in rule.methods if method not in ['HEAD', 'OPTIONS']]
          methods_str = ', '.join(methods)
          route = {
              "name": rule.endpoint,
              "method": methods_str,
              "param": rule.rule,
              "url": rule.rule
          }
          routes.append(route)
  return routes

@app.route('/')
def home():
  routes = get_routes()
  return render_template('index.html', routes=routes)

if __name__ == '__main__':
    app.run(debug=True)
