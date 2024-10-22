from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client['user_database'] # Selects the database
users_collection = db['users'] # Selects the collection

'''
Welcome message to user when user visit the root url
'''
@app.route('/') #Root route
def home(): #Defines function
    return "Welcome to the Flask app!" #Output

'''
Route for greeting user with the name user provides
Returns a string greeting to the user with provided name
'''
@app.route('/hello/<string:name>') #Root route
def hello_user(name): #Defines function, takes name as input
    return f"Hello, {name}!" #Output

'''
Greeting message to user
'''
@app.route('/greet') #Root route
def greet(): #Defines function
    return "Greetings people!" #Output

'''
Route that takes two integers, a and b, from the URL and adds them together
Returns a string that displays the equation and answer
'''
@app.route('/add/<int:a>/<int:b>') #Root route
def add(a, b): #Defines function, takes a and b from URL as integers
    return f"{a} + {b} = {a + b}" #Output

'''
Good bye message to the user
'''
@app.route('/goodbye') #Root route
def goodbye(): #Defines function
    return "Goodbye! Have a great day! Please come back!" #Output

'''
Route that takes a the user ID from the URL and displays it
Returns a string that displays the user ID
'''
@app.route('/user/<int:user_id>') #Root route
def show_user(user_id): #Defines function, takes user_id as input
    return f"User ID: {user_id}" #Output

'''
Route that takes a message from the URL and displays it
Returns a string that displays the message
'''
@app.route('/echo/<string:message>') #Root route
def echo_message(message): #Defines function, takes message as input
    return f"Message you said is: {message}" #Output

'''
Route that takes two integers, a and b, from the URL and subtracts b from a
Returns a string that displays the equation and answer
'''
@app.route('/subtract/<int:a>/<int:b>') #Root route
def subtract(a, b): #Defines function, takes a and b as input 
    return f"The substraction of {a} and {b} is {a - b}" #Output

'''
Route that takes two integers, a and b, from the URL and multiplies them
Returns a string that displays the equation and answer
'''
@app.route('/multiply/<int:a>/<int:b>') #Root route
def multiply(a, b): #Function, takes a and b as input
    return f"The multiplication of {a} and {b} is {a * b}" #Output

'''
Route that takes an integer, number, from the URL and calculates its square
Returns a string that displays the number and its squared result
'''
@app.route('/square/<int:number>') #Root route
def square(number): #Function, takes number as input
    return f"The square of {number} is {number ** 2}" #Output

'''
Route that takes a string from the URL and calculates its length.
Returns a string that displays the length of the input string.
'''
@app.route('/length/<string:input_str>') #Root route
def string_length(input_str): #Function, takes input_str as input
    return f"The length of the input string is {len(input_str)}." #Output

'''
Route to add a new user to the database.
Accepts a JSON object with the user's name and email via a POST request.
Returns a success message and the user's ID if successful, 
or an error message if input is invalid.
'''
@app.route('/add_user', methods=['POST'])  # Root route to add user, POST method
def add_user():

    # Retrieve the JSON data from the request
    data = request.get_json()
    
    # Extract name and email from the received data
    name = data.get('name')
    email = data.get('email')

    # Check if both name and email are provided
    if name and email:
        # Insert the new user into the database and get the inserted ID
        user_id = users_collection.insert_one({"name": name, "email": email}).inserted_id
        
        # Return a success message with the user's ID
        return jsonify({"message": "User added successfully", "id": str(user_id)})
    
    # Return an error message if input is invalid (missing name or email)
    return jsonify({"error": "Invalid input"}), 400  # 400 status code for bad request

'''
Route to retrieve all users from the database.
Returns a JSON object containing a list of users with their IDs, names, and emails.
'''
@app.route('/users', methods=['GET'])  # Root route to get all users, using the GET method
def get_users():
    # Retrieve all user documents from the users_collection
    users = users_collection.find()  # Query to get all users

    # Create a list of users, formatting each user document as a dictionary
    result = [
        {
            "id": str(user["_id"]),  # Convert ObjectId to string for JSON serialization
            "name": user["name"],    # Extract the user's name
            "email": user["email"]    # Extract the user's email
        } 
        for user in users  # Iterate through each user document in the result
    ]
    
    # Return a JSON response containing the list of users
    return jsonify({"users": result})  # Wrap the result in a dictionary with the key "users"


@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users_collection.find_one({"_id": ObjectId(user_id)})

    if user:
        return jsonify({"id": str(user["_id"]), "name": user["name"], "email": user["email"]})
    return jsonify({"error": "User not found"}), 404

@app.route('/update_user/<user_id>/<name>/<email>', methods=['PUT'])
def update_user(user_id, name, email):
    user_id_obj = ObjectId(user_id)

    users_collection.update_one(
        {"_id": user_id_obj}, 
        {"$set": {"name": name, "email": email}}
        )
    return jsonify({"message": "User updated successfully!"})


@app.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    
    if result.deleted_count > 0:
        return jsonify({"message": f"User {user_id} deleted successfully!"})
    return jsonify({"error": "User not found"}), 404


@app.route('/users/name/<name>', methods=['GET'])
def get_users_by_name(name):
    users = users_collection.find({"name": name})
    result = [{"id": str(user["_id"]), "name": user["name"], "email": user["email"]} for user in users]
    return jsonify({"users": result})

#Execution
if __name__ == '__main__':
    app.run(debug=True, port = 2000) #Runs in debug mode on port 5000

