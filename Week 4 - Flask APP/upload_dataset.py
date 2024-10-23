'''
import json
from pymongo import MongoClient

# Connecting to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Establishes the connection to MongoDB
db = client['user_database']  # Selects the database
users_collection = db['users']  # Selects the collection

# Load the JSON data from the file
with open('users.json') as file:
    users_data = json.load(file)  # Loads the JSON data from the file

# Insert the JSON data into the collection
users_collection.insert_many(users_data)  # Inserts the loaded data into the users collection

print("Data uploaded successfully!")
'''

'''
Script to upload a JSON dataset of users to MongoDB.
The dataset is read from 'users.json' and inserted into the 'users' collection
in the 'user_database' database.
'''

import os
import json
from pymongo import MongoClient, errors

# Connects to MongoDB
def connect_to_mongodb(uri="mongodb://localhost:27017/", db_name="user_database", collection_name="users"):
    try:
        client = MongoClient(uri)  # Establishes the connection to MongoDB
        db = client[db_name]  # Selects the database
        collection = db[collection_name]  # Selects the collection
        return collection
    except errors.ConnectionFailure:
        raise Exception("Could not connect to MongoDB")

# Loads JSON data from file
def load_json_data(file_name):
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(__file__)
        # Construct full path to the users.json file
        file_path = os.path.join(script_dir, file_name)

        with open(file_path, 'r') as file:
            data = json.load(file)  # Loads the JSON data from the file
            if not isinstance(data, list):
                raise Exception("JSON data is not a list of documents")
            print(f"Successfully loaded {len(data)} records from '{file_name}'.")
            return data
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise Exception(f"Error decoding JSON from file: {file_path}")

# Insert data into MongoDB
def insert_data(collection, data):
    if not data:
        raise Exception("No data provided to insert.")
    try:
        collection.insert_many(data)  # Inserts the loaded data into the users collection
        return {"message": "Data uploaded successfully"}
    except Exception as e:
        raise Exception(f"Error inserting data into MongoDB: {e}")

def main():
    try:
        users_collection = connect_to_mongodb()  # Connect to MongoDB
        users_data = load_json_data('users.json')  # Load JSON data
        result = insert_data(users_collection, users_data)  # Insert data into MongoDB
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()  # Run the main function

