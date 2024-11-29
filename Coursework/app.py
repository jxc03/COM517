'''
# "Select only neccessary fields"
- /get_appendix
- /get_mmt
# "Match values in an array"
- /get_math_tags
'''

from flask import Flask, request, jsonify
from pymongo import MongoClient
import json
from bson.json_util import dumps

app = Flask(__name__)

# Connection to MongoDB
client = MongoClient('mongodb://localhost:27017/')
database = client['coursework_db']
collection = database['categories']

# Show all categories
@app.route('/show_all', methods=['GET'])
def show_all():
    '''
    all_documents = collection.find({})
    documents_list = []
    for documents in all_documents:
        documents["_id"] = str(documents["_id"]) 
        documents_list.append(documents)
    return jsonify(documents_list), 200

    https://www.mongodb.com/docs/languages/python/pymongo-driver/current/read/retrieve/?msockid=20511825578569d936200d1856b9683a
    https://www.w3schools.com/python/python_mongodb_find.asp
    https://www.slingacademy.com/article/pymongo-how-to-convert-objectid-to-string-and-vice-versa/
    '''

    all_documents = collection.find({})
    documents = [{**document, "_id": str(document["_id"])} for document in all_documents]
    return jsonify(documents), 200
    '''
    https://geekflare.com/python-unpacking-operators/
    https://docs.python.org/3/tutorial/controlflow.html#index-4
    '''

# Show all appendix related concerns
@app.route('/all_appendix', methods=['GET'])
def all_appendix():
    appendix_documents = collection.find({"Category": "Appendix-related concerns"})
    appendix_documents_list = []
    for document in appendix_documents:
        document["_id"] = str(document["_id"])
        appendix_documents_list.append(document)
    return jsonify(appendix_documents_list), 200

# Show all method, maths and terminology
@app.route('/all_MMT', methods=['GET'])
def all_mmt():
    mmt_documents = collection.find({"Category": "Method, Mathematics and Terminology"})
    mmt_documents_list = []
    for document in mmt_documents:
        document["_id"] = str(document["_id"])
        mmt_documents_list.append(document)
    return jsonify(mmt_documents_list), 200


# Get appendix related concerns with relevant information 
@app.route('/get_appendix', methods=['GET'])
def get_appendix():
    appendix_documents = collection.find({"Category": "Method, Mathematics and Terminology"}, {"Category": 1, "Comment": 1, "Date": 1, "Severity": 1, "Priority": 1, "Suggested Action": 1}) # Selects only 
    result = [{"Category": document["Category"], "Comment": document["Comment"], "Date": document["Date"], "Severity": document["Severity"], "Priority": document["Priority"], "Suggested Action": document["Suggested Action"]} for document in appendix_documents] # Stores to a list
    return jsonify(result) # Outputs the list

# Get method, maths and terminology with relevant information 
@app.route('/get_mmt', methods=['GET'])
def get_mmt():
    appendix_documents = collection.find({"Category": "Method, Mathematics and Terminology"}, {"Category": 1, "Comment": 1, "Date": 1, "Severity": 1, "Priority": 1, "Suggested Action": 1})
    result = [{"Category": document["Category"], "Comment": document["Comment"], "Date": document["Date"], "Severity": document["Severity"], "Priority": document["Priority"], "Suggested Action": document["Suggested Action"]} for document in appendix_documents]
    return jsonify(result)

# Get all the document that has the 'tag' of 'math'    
@app.route('/get_math_tags', methods=['GET'])
def get_math_tags(): 
    tags = collection.find({"Tags": {"$in": ["math"]}})
    result = [{"Category:": document["Category"],
               "Comment": document["Comment"],
               "Date": document["Date"],
               "Type": document["Type"],
               "Severity": document["Severity"],
               "Priority": document["Priority"],
               "Suggested Action": document["Suggested Action"],
               "Status": document["Status"],
               "Tags": document["Tags"]} for document in tags] 
    return jsonify(result)
# Type is at the bottom; fix later on

# Get mmt documents that have the 'tag' of 'method' and the 'severity' of 'high'
@app.route('/get_mmt_severity_high', methods=['GET'])
def get_appendix_severity_high():
    docs = collection.find(
        {
            "Tags": {"$in": ["method"]},
            "Severity": "High"
        }, 
        {'_id': 0})
    result = list(docs)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=2000)