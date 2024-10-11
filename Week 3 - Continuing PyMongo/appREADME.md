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
@app.route('/substract/<int:a>/<int::b>') #Root route
def substract(a, b): #Defines function, takes a and b as input 
    return f"The substraction of {a} and {b} is {a - b}" #Output
```

**T9**<br>
Create a multiply route.<br>
Add a route `/multiply/<a>/<b>` that takes two numbers as input and returns their product.

```python

```

**T6**<br>

```python

```