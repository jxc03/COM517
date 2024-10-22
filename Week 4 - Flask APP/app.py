from flask import Flask, request, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# Connecting to MongoDB
client = MongoClient("mongodb://localhost:27017/") # Establishes the connection to MongoDB
db = client['user_database'] # Selects the database
users_collection = db['users'] # Selects the collection

@app.route('/load_data', methods=['POST'])
def load_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}, 400)
        
        users_collection.insert_many(data)
        return jsonify({"message": "Data loaded successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    