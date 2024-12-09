from flask import Flask, request, jsonify
from pymongo import MongoClient
import json
from bson.json_util import loads, dumps
from datetime import datetime

app = Flask(__name__)

# Connection to MongoDB
client = MongoClient('mongodb://localhost:27017/')
database = client['coursework_db']
collection = database['categories']

# http://127.0.0.1:2000/show_all
# Show all documents
@app.route('/show_all', methods=['GET'])
def show_all():
    try: # Try the code 
        all_documents = collection.find({}) # Find all documents
        documents = [{**document, "_id": str(document["_id"])} for document in all_documents] # Take documents and convert ObjectID
        return jsonify(documents), 200 # Output the document
    except Exception as err: # Handle any error
        return jsonify({"Error": str(err)}), 500
    
# http://127.0.0.1:2000/all_appendix
# Show all appendix related concerns
@app.route('/all_appendix', methods=['GET'])
def all_appendix():
    try:
        appendix_documents = collection.find({"Category": "Appendix-related concerns"}) # Find all document specified
        appendix_documents_list = [] # Create list
        for document in appendix_documents:
            document["_id"] = str(document["_id"]) # Handle CbjectID
            appendix_documents_list.append(document) # Add queried document with converted ObjectID to list
        return jsonify(appendix_documents_list), 200 # Output the list of document
    except Exception as err:
        return jsonify({"Error": str(err)}), 500

# http://127.0.0.1:2000/all_MMT
# Show all method, maths and terminology
@app.route('/all_MMT', methods=['GET'])
def all_mmt():
    try:
        mmt_documents = collection.find({"Category": "Method, Mathematics and Terminology"})
        mmt_documents_list = []
        for document in mmt_documents:
            document["_id"] = str(document["_id"])
            mmt_documents_list.append(document)
        return jsonify(mmt_documents_list), 200
    except Exception as err:
        return jsonify({"Error": str(err)}), 500

'''
Select only neccessary fields
'''
# http://127.0.0.1:2000/get_appendix
# Get appendix related concerns with relevant information 
@app.route('/get_appendix', methods=['GET'])
def get_appendix():
    try:
        appendix_documents = collection.find({"Category": "Method, Mathematics and Terminology"}, {"Category": 1, "Comment": 1, "Date": 1, "Severity": 1, "Priority": 1, "Suggested Action": 1}) # Find only 
        result = [{"Category": document["Category"], "Comment": document["Comment"], "Date": document["Date"], "Severity": document["Severity"], "Priority": document["Priority"], "Suggested Action": document["Suggested Action"]} for document in appendix_documents] # Store to a list
        return jsonify(result), 200
    except Exception as err:
        return jsonify({"Error": str(err)}), 500

# http://127.0.0.1:2000/get_mmt
# Get method, maths and terminology with relevant information 
@app.route('/get_mmt', methods=['GET'])
def get_mmt():
    try:
        appendix_documents = collection.find({"Category": "Method, Mathematics and Terminology"}, {"Category": 1, "Comment": 1, "Date": 1, "Severity": 1, "Priority": 1, "Suggested Action": 1})
        result = [{"Category": document["Category"], "Comment": document["Comment"], "Date": document["Date"], "Severity": document["Severity"], "Priority": document["Priority"], "Suggested Action": document["Suggested Action"]} for document in appendix_documents]
        return jsonify(result), 200
    except Exception as err:
        return jsonify({"Error": str(err)}), 500

'''
Match values in an array
'''
# Get documents using tag
# http://127.0.0.1:2000/get_math_tags
# Get all the document that has the 'tag' of 'math'    
@app.route('/get_math_tags', methods=['GET'])
def get_math_tags(): 
    try:
        tags = collection.find({"Tags.name": {"$in": ["math"]}})
        result = [{"Category:": document["Category"],
                "Comment": document["Comment"],
                "Date": document["Date"],
                "Type": document["Type"],
                "Severity": document["Severity"],
                "Priority": document["Priority"],
                "Suggested Action": document["Suggested Action"],
                "Status": document["Status"],
                "Tags": document["Tags"]} for document in tags] 
        return jsonify(result), 200
    except Exception as err:
        return jsonify({"Error": str(err)}), 500
        
'''
Match array element with multiple criteria
'''
# Get documents using severity 
# http://127.0.0.1:2000/get_mmt_severity_high
# Get mmt documents that have the tag of method and the severity of high and priority of high
@app.route('/get_mmt_severity_high', methods=['GET'])
def get_mmt_severity_high():
    try:
        documents = collection.find(
            #{
                #"Tags": {"$in": ["method"]},
                #"Severity": "High"
            #}, 
            #{'_id': 0})
            {
                "Tags": {"$elemMatch": {"name": "method"}}, # Find method tag using elemMatch operator
                "Severity": "High",
                "Priority": "Critical"
            },
            {"_id": 0}) # Excludes ObjectID
        result = list(documents) # Store documents in a list
        return jsonify(result), 200
    except Exception as err:
        return jsonify({"Error": str(err)}), 500
'''
Match arrays containing all specified elements
'''
# Get documents using tag name 
# http://127.0.0.1:2000/get_appendix_missingContent_tag
# Get documents with the tag of appendix and missing content
@app.route('/get_appendix_missingContent_tag', methods=['GET'])
def get_appendix_missingContent_tag():
    try:
        documents = collection.find(
            {"Tags.name": {"$all": ["appendix", "missing content"]}}, # Find all document with specified tags
        )
        result = []
        for document in documents:
            document["_id"] = str(document["_id"])
            result.append(document)
        return jsonify(result), 200
    except Exception as err:
        return jsonify({"Error": str(err)}), 500

'''
Iterating over result sets
'''
# http://127.0.0.1:2000/get_doc_15th_onwards
# Get documents from 15/01/2024 onwards 
@app.route('/get_doc_15th_onwards', methods=['GET'])
def get_doc_15th_onwards():
    try:
        document_finder = collection.find({"Date": {"$gte": "20/01/2024"}}) # Find document after specified date
        result = [{"Category": document["Category"],
                "Comment": document["Comment"],
                "Date": document["Date"],
                "Type": document["Type"],
                "Severity": document["Severity"],
                "Priority": document["Priority"],
                "Suggested Action": document["Suggested Action"],
                "Status": document["Status"],
                "Tags": document["Tags"],
                "Date Reviewed": document["Date Reviewed"],
                "Reviewer ID": document["Reviewer ID"],
                "Reviewer Details": document["Reviewer Details"],
                "Resolved": document["Resolved"],
                "Resolution Date": document["Resolution Date"],
                "Additional Notes": document["Additional Notes"],
                "Impact": document["Impact"]
                } for document in document_finder]
        return jsonify(result), 200
    except Exception as err:
        return jsonify({"Error": str(err)}), 500
    
'''
Query embedded documents and arrays
'''
# Get reviewers by their role
# http://127.0.0.1:2000/get_editor_reviewers
# Get reviewers with the role of editor
@app.route('/get_editor_reviewers', methods=['GET'])
def get_editor_reviewers():
    try:
        editor_reviewers = collection.find({"Reviewer Details.role": {"$regex": "^editor$", "$options": "i"}}) # Find role of editor with case-insensitive
        result = [{"Reviewer Details": r_editor["Reviewer Details"]} for r_editor in editor_reviewers] # Output information within reviewer details
        return jsonify(result), 200
    except Exception as err:
        return jsonify({"Error": str(err)}), 500
    
'''
Match elements in arrays with criteria
'''
# Get documents by their importance 
# http://127.0.0.1:2000/get_important_technical_tag
# Get documents with the tag of importance of 4 and over
@app.route('/get_important_technical_tag', methods=['GET'])
def get_important_technical_tag():
    try:

        documents = collection.find({
            "Tags": {"$elemMatch": { # Find tag that matches
                "category": "technical", # Category of technical
                "importance": {"$gte": 4} # With importance of 4 and above
            }}
        })

        result = []

        for document in documents:
            document["_id"] = str(document["_id"]) # Convert MongoDB ObjectID to a string
            # Code to only include tags with importance that is equal or more than 4
            filter_tags = []
            for tag in document["Tags"]:
                if tag["category"] == "technical" and tag["importance"] >= 4:
                    filter_tags.append(tag)
            document["Tags"] = filter_tags # Update the document with correct tag data
            result.append(document)
        return jsonify(result), 200

    except Exception as err:
        return jsonify({"Error": str(err)}), 500

'''
Match arrays with all elements specified
'''
# http://127.0.0.1:2000/get_specified_tag
# Get all documents that has the tag information specified
@app.route('/get_specified_tag', methods=['GET'])
def get_specified_tag():
    try:

        documents = collection.find({"Tags":[ # Find exact tag criteria
            {
                "name": "method", 
                "importance": 5,
                "category": "content",
                "dateAdded": "06/02/2024"
            },
            {
                "name": "justification", 
                "importance": 5,
                "category": "structure",
                "dateAdded": "06/02/2024"
            }
        ]})

        result = []

        for document in documents:
            document["_id"] = str(document["_id"])
            result.append(document)
        return jsonify(result)

    except Exception as err:
        return jsonify({"Error": str(err)}), 500

# Old code which may have worked
'''
collection.create_index([
    ("Comment", "text"),
    ("Category", "text"),
    ("Additional notes", "text"),
    ("Suggested action", "text")
])
'''

'''
"Perform text search"
'''
# http://127.0.0.1:2000/search
# Get all status pending documents
@app.route('/search', methods=['GET'])
def text_search():
    # Old testing code to help fix index error / duplication
    '''
    try:
        collection.drop_index("Comment_text_Category_text_Additional Notes_text_Tags.name_text")
    except Exception as err:
        print({"Error": str(e)})
    '''
    try:
        text_search = request.args.get('query', '') # Search query, defaulted to a empty string
        if not text_search: # Validate search query
            return jsonify({"Error": "Search query is required"})
        
        results = collection.find(
            {"$text": {"$search": text_search}}, # Find search query
        )

        results_list = json.loads(dumps(list(results))) # Convert to JSON list
        return jsonify({"Results": results_list})
    except Exception as err:
        return jsonify({"Error": str(err)}, 500)

# Code to help debug
'''
@app.route('/indexes', methods=['GET'])
def get_indexes():
    try:
        indexes = list(collection.list_indexes())
        return jsonify({"indexes": json.loads(dumps(indexes))})
    except Exception as err:
        return jsonify({"Error": str(err)}), 500
'''

'''
Transformations
'''
# http://127.0.0.1:2000/severity_impact
# Analyse severity and impact
@app.route('/severity_impact', methods=['GET'])
def severity_impact_analysis():
    try:
        pipeline = [ # Aggregration pinline
            # Group by severity and impact
            {"$group": {
                "_id": {
                    "severity": "$Severity",
                    "impact": "$Impact"
                },
                # Issues
                "total_issues": {"$sum": 1}, # Total number of issues
                "resolved_counter": {"$sum": {"$cond": ["$Resolved", 1, 0]}}, # Count resolved issues 
                # Priorities
                "critical_counter": {"$sum": {"$cond": [{"$eq": ["$Priority", "Critical"]}, 1, 0]}},
                #Categories
                "categories": {"$addToSet": "$Category"}
                }
            },
            # Calculate metrics
            {"$project": {
                "_id": 0,
                "severity": "$_id.severity",
                "impact": "$_id.impact",
                "metrics": {
                    "total_issues": "$total_issues",
                    "resolved_issues": "$resolved_count",
                    "resolution_rate": {"$multiply": [{"$divide": ["$resolved_count", "$total_issues"]}, 100]},
                    "critical_issues": "$critical_count",
                    "affected_categories": {"$size": "$categories"},
                    "category_list": "$categories"
                    }
                }
            },
            # Sort by total issues
            {
                "$sort": {"metrics.total_issues": -1}
            }
        ]

        # Get results
        results = list(collection.aggregate(pipeline))

        # Summary section
        summary = {
            "overview": {
                "total_combinations": len(results),
                "total_issues": sum(r["metrics"]["total_issues"] for r in results),
            },
            "risk": {
                "high_risk": len([r for r in results if r["risk_level"] == "High Risk"]),
                "medium_risk": len([r for r in results if r["risk_level"] == "Medium Risk"]),
                "low_risk": len([r for r in results if r["risk_level"] == "Low Risk"])
            }
        }

        # Output
        return jsonify({
            "Summary": summary,
            "Serverity and impact analysis": results
        })
    
    except Exception as err:
        return jsonify({"error": str(err)}), 500
    
'''   
Deconstruct array into seperate documents
'''
# http://127.0.0.1:2000/unwind_tags
# Break down of tags
@app.route('/unwind_tags', methods=['GET'])
def unwind_tags():
    try:
        pipeline = [
            {"$unwind": "$Tags"},
            {"$project": {
                "_id": 0,
                "Category": 1,
                "Tag Name": "$Tags.name",
                "Tag Category": "$Tags.category",
                "Tag Importance": "$Tags.importance",
                "Date Added": "$Tags.dateAdded",
                "Status": 1,
                "Priority": 1,
                "Severity": 1    
            }
            }
        ]
        result = list(collection.aggregate(pipeline))
        return jsonify({
            "Total tags": len(result),
            "Tags": result
            })
    except Exception as err:
        return jsonify({"Error": str(err)}), 500
'''
MapReduce
'''
# http://127.0.0.1:2000/comment_word_count
# Word count for the comments data
@app.route('/comment_word_count', methods=['GET'])
def word_count():
    try:
        # Define aggregation pipeline for word counting
        pipeline = [
            # Split comments into words
            {
                "$project": {
                    "words": {"$split": ["$Comment", " "]}
                }
            },
            # Unwind to create a document for each word
            {
                "$unwind": "$words"
            },
            # Remove empty strings
            {
                "$match": {
                    "words": {"$ne": ""}
                }
            },
            # Group and count word occurrences
            {
                "$group": {
                    "_id": "$words",
                    "count": {"$sum": 1}
                }
            },
            # Sort by frequency
            {
                "$sort": {"count": -1}
            }
        ]
        
        result = list(collection.aggregate(pipeline))
        
        return jsonify({
            "Total_unique_words": len(result),
            "word_counts": result
        })
        
    except Exception as err:
        return jsonify({"Error": str(err)}), 500

'''
Use aggregration expressions
'''
# http://127.0.0.1:2000/category_analysis
# Analyse categories
@app.route('/category_analysis', methods=['GET'])
def category_analysis():
    try:
        pipeline = [
            {"$unwind": "$Tags"},
            {"$group": {
                "_id": {"category": "$Category", "tag_category": "$Tags.category"},
                        "total_issues": {"$sum": 1},
                        "importance_average": {"$avg": "$Tags.importance"},
                        "tags": {"$addToSet": "$Tags.name"},
                        "resolved_counter": {"$sum": {"$cond": ["$Resolved", 1, 0]}},
                        "high_priority_counter": {"$sum": {"$cond": [{"$eq": ["$Priority", "Critical"]}, 1, 0]}}
                }
            },
            {"$sort": {"total_issues": -1}}, # Sort my highest to lowest
            {"$project": {
                "_id": 0,
                "Main category": "$_id.category",
                "Tag category": "$_id.tag_category",
                "Total issues": "$total_issues",
                "Average importance": "$importance_average",
                "Tag count": {"$size": "$tags"},
                "Tags": "$tags",
                "Resolve count": "$resolved_counter",
                "High priority count": "$high_priority_counter"
                }    
            }     
        ]

        result = list(collection.aggregate(pipeline))
        return jsonify({"Category analysis": result})
    
    except Exception as err:
        return jsonify({"Error": str(err)}), 500
'''
https://www.mongodb.com/docs/manual/reference/operator/update/addToSet/#mongodb-update-up.-addToSet
'''

'''
Conditional update 
'''
# http://127.0.0.1:2000/update_priority [GET, PUT]
# Update documents with priority to critical if severity is high and impact is major
@app.route('/update_priority', methods=['GET', 'PUT'])
def update_priority():
    if request.method == 'PUT':
        try:
            update_fields = list(collection.find({
                "Severity": "High",
                "Impact": "Major",
                "Resolved": False,
                "Priority": {"$ne": "Critical"} 
            }))
            
            result = collection.update_many(
                {
                    "Severity": "High",
                    "Impact": "Major",
                    "Resolved": False,
                    "Priority": {"$ne": "Critical"}
                },
                {
                    "$set": {
                        "Priority": "Critical",
                        "Last_Modified": datetime.now()
                    },
                    "$push": {
                        "Update_History": {
                            "field": "Priority",
                            "old_value": "$Priority",
                            "new_value": "Critical",
                            "date": datetime.now()
                        }
                    }
                }
            )

            updated_documents = []
            if update_fields:
                updated_ids = [document["_id"] for document in update_fields]
                updated_documents = list(collection.find({"_id": {"$in": updated_ids}}))
                for document in updated_documents:
                    document["_id"] = str(document["_id"])
         
            return jsonify({
                "Number of modified": result.modified_count,
                "Modified documents": json.loads(dumps(updated_documents))
            })

        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    # Handle GET request
    return jsonify({"Error": "Please use PUT method to update priorities"})

if __name__ == '__main__':
    app.run(debug=True, port=2000)