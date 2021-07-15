# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/
import difflib as dl

from flask import (Flask,jsonify,json,make_response,request)
app = Flask(__name__)
class TextSimilarityResponse:   
   def __init__(self, score):
      self.score = score
   def to_json(self):
       return jsonify({"score" : self.score })

@app.route('/')
def text_similarity_score():
    text1 = request.args.get('text1')
    text2 = request.args.get('text2')
    score = dl.SequenceMatcher(None,text1, text2).ratio()    
    text_similarity_score = TextSimilarityResponse(score*100)
    response = make_response(
        text_similarity_score.to_json(),
        200,        
    )    
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    app.run()

