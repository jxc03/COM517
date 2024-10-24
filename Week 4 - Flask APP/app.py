'''
Documentation links
PyMongo - https://pymongo.readthedocs.io/en/stable/index.html#
MongoDB PyMongo - https://www.mongodb.com/docs/languages/python/pymongo-driver/current/
'''

from flask import Flask, request, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# Connecting to MongoDB
client = MongoClient("mongodb://localhost:27017/") # Establishes the connection to MongoDB
db = client['user_database'] # Selects the database
collection = db['users'] # Selects the collection

'''
Route to get users by age range.
Accepts `min_age` and `max_age` as query parameters.
Returns a JSON array of users within the specified age range or an error message if something goes wrong.
'''
# Gets user by age range
@app.route('/users/age_range', methods=['GET'])  # Defines a route for GET requests to fetch users by age range
def get_users_by_age_range():  # Function to get users by age range
    try: #Tests the code

        # Gets the 'min_age' and 'max_age' query parameters, defaulted to 0 and 100
        min_age = int(request.args.get('min_age', 0))  # Minimum age filter, defaults to 0 if not provided
        max_age = int(request.args.get('max_age', 100))  # Maximum age filter, defaults to 100 if not provided
        
        # Creates the query for the age range filter
        query = {'age': {'$gte': min_age, '$lte': max_age}}  # Filters to find users within the age range
        # Queries the database and excludes the MongoDB '_id' field
        users = list(collection.find(query, {"_id": 0}))  # Execute query and convert results to a list, excluding '_id' field
        
        # Checks if no users are found
        if not users:  # If the list of users is empty
            return jsonify({"message": "No users found in the given age range"}), 404  # Returns a message indicating no users found
        # If there is then returns the users
        return jsonify(users), 200 # Returns the list of users as JSON with a 200 status code

    # If any error occurs, handles it here    
    except Exception as e:  # Handles any exceptions that occur
        return jsonify({"error": str(e)}), 500  # Returns an error message with exception details and 500 status code
'''
/*To test*/
Url - change number of 20 and 30
http://127.0.0.1:5000/users/age_range?min_age=20&max_age=30

/*Links to help understand*/
$gte 
- https://www.mongodb.com/docs/manual/reference/operator/query/gte/
$lte 
- https://www.mongodb.com/docs/manual/reference/operator/query/lte/
request.args.get
- https://flask.palletsprojects.com/en/stable/reqcontext/
- https://docs.python-requests.org/en/latest/index.html#
'''

# Gets user by city
@app.route('/users/city/<city>', methods=['GET'])  # Defines a route for GET requests to fetch users by city
def get_users_by_city(city):  # Function to get users by city
    
    # Try block,  tests the code
    try:  

        # Creates a case-insensitive regex query for matching city names
        query = {'city': {'$regex': city, '$options': 'i'}}  # Filters to find users by city
        # Executes the query and convert results to a list, excluding '_id' field
        users = list(collection.find(query, {"_id": 0}))  # Gets the results 
        
        # Checks if no users are found
        if not users:  # If the list of users is empty
            return jsonify({"message": f"No users found in the city: {city}"}), 404  # Returns a message indicating no users found
        # If users are found
        return jsonify(users), 200  # Returns the list of users as JSON with a 200 status code
    
    # Except block, handles any error that occurs
    except Exception as e:   
        return jsonify({"error": str(e)}), 500  # If there is, returns an error message with exception details and 500 status code
'''
/*To test*/
Url - change Belfast
http://127.0.0.1:5000/users/city/Belfast

/*Links to help understand*/
$regex
- https://www.mongodb.com/docs/manual/reference/operator/query/regex/
$options
- https://www.mongodb.com/docs/manual/reference/operator/query/regex/#mongodb-query-op.-options
'''



if __name__ == '__main__':
    app.run(debug=True)
    