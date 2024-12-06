from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import json_util
import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/coursework_db"
mongo = PyMongo(app)

def setup_database():
    """Create text index for search functionality"""
    mongo.db.categories.create_index([
        ("Comment", "text"),
        ("Category", "text"),
        ("Additional Notes", "text"),
        ("Tags.name", "text")
    ])

def perform_text_search(search_text, filters=None):
    """
    Perform text search with optional filters
    
    Args:
        search_text (str): Text to search for
        filters (dict): Optional MongoDB filters to apply
    
    Returns:
        list: Search results
    """
    # Base query with text search
    query = {"$text": {"$search": search_text}}
    
    # Add any additional filters
    if filters:
        query.update(filters)
    
    # Define fields to return and include search score
    projection = {
        "score": {"$meta": "textScore"},
        "Comment": 1,
        "Category": 1,
        "Status": 1,
        "Priority": 1,
        "Tags": 1,
        "_id": 0
    }
    
    # Execute search and sort by relevance
    results = mongo.db.categories.find(
        query,
        projection
    ).sort([("score", {"$meta": "textScore"})])
    
    return list(results)

@app.route("/api/search", methods=["GET"])
def search():
    """
    Search endpoint supporting text search and filters
    
    Query Parameters:
        q (str): Search text
        status (str, optional): Filter by status
        priority (str, optional): Filter by priority
        category (str, optional): Filter by category
    """
    try:
        # Get search text (required)
        search_text = request.args.get("q")
        if not search_text:
            return jsonify({"error": "Search text is required"}), 400
            
        # Build filters from query parameters
        filters = {}
        if status := request.args.get("status"):
            filters["Status"] = status
        if priority := request.args.get("priority"):
            filters["Priority"] = priority
        if category := request.args.get("category"):
            filters["Category"] = category
            
        # Perform search
        results = perform_text_search(search_text, filters)
        
        # Convert results to JSON
        documents = json.loads(json_util.dumps(results))
        
        return jsonify({
            "query": {
                "search_text": search_text,
                "filters": filters
            },
            "count": len(documents),
            "results": documents
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/filters", methods=["GET"])
def get_filters():
    """Get available filter values for the search interface"""
    try:
        return jsonify({
            "categories": list(mongo.db.categories.distinct("Category")),
            "statuses": list(mongo.db.categories.distinct("Status")),
            "priorities": list(mongo.db.categories.distinct("Priority"))
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    setup_database()
    app.run(debug=True)

    