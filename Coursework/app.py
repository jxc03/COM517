from flask import Flask, request, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# Connection to MongoDB
client = MongoClient('mongodb://localhost:27017/')
database = client['courseworkDB']
collection = database['categories']

# Upload dataset to MongoDB
@app.route('/add_dataset', methods=['POST'])
def add_dataset():
    

if __name__ == '__main__':
    app.run(debug=True, port=2000)