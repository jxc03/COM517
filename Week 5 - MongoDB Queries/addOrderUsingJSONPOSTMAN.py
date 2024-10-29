from flask import Flask, jsonify, request
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['order_database']

app = Flask(__name__)

def validate_order(order_data):
    """Validates the order data."""
    required_fields = ['order_id', 'amount', 'date', 'items', 'customer']
    
    for field in required_fields:
        if field not in order_data:
            return False, f"The missing required field(s) are: {field}"
    
    if not isinstance(order_data['amount'], (int, float)) or order_data['amount'] <= 0:
        return False, "Amount must be a positive number."

    try:
        datetime.strptime(order_data['date'], '%Y-%m-%d')
    except ValueError:
        return False, "Date must be in YYYY-MM-DD format."

    if not isinstance(order_data['items'], list) or len(order_data['items']) == 0:
        return False, "Items must be a non-empty list."

    for item in order_data['items']:
        if 'product' not in item or 'quantity' not in item or 'price' not in item:
            return False, "Each item must have 'product', 'quantity', and 'price'."
        if not isinstance(item['quantity'], int) or item['quantity'] <= 0:
            return False, "Quantity must be a positive integer."
        if not isinstance(item['price'], (int, float)) or item['price'] <= 0:
            return False, "Price must be a positive number."

    return True, "All required fields are present."

@app.route('/add_order', methods=['POST'])
def add_order():
    """Add a new order to the database."""
    try:
        # Check the Content-Type
        if request.is_json:
            # Handle JSON data
            order_data = request.get_json()
        else:
            # Handle form data
            order_data = request.form.to_dict(flat=True)

            # Convert items from form data if present
            items = []
            items_count = int(order_data.get('items_count', 0))  # Read item count
            for i in range(items_count):
                item = {
                    "product": order_data.get(f'items[{i}][product]'),
                    "quantity": int(order_data.get(f'items[{i}][quantity]', 0)),
                    "price": float(order_data.get(f'items[{i}][price]', 0))
                }
                items.append(item)

            # Create a clean order_data dictionary without unnecessary fields
            order_data = {
                "order_id": order_data['order_id'],
                "amount": float(order_data['amount']),
                "date": order_data['date'],
                "customer": order_data['customer'],
                "items": items
            }

        if not order_data:
            return jsonify({"error": "No data provided"}), 400
        
        # Calls the validation function
        is_valid, error_message = validate_order(order_data)
        if not is_valid:
            return jsonify({"error": error_message}), 400
        
        # Insert the order into MongoDB
        db.orders.insert_one(order_data)
        return jsonify({"message": "Order has been added successfully"}), 201

    except ValueError:
        return jsonify({"error": "Invalid data format"}), 400
    except Exception as err:
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True)

