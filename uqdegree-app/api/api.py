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

@app.route('/courses')
# should return a list of course codes i.e
# ['COSC2500', 'MATH1071', 'MATH1061', 'CSSE1001']
def queryCourses():
    print(getCourses())
    return jsonify(getCourses())

def getCourses():
    list = ['csse1001', 'math1071']
    return list