'''
Documentation links
PyMongo - https://pymongo.readthedocs.io/en/stable/index.html#
MongoDB PyMongo - https://www.mongodb.com/docs/languages/python/pymongo-driver/current/
Python handling exceptions (try & except) - https://docs.python.org/3/tutorial/errors.html#handling-exceptions
Python Exception - https://docs.python.org/3/library/exceptions.html#Exception
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
@app.route('/users/age_range', methods=['GET'])  # Route for GET requests to fetch users by age range
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

# Gets users by city
@app.route('/users/city/<city>', methods=['GET'])  # Route for GET requests to fetch users by city
def get_users_by_city(city):  # Function to get users by city
    
    # Try block,  tests the code
    try:  

        # Creates a case-insensitive regex query for matching city names
        query = {'city': {'$regex': city, '$options': 'i'}}  # Filters to find users by city
        # Executes the query and convert the results to a list, excluding '_id' field
        users = list(collection.find(query, {"_id": 0}))  # Gets the results 
        
        # Checks if no users are found
        if not users:  # If the list of users is empty
            return jsonify({"message": f"No users found in the city: {city}"}), 404  # Returns a message indicating no users found
        # If users are found
        return jsonify(users), 200  # Returns the list of users as JSON with a 200 status code
    
    # Except block, handles any error that occurs
    except Exception as e: # If any error occurs, handle it here   
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

'''
Route to get users older than a specified age.
Accepts `age` as a URL parameter.
Returns a JSON array of users older than the specified age or an error message if something goes wrong.
'''
# Gets users older than a specific age
@app.route('/users/older_than/<int:age>', methods=['GET'])  # Route for GET requests to fetch users older than the specified age
def get_users_older_than(age):  # Function to get users older than a specified age
    
    # Try block,  tests the code
    try:  

        # Creates a query to find users older than the specified age
        query = {'age': {'$gt': age}}  # Filters to find users 
        # Executes the query and converts the results to a list, excluding '_id' field
        users = list(collection.find(query, {"_id": 0}))  # Gets the results
        
        # Checks if no users are found
        if not users:  # If the list of users is empty
            return jsonify({"message": f"No users found older than {age}"}), 404  # Returns a message indicating no users found
        # If users are found
        return jsonify(users), 200  # Return the list of users as JSON with a 200 status code
    
    # Except block, handles any error that occurs
    except Exception as e:  # If any error occurs, handle it here
        return jsonify({"error": str(e)}), 500  # Return an error message with exception details and 500 status code
'''
/*To test*/
Url - change number of 40
http://127.0.0.1:5000/users/older_than/40

/*Links to help understand*/
$gt
- https://www.mongodb.com/docs/manual/reference/operator/query/gt/?msockid=290353cdb44a6f1b2eeb470cb5296ee6
'''

'''
Route to get users whose names start with a specific letter.
Accepts `letter` as a URL parameter.
Returns a JSON array of users whose names start with the specified letter or an error message if something goes wrong.
'''
#Gets users whose name starts with a specific letter
@app.route('/users/name_starts_with/<letter>', methods=['GET'])  # Route for GET requests to fetch users by name starting with a specific letter
def get_users_name_starts_with(letter):  # Function to get users by name starting with a specific letter
    
    #Try block, tests the code
    try:
        # Creates a case-insensitive regex query for matching names starting with the specified letter
        query = {'name': {'$regex': f'^{letter}', '$options': 'i'}}  # Filters to find users whose names start with the given letter

        # Executes the query and convert results to a list, excluding '_id' field
        users = list(collection.find(query, {"_id": 0}))  # Get results as a list 
        
        # Checks if no users are found
        if not users:  # If the list of users is empty
            return jsonify({"message": f"No users found whose name starts with '{letter}'"}), 404  # Returns a message indicating no users found
        # If users are found
        return jsonify(users), 200  # Returns the list of users as JSON with a 200 status code
    
    # Except block, handles any error that occurs
    except Exception as e:  # If any error occurs, handle it here
        return jsonify({"error": str(e)}), 500  # Returns an error message with exception details and 500 status code
'''
/*To test*/
Url - change number of 40
http://127.0.0.1:5000/users/older_than/40

/*Links to help understand*/
^{letter}
- https://docs.python.org/3/howto/regex.html#more-metacharacters
- https://docs.python.org/3/howto/regex.html
'''

'''
Route to get the youngest user.
Returns a JSON object of the youngest user or an error message if something goes wrong.
'''
# Gets the youngest user
@app.route('/users/youngest', methods=['GET'])  # Route for GET requests to fetch the youngest user
def get_youngest_user():  # Function to get the youngest user
    
    #Try block, tests the code
    try: 
        # Queries the collection to find all users, sorts them by age in ascending order, and limits the results to 1
        youngest = collection.find({}, {"_id": 0}).sort('age', 1).limit(1)  # Finds the youngest user and exclude '_id' field
        # Returns the youngest user as JSON with a 200 status code
        return jsonify(list(youngest)), 200 # Fetches results, makes a list and returns as JSON
    
    # Except block, handles any error that occurs
    except Exception as e:  # If any error occurs, handle it here
        return jsonify({"error": str(e)}), 500  # Returns an error message with exception details and 500 status code


'''
Route to get the oldest user.
Returns a JSON object of the oldest user or an error message if something goes wrong.
'''
# Gets the oldest user
@app.route('/users/oldest', methods=['GET'])  # Route for GET requests to fetch the oldest user
def get_oldest_user():  # Function to get the oldest user
    
    #Try block, tests the code
    try:  
        # Queries the collection to find all users, sorts them by age in descending order, and limits the results to 1
        oldest = collection.find({}, {"_id": 0}).sort('age', -1).limit(1)  # Find the oldest user and exclude '_id' field
        # Returns the oldest user as JSON with a 200 status code
        return jsonify(list(oldest)), 200  # Convert cursor to list and return as JSON
    
    # Except block, handles any error that occurs
    except Exception as e:  # If any error occurs, handle it here
        return jsonify({"error": str(e)}), 500  # Returns an error message with exception details and 500 status code


if __name__ == '__main__':
    app.run(debug=True)
    