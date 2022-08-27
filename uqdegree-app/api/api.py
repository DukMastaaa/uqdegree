from flask import Flask, request, jsonify
from flask_cors import CORS

import json

app = Flask(__name__)  
CORS(app)

@app.route('/', methods=['POST'])
def choose_course():
    v = request.get_json()
    print(v)
    return v