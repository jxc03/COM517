from pymongo import MongoClient
from datetime import datetime, timedelta
import random
from flask import Flask, request, jsonify


app = Flask(__name__)

# Connection to MongoDB
client = MongoClient('mongodb://localhost:27017/')
database = client['coursework_dbVideo']
collection = database['categoriesVideo']

# Added to better use $elemMatch
@app.route('/update_all_tags_random', methods=['POST'])
def update_all_tags_random():
    # Define possible categories and importance ranges
    categories = ["technical", "content", "quality", "structure", "methodology"]
    
    # Define start and end dates for random date generation
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 2, 29)

    documents = collection.find({})
    
    for doc in documents:
        new_tags = []
        for tag in doc['Tags']:
            # Generate random values
            random_importance = random.randint(1, 5)
            random_category = random.choice(categories)
            
            # Generate random date within range
            random_days = random.randint(0, (end_date - start_date).days)
            random_date = start_date + timedelta(days=random_days)
            date_str = random_date.strftime("%d/%m/%Y")

            new_tag = {
                "name": tag,
                "importance": random_importance,
                "category": random_category,
                "dateAdded": date_str
            }
            new_tags.append(new_tag)
            
        collection.update_one(
            {"_id": doc['_id']},
            {"$set": {"Tags": new_tags}}
        )
    
    return jsonify({"message": "Tags updated successfully"})

@app.route('/check_updated_tags', methods=['GET'])
def check_updated_tags():
    documents = collection.find({}, {"Tags": 1})
    result = []
    for doc in documents:
        doc["_id"] = str(doc["_id"])
        result.append(doc)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=3000)