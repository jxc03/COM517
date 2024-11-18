from flask import Flask, request, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# Connection to MongoDB
client = MongoClient('mongodb://localhost:27017/')
database = client['courseworkDB']
collection = database['categories']

# Upload dataset to MongoDB
@app.route('/add_users_bulk', methods=['POST'])
def add_users_bulk():
    if 'file' not in request.files:
    return jsonify({"message": "No file part"}), 400
file = request.files['file']
if file.filename == '':
return jsonify({"message": "No selected file"}), 400
if file:
users = json.load(file)
if isinstance(users, list):
db.users.insert_many(users)
return jsonify({"message": "Users added successfully"}), 201
else:
return jsonify({"message": "Invalid JSON format. Expected a list of users."}), 400

if __name__ == '__main__':
    app.run(debug=True, port=2000)