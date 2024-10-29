
```python
@app.route('/add_order', methods=['POST'])
def add_order():
    order_data = request.get_json()
    db.orders.insert_one(order_data)
    return jsonify({"message": "Order added successfully"}), 201
```

Uploaded order using POST request in POSTMAN. Body - raw - JSON type
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
```
curl -X POST -H "Content-Type: application/json" -d "{\"order_id\":\"ORD007\",\"amount\":420,\"date\":\"2024-04-26\",\"items\":[{\"product\":\"Monitor\",\"quantity\":2,\"price\":200},{\"name\":\"Mousepad\",\"quantity\":1,\"price\":20}],\"customer\":\"Curl Work\"}" http://127.0.0.1:5000/add_order
```