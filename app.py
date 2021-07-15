# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/
import difflib as dl
import os
import pytest

from flask import (Flask,jsonify,json,make_response,request,render_template)
app = Flask(__name__)
class TextSimilarityResponse:   
   def __init__(self, similarity):
      self.similarity = similarity
   def to_json(self):
       return jsonify({"similarity" : self.similarity })

@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template('index.html')
def text_similarity(text1,text2):
    return (dl.SequenceMatcher(None,text1, text2).ratio() * 100)

@app.route('/text/similarity',methods=['GET'])
def text_similarity_score():
    text1 = request.args.get('text1')
    text2 = request.args.get('text2')
    if text1 == None or text2 == None:
        response = make_response(
        "No valid text1 and text2 value were found in query params",
        403,
        )
        return response;        
    
    score = text_similarity(text1, text2)
    text_similarity_score = TextSimilarityResponse(score)
    response = make_response(
        text_similarity_score.to_json(),
        200,        
    )    
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)



def test_text_similarity():
	text1="New Delhi"
	text2="Delhi"
	assert text_similarity(text1, text2) > 71.0,"test failed"