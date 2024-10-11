from flask import Flask, request

app = Flask(__name__)

#Route for the root URL
@app.route('/') #Root route
def home(): #Defines function
    return "Welcome to the Flask app!" #Output

#Route for the root URL
@app.route('/hello/<string:name>') #Root route
def hello_user(name): #Defines function, name as
    return f"Hello, {name}!" #Output

#Script execution
if __name__ == '__main__':
    app.run(debug=True, port = 5000) #Runs in debug mode on port 5000

