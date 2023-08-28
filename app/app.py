from flask import Flask, Response, request
import pymongo
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

def get_db():
    client = MongoClient(host="mongo",
                         port=27017, 
                         username="admin", 
                         password="admin",
                         authSource="admin")
    db = client["main_db"]
    return db

@app.route("/hello")
def hello():
   return "How do you do fellow kids?"

@app.route("/", methods=["GET"])
def get_collection():
    db = get_db()
    collection = db.main.find({}, {"_id": False})
    response = json_util.dumps(collection)
    return Response(response, mimetype="application/json")


@app.route("/new", methods=["POST"])
def post_new():
    text = request.json["text"]
    db = get_db()
    collection = db.main.insert_one({"text": text})
    response = json_util.dumps(collection.inserted_id)
    return response


if __name__ == "__main__":  
	app.run(host="0.0.0.0", port=5000, debug=True)