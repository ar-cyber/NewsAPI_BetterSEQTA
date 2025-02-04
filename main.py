import flask
# REQUEST STRING:  const url = `https://newsapi.org/v2/everything?domains={uri}&from=${from}&apiKey=17c0da766ba347c89d094449504e3080`;
import os
import json
import requests

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return flask.jsonify({
    "error": True,
    "data": "DO NOT QUERY THIS API BY ITS ROOT URI."
  })
@app.route('/news/get/<country>/<fromstr>')
def newsget(country, fromstr):
  if type(country) != str and type(from) != str:
    return flask.jsonify({
      'error': True,
      'data': "country or from state is not str"})
  for item in os.listdir('/countries'):
    if item.replace(".txt", "") == country:
      found = True
      break
    else:
      pass
  if found == True:
    url = open(country + ".txt", "r")
    finisheduri = f"https://newsapi.org/v2/everything?domains={uri}&from={fromstr}&apiKey=17c0da766ba347c89d094449504e3080"
    data = requests.get(finisheduri).json()
    return jsonify({
      "error": False,
      "data": data
  else:
    return flask.jsonify({
      'error': True,
      'data': "Your country does not currently have a news page. Please suggest your news page in 'https://github.com/betterseqta/betterseqta-plus/issues/new'"})
    
app.run("0.0.0.0", 80)
