from flask import Flask, request, jsonify
from flask_pymongo import MongoClient
from bson import ObjectId, errors
import sys

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/') # Have to specify the host & port
db = client.restdb
collection = db.cats

@app.route('/')
def homepage():
    return "Homepage", 200

@app.route('/info', methods=['POST'])
def post_info():
    if not request.json:
        return "Please enter in JSON", 400
    info = request.json
    id = collection.insert_one(info).inserted_id
    return jsonify(str(id)), 201

@app.route('/info/<id>', methods=['GET'])
def get_info(id):
    try:
        result = collection.find_one({'_id': ObjectId(id)})
    except errors.InvalidId:
        return "ID entered invalid", 400

    if not result:
        return "Object not found", 404

    return jsonify({'name': result['name']}), 200

@app.route('/info/<id>', methods=['DELETE'])
def delete_info(id):
    try:
        result = collection.find_one({'_id': ObjectId(id)})
    except errors.InvalidId:
        return "ID entered invalid", 400

    if not result:
        return "Object not found", 404

    collection.remove({'_id': ObjectId(id)})

    return jsonify(result['name']), 200

@app.route('/info/<id>', methods=['PUT'])
def put_info(id):
    try:
        result = collection.find_one({'_id': ObjectId(id)})
    except errors.InvalidId:
        return "ID entered invalid", 400

    if not result:
        return "Object not found", 404

    if not request.json:
        return "Please enter in JSON", 400

    info = request.json

    collection.update({'_id': ObjectId(id)}, {'$set': info})

    result = collection.find_one({'_id': ObjectId(id)})

    return jsonify(result['name']), 200

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
