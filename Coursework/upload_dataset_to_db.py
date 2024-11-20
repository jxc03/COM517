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

if __name__ == '__main__':
    main()  # Run the main function