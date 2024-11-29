'''
import json
from pymongo import MongoClient, errors

# Connect to MongoDB
def connect_to_mongodb(uri="mongodb://localhost:27017/", db_name="coursework_db", collection_name="categories"):
    try:
        client = MongoClient(uri)  # Connection to MongoDB
        db = client[db_name]  # Selects the database
        collection = db[collection_name]  # Selects the collection
        print("Connection successful")
        return collection
    except Exception as err:
        raise Exception("Error occured:", err)

# Load JSON data from file
def load_json_data(file_name):
    try:
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
'''

import json  # Import JSON module for reading/writing JSON files
from pymongo import MongoClient
import os  # Import os module to check file existence

# MongoDB connection
mongo_uri = "mongodb://localhost:27017/"
database_name = "coursework_db"
collection_name = "categories"

def upload_data():
    try: 
        file_path = 'coursework\dataset_json.json'  # File path for JSON data
        print(f"Reading JSON file: {file_path}")  # Display to terminal

        # Verify file path
        if not os.path.exists(file_path):
            print(f"Error: File not found")
            print("Please ensure the file path is correct")
            return

         # Read JSON data
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Connect to MongoDB
        client = MongoClient(mongo_uri)
        db = client[database_name]
        collection = db[collection_name]
        print(f"Connected to MongoDB: {database_name}")

        # Check for existing data
        if collection.count_documents({}) > 0:
            action = input("Database contains data. (c)lear, (a)ppend, or (x)cancel?: ").lower()
            if action == 'c':
                collection.delete_many({})
                print("Existing data cleared")
            elif action != 'a':
                print("Import cancelled")
                return

        # Import data
        result = collection.insert_many(data)
        print(f"Successfully imported {len(result.inserted_ids)} documents")

    # Handle exception errors   
    except Exception as err:
        print(f"Error: {str(err)}")

if __name__ == "__main__":
    upload_data()