

## Tasks 
**T1**<br>
Adding dataset using Flask API.

```python
from flask import Flask, jsonify, request
from pymongo import MongoClient
import json

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Establishes the connection to MongoDB
db = client['order_database']  # Selects the database
collection = db['orders']  # Selects the collection

@app.route('/upload_orders', methods=['POST'])
def upload_orders():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    
    if file:
        orders = json.load(file)
        if isinstance(orders, list):
            db.users.insert_many(orders)
            return jsonify({"message": "Users added successfully"}), 201
        else:
            return jsonify({"message": "Invalid JSON format. Expected a list of users."}), 400

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
```

Uploading dataset using cURL, make sure to run the terminal using cmd and to cd to your directory.
```cmd
curl -X POST -F "file=@orders.json" http://127.0.0.1:2000/upload_orders
```

**T2**<br>
Adding endpoint to insert data.

```python
@app.route('/add_order', methods=['POST'])
def add_order():
    order_data = request.get_json()
    print(order_data)
    db.orders.insert_one(order_data)
    return jsonify({"message": "Order added successfully"}), 201
```

Uploading order using POST request in POSTMAN. Body - raw - JSON type.<br>
Uploading order using cURL.

```json
{
  "order_id": "ORD006",
  "amount": 120,
  "date": "2024-04-21",
  "items": [
    {"product": "Headphone", "quantity": 1, "price": 90},
    {"product": "Mousepad", "quantity": 1, "price": 30}
  ],
  "customer": "Second Try"
}
```
```cmd
curl -X POST -H "Content-Type: application/json" -d "{\"order_id\":\"ORD007\",\"amount\":420,\"date\":\"2024-04-26\",\"items\":[{\"product\":\"Monitor\",\"quantity\":2,\"price\":200},{\"name\":\"Mousepad\",\"quantity\":1,\"price\":20}],\"customer\":\"Curl Work\"}" http://127.0.0.1:5000/add_order
```

**T3**<br>
Selecting only necessary fields.<br>
The first code selects only the 'order_id' and 'customer' (name) from the orders collection.<br>
The second code excludes the '_id'.

```python
# Route to get users 
@app.route('/get_orders', methods=['GET'])
def get_orders(): # Defining function

    # Queries the database to get 'order_id' and 'customer' for each order
    orders = db.orders.find({}, {"order_id": 1, "customer": 1}) # Finds all orders

    # Creates a list [] of dictionaries {} with 'order_id' and 'customer' for each order
    result = [{"order_id": order["order_id"], "customer": order["customer"]} for order in orders] # List of results
    
    # Returns the list as a JSON response
    return jsonify(result) # Output, returns the result list (order id and customer name)
```
```python
# Route to get users 
@app.route('/get_orders_no_id', methods=['GET'])
def get_orders_no_id():
    # Queries the database to get 'order_id' and 'customer' for each order
    orders = db.orders.find({}, {"_id": 0, "order_id": 1, "customer": 1}) # Finds all orders

    # Creates a list [] of dictionaries {} with 'order_id' and 'customer' for each order
    result = [{"order_id": order["order_id"], "customer": order["customer"]} for order in orders] # List of results
    
    # Returns the list as a JSON response
    return jsonify(result) # Output, returns the result list (order id and customer name)
```

To test with Postman and cURL<br>
- Create HTTP request<br>
- Enter URL (e.g. http://127.0.0.1:5000/get_orders) and choose GET<br>
- Click Send button
```cmd
curl -X GET http://127.0.0.1:2000/get_orders
```

**T4**<br>
Matching values in an array.<br>
First route uses the '$in' operator to find users who 

```python
# Route to get mouse orders
@app.route('/get_mouse_orders', methods=['GET'])
def get_mouse_orders():
    """
    Handle GET requests to /get_mouse_orders.

    - Queries the database to find orders containing items with product names 'mouse' or 'Mouse'.
    - Constructs a list of such orders and returns it as a JSON response.
    """
    # Queries the database to find orders containing 'mouse' or 'Mouse' in the 'items' array
    orders = db.orders.find({"items.product": {"$in": ["mouse", "Mouse"]}})  # Query for orders with 'mouse' or 'Mouse'

    # Empty list to store orders
    result = []
    
    # Goes through each order and adds relevant items to the result list
    for order in orders:  # Loop through each order in the cursor
        for item in order["items"]:  # Loop through each item in the order's items list
            
            if item["product"] in ["mouse", "Mouse"]:  # Check if the item's product is 'mouse' or 'Mouse'
                result.append(
                    {
                        "customer name": order["customer"],  # Customer name from the order
                        "product": item["product"],  # Product name
                        "quantity": item["quantity"],  # Quantity of the product
                        "price": item["price"],  # Price of the product
                    }
                )
    
    # Return the list as a JSON response
    return jsonify(result)  # Output, returns the result list
```
