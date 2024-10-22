<h1 align="center">
    Week 2 - Continuing PyMongo with query examples
</h1>

<p>
    Creating a simple web application using Flask.
</p>

## Tasks 
**T1**<br>
Import flask and create an app using:

```
from flask import Flask, request

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

Define a route for the root URL that returns a welcome message:

```python
from flask import Flask, request

app = Flask(__name__)

#Route for the root URL
@app.route('/') #Root route
def home(): #Defines function
    return "Welcome to the Flask app!" #Output

#Script execution
if __name__ == '__main__':
    app.run(debug=True, port = 5000) #Runs in debug mode on port 5000
```

**T2**<br>
Create a dynamic hello route.<br>
Add a route `/hello/<name>` that takes a name as input and returns a greating.
 
```python
#Route for the root URL
@app.route('/hello/<string:name>') #Root route
def hello_user(name): #Defines function, name as
    return f"Hello, {name}!" #Output
```

**T3**<br>
Create a greet route.<br>
Add a route `/greet` that returns a static message: "Hello, everyone!".

```python
'''
Route returns a greeting message to user
'''
@app.route('/greet') #Root route
def greet(): #Defines function
    return "Greetings people!" #Output
```

**T4**<br>
Create a simple addition route.<br>
Define a route `/add/<a>/<b>` that takes two numbers as input and returns their sum.<br>
Ensure the parameters are integers.

```python
'''
Route that takes two integers, a and b, from the URL and adds them together
Returns a string that displays the equation and answer
'''
@app.route('/add/<int:a>/<int:b>') #Root route
def add(a, b): #Defines function, takes a and b from URL as integers
    return f"{a} + {b} = {a + b}" #Output
```

**T5**<br>
Create a goodbye route.<br>
Add a route `/goodbye` that returns a farewell message: "Goodbye! Have a great day! Please come back!".

```python
'''
Good bye message to the user
'''
@app.route('/goodbye') #Root route
def goodbye(): #Defines function
    return "Goodbye! Have a great day! Please come back!" #Output
```

**T6**<br>
Create a Show User ID Route.<br>
Define a route `/user/<user_id>` that takes an integer as input and displays the user ID.

```python
'''
Route that takes a the user ID from the URL and displays it
returns a string that displayers the user ID
'''
@app.route('/user/<int:user_id>') #Root route
def show_user(user_id): #Defines function, takes user_id as input
    return f"User ID: {user_id}" #Output
```

**T7**<br>
Create an echo route.<br>
Add a route /echo/<message> that takes a string message and returns it back.

```python
'''
Route that takes a message from the URL and displays it
Returns a string that displays the message
'''
@app.route('/echo/<string:message>') #Root route
def echo_message(message): #Defines function, takes message as input
    return f"Message you said: {message}" #Output
```

**T8**<br>
Create a subtract route.<br>
Add a route `/subtract/<a>/<b>` that takes two numbers as input and returns their difference.

```python
'''
Route that takes two integers, a and b, from the URL and subtracts b from a
Returns a string that displays the equation and answer
'''
@app.route('/subtract/<int:a>/<int::b>') #Root route
def substract(a, b): #Defines function, takes a and b as input 
    return f"The substraction of {a} and {b} is {a - b}" #Output
```

**T9**<br>
Create a multiply route.<br>
Add a route `/multiply/<a>/<b>` that takes two numbers as input and returns their product.

```python
'''
Route that takes two integers, a and b, from the URL and multiplies them
Returns a string that displays the equation and answer
'''
@app.route('/multiply/<int:a>/<int:b>') #Root route
def multiply(a, b): #Function, takes a and b as input
    return f"The multiplication of {a} and {b} is {a * b}" #Output
```

**T10**<br>
Create a divide route<br>
Add a route `/divide/<a>/<b>` that takes two numbers as input and returns their quotient. Ensure the second number is not zero.

```python
'''
Route that takes an integer, number, from the URL and calculates its square
Returns a string that displays the number and its squared result
'''
@app.route('/square/<int:numbers>') #Root route
def square(number): #Function, takes number as input
    return f"The square of {number} is {number ** 2}" #Output
```

**T11**<br>
Create a length of string route<br>
Add a route `/length/<string:input_str>` that takes a string as input and returns its length.

```python
'''
Route that takes a string from the URL and calculates its length.
Returns a string that displays the length of the input string.
'''
@app.route('/length/<string:input_str>') #Root route
def string_length(input_str): #Function, takes input_str as input
    return f"The length of the input string is {len(input_str)}." #Output
```

**T12**<br>
Add user route (/add_user - POST).<br>
This route will allow you to add a new user to the database.

```python
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
```

**T13**<br>
Get all users route (/users - GET).<br>
This route will retrieve all users from the database.

```python
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
```

**T14**<br>
Get user by ID (/user/<user_id> - GET).<br>
This route will return a specific user's details by their MongoDB _id.

```python
'''
Route to retrieve all users from the database.
Returns a JSON object containing a list of users with their IDs, names, and emails.
'''
# Route to get a user by user_id using the GET method
@app.route('/user/<user_id>', methods=['GET'])  # Defines a route for GET requests to fetch a user by their user_id
def get_user(user_id):  # Defines the function to get a user, takes user_id as its parameter
    # Query the database to find the user by user_id
    user = users_collection.find_one({"_id": ObjectId(user_id)})  # Finds the user in the collection using their ObjectId
    if user:  # If the user is found
        return jsonify({"id": str(user["_id"]), "name": user["name"], "email": user["email"]})  # Return user details as JSON
    # If the user is not found
    return jsonify({"error": "User not found"}), 404  # Return an error message with a 404 status code
```

**T15**<br>
Update user route (/update_user/<user_id> - PUT).<br>
This route will update an existing user's name and email.

```python
'''
Route to update a user's name and email in the database
Accepts user_id, name, and email as parameters
Returns a JSON object with a success message upon completion
'''
@app.route('/update_user/<user_id>/<name>/<email>', methods=['PUT']) # Route to update a user's name and email using the PUT method
def update_user(user_id, name, email): # Function to update a user, takes user_id, name, and email as parameters
    
    #Converts the user_id to an ObjectId
    user_id_obj = ObjectId(user_id)
    
    #Updates the user's name and email in the database
    users_collection.update_one( #Update the user's name and email in the database
        {"_id": user_id_obj}, #Finds the user by their ObjectId
        {"$set": {"name": name, "email": email}} #Sets the new name and email values
        )
    
    return jsonify({"message": "User updated successfully!"}) #Returns a success message as JSON
```

**T16**<br>
Delete user route (/delete_user/<user_id> - DELETE).<br>
This route will delete a user by their ID.

```python
'''
Route to delete a user from the database by user_id.
Takes user_id as a URL parameter.
Returns a JSON object with a success message if the user is deleted,
or an error message if the user is not found.
'''
# Route for deleting a user by user_id using the DELETE method
@app.route('/delete_user/<user_id>', methods=['DELETE'])  # Defines the route and allowed HTTP method
def delete_user(user_id):  # Function to delete a user, takes user_id as its parameter
    
    user_id_obj = ObjectId(user_id)  # Convert user_id to ObjectId
    
    # Attempt to delete the user from the database
    result = users_collection.delete_one({"_id": user_id_obj})  # Deletes a single document from the users collection
    
    if result.deleted_count > 0:  # If the deletion was successful
        return jsonify({"message": f"User {user_id} deleted successfully!"})  # Return success message as JSON
    
    # If no user was deleted (user not found)
    return jsonify({"error": "User not found"}), 404  # Return an error message with a 404 status code
```

**T17**<br>
Filter users by name (/users/name/<name> - GET).<br>
This route will filter users by their name.

```python
'''
Route to retrieve users by their name from the database.
Takes a name as a URL parameter.
Returns a JSON object containing a list of users with their IDs, names, and emails.
'''
# Route for retrieving users by name using the GET method
@app.route('/users/name/<name>', methods=['GET'])  # Defines the route and allowed HTTP method
def get_users_by_name(name):  # Function to get users by name, takes name as its parameter
    
    # Query the database to find users with the specified name
    users = users_collection.find({"name": name})  # Finds all users with the given name
    
    # Create a list of users with their details
    result = [{"id": str(user["_id"]), "name": user["name"], "email": user["email"]} for user in users]  # Convert ObjectId to string and create a list of user details
    
    # Return the list of users as JSON
    return jsonify({"users": result})  # Sends the user list as JSON
```


