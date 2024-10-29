from flask import Flask, jsonify, request # Imports the modules that will be used
from pymongo import MongoClient # Imports the MongoDB client
from collections import OrderedDict
# Connecting to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Establishes the connection to MongoDB
db = client['order_database']  # Selects the database
collection = db['orders']  # Selects the collection

# Creates the Flask app
app = Flask(__name__)

# Validates the 'add_order' data
def validate_order(order_data): # Defining the function, takes 'order_data' as its' parameter
    
    required_fields = ['order_id', 'amount', 'date', 'items', 'customer'] # List of field that is required
    
    for field in required_fields: # Checks if the field matches to the fields in 'required_fields'
        if field not in order_data: # Checks if field is present
            return False, f"The missing required field(s) are: {field}" # Returns a error message if a field is missing
    return True, "All required fields are present" # Proceeds if all fields are in
'''
Reference links:
Looping through required fields - https://wiki.python.org/moin/ForLoop
'''

# Adds a new order to the database
@app.route('/add_order', methods=['POST']) # Route for adding orders
def add_order(): # Defining the function 

    try: # Tests code
        order_data = request.get_json() # Gets JSON data from request
        if order_data is None: # Checks if there is no data
            return jsonify({"error": "There is no data provided"}), 400 # Returns error message if there's no data
        '''
        Reference links:
        Handling incoming JSON data - https://tedboy.github.io/flask/generated/generated/flask.Request.get_json.html
        Checking for no data - https://medium.com/@Hichem_MG/check-if-a-variable-is-not-none-in-python-3d6407798dec
        '''
        
        # Calls the validation function
        validate_order(order_data) # Validating order data

        # If validation passes, it will insert the order to MongoDB
        db.orders.insert_one(order_data) # Adds the order data to the datababase
        return jsonify({"message": "Order has been added successfully"}), 201 # Returns a success message
        '''
        Reference links:
        Inserting data into MongoDB - https://pymongo.readthedocs.io/en/stable/tutorial.html#inserting-documents
        '''

    except ValueError: # Handles value errors
        return jsonify({"error": "Invalid data format"}), 400 # Returns a error message for invalid format
    except Exception as err: # Handles any other exception
        return jsonify({"error": str(err)}), 500 # Returns a general error message
    '''
    Reference links:
    Exception handling - https://docs.python.org/3/tutorial/errors.html
    '''

# Route to get users 
@app.route('/get_orders', methods=['GET'])
def get_orders(): # Defining function

    try: # Tests code
        # Queries the database to get 'order_id' and 'customer' for each order
        orders = db.orders.find({}, {"_id": 1, "order_id": 1, "customer": 1}) # Finds all orders

        # Empty list to store orders
        result = []

        # Goes through each order and adds it to the result list
        for order in orders: # 
            result.append(
                {
                    "id": str(order["_id"]), # Convert ObjectID to a string
                    "order_id": order["order_id"],
                    "customer name": order["customer"]
                }
            )

        # Checks if the result list is empty
        if len(result) == 0: # If it is
            print({"message": "No orders found"}) # Output, returns message
            return jsonify(result) # Output, returns empty list
        print("Orders retrieved successfully") # Confirmation message
        return jsonify(result) # Output, returns the result list (order id and customer name)
    
    except Exception as err: # Handles exceptions
        print(f"Error: {err}") # Outputs error message
        return jsonify({"error": str(err)}), 500 # Output, returns error message

# Route to get users 
@app.route('/get_orders_no_id', methods=['GET'])
def get_orders_no_id():
    
    # Queries the database to get 'order_id' and 'customer' for each order
    orders = db.orders.find({}, {"_id": 0, "order_id": 1, "customer": 1}) # Finds all orders

    # Creates a list [] of dictionaries {} with 'order_id' and 'customer' for each order
    result = [{"order_id": order["order_id"], "customer name": order["customer"]} for order in orders] # List of results
    
    # Returns the list as a JSON response
    return jsonify(result) # Output, returns the result list (order id and customer name)

# Route to get mouse orders
@app.route('/get_mouse_orders', methods=['GET'])
def get_mouse_orders():

    try:
        orders = db.orders.find({"items.product": {"$in": ["mouse", "Mouse"]}})

        result = []

        for order in orders:
            for item in order["items"]:
                
                if item["product"] in ["mouse", "Mouse"]:
                    result.append(
                        {
                            "customer name": order["customer"],
                            "product": item["product"],
                            "quantity": item["quantity"],
                            "price": item["price"],
                        }
                    )

        if not result:
            return jsonify({"message": "No mouse orders found."}), 404
        return jsonify(result)
    
    except Exception as err:
        return jsonify({"error": str(err)}), 500

# Entry point for running the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=2000)  # Runs the Flask application in debug mode

