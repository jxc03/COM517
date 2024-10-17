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

@app.route('/multiply/<int:a>/<int:b>') #Root route
def multiply(a, b): #Function, takes a and b as input
    return f"The multiplication of {a} and {b} is {a * b}" #Output

@app.route('/square/<int:number>') #Root route
def square(number): #Function, takes number as input
    return f"The square of {number} is {number ** 2}" #Output

@app.route('/length/<string:input_str>') #Root route
def string_length(input_str): #Function, takes input_str as input
    return f"The length of the input string is {len(input_str)}." #Output

@app.route('/add_user', methods=['POST']) #Root route to add user, POST method
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if name and email:
        user_id = users_collection.insert_one({"name": name, "email": email}).inserted_id
        return jsonify({"message": "User added successfully", "id": str(user_id)})
    return jsonify({"error": "Invalid input"}), 400

@app.route('/users', methods=['GET'])
def get_users():
    users = users_collection.find()
    result = [{"id": str(user["_id"]), "name": user["name"], "email": user["email"]} for user in users]
    return jsonify({"users": result})

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

