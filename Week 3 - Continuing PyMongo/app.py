from flask import Flask, request

app = Flask(__name__)

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

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return f"The multiplication of {a} and {b} is {a * b}"

#Script execution
if __name__ == '__main__':
    app.run(debug=True, port = 5000) #Runs in debug mode on port 5000

