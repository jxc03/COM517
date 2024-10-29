from flask import Flask, jsonify, request
from pymongo import MongoClient
import json
'''
Reference links:
Flask import - https://flask.palletsprojects.com/en/stable/quickstart/
Jsonify and requests - https://flask.palletsprojects.com/en/stable/api/#module-flask
MongoClient - https://pymongo.readthedocs.io/en/stable/api/pymongo/mongo_client.html
JSON module - https://docs.python.org/3/library/json.html
'''

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")  # Establishes the connection to MongoDB
db = client['order_database']  # Selects the database
collection = db['orders']  # Selects the collection
'''
Reference links:
MongoClient connections - https://pymongo.readthedocs.io/en/stable/tutorial.html#getting-a-mongodb-server
'''

# Route to handle the upload of orders
@app.route('/upload_orders', methods=['POST'])
def upload_orders(): #Function
    
    # Assign the uploaded file to variable `file`
    file = request.files.get('file')  # Retrieves the file object from the request
    
    # Check if the file is part of the request
    if file is None:  # Ensures the request contains a file
        return jsonify({"message": "No file part"}), 400  # Responds with an error if no file part found

    # Check if a file was selected
    if file.filename == '':  # Ensures a file is selected
        return jsonify({"message": "No selected file"}), 400  # Responds with an error if no file selected
    
    try: # Validate
        orders = json.load(file)  # Reads the file content as JSON
    except: # Catch and handle JSON reading errors
        return jsonify({"message": "Invalid JSON format"}), 400  # Responds with an error if JSON is invalid
    
    # Check if the JSON is a list
    if type(orders) is list:  # Validates the JSON if it's a list
        db.orders.insert_many(orders)  # Insert orders into the orders collection
        return jsonify({"message": "Orders added successfully"}), 201  # Responds with a success message
    else:
        return jsonify({"message": "Invalid JSON format. Expected a list of orders"}), 400  # Responds with an error if JSON is not a list
'''
Reference links:
Flask route decorator - https://flask.palletsprojects.com/en/stable/quickstart/#routing
Request files - https://flask.palletsprojects.com/en/stable/patterns/fileuploads/
Insert many - https://pymongo.readthedocs.io/en/stable/tutorial.html#inserting-many-documents
Type checking - https://docs.python.org/3/library/functions.html#type
'''

# Entry point for running the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=2000)  # Runs the Flask application in debug mode
'''
Reference links:
Running flask - https://copilot.microsoft.com/?FORM=undexpand&
'''