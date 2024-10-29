

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
curl -X POST -F "file=@orders.json" http://127.0.0.1:5000/upload_orders
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

Uploading order using POST request in POSTMAN. Body - raw - JSON type
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

Uploading order using cURL
```cmd
curl -X POST -H "Content-Type: application/json" -d "{\"order_id\":\"ORD007\",\"amount\":420,\"date\":\"2024-04-26\",\"items\":[{\"product\":\"Monitor\",\"quantity\":2,\"price\":200},{\"name\":\"Mousepad\",\"quantity\":1,\"price\":20}],\"customer\":\"Curl Work\"}" http://127.0.0.1:5000/add_order
```

**T3**<br>