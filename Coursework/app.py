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

# Show all documents
@app.route('/show_all', methods=['GET'])
def show_all():
    all_documents = collection.find({})
    documents = [{**document, "_id": str(document["_id"])} for document in all_documents]
    return jsonify(documents), 200

# Show all appendix related concerns
@app.route('/all_appendix', methods=['GET'])
def all_appendix():
    appendix_documents = collection.find({"Category": "Appendix-related concerns"})
    appendix_documents_list = []
    for document in appendix_documents:
        document["_id"] = str(document["_id"])
        appendix_documents_list.append(document)
    return jsonify(appendix_documents_list), 200

# Show all method, maths and terminology
@app.route('/all_MMT', methods=['GET'])
def all_mmt():
    mmt_documents = collection.find({"Category": "Method, Mathematics and Terminology"})
    mmt_documents_list = []
    for document in mmt_documents:
        document["_id"] = str(document["_id"])
        mmt_documents_list.append(document)
    return jsonify(mmt_documents_list), 200

'''
Select only neccessary fields
'''
# Get appendix related concerns with relevant information 
@app.route('/get_appendix', methods=['GET'])
def get_appendix():
    appendix_documents = collection.find({"Category": "Method, Mathematics and Terminology"}, {"Category": 1, "Comment": 1, "Date": 1, "Severity": 1, "Priority": 1, "Suggested Action": 1}) # Selects only 
    result = [{"Category": document["Category"], "Comment": document["Comment"], "Date": document["Date"], "Severity": document["Severity"], "Priority": document["Priority"], "Suggested Action": document["Suggested Action"]} for document in appendix_documents] # Stores to a list
    return jsonify(result) # Outputs the list

# Get method, maths and terminology with relevant information 
@app.route('/get_mmt', methods=['GET'])
def get_mmt():
    appendix_documents = collection.find({"Category": "Method, Mathematics and Terminology"}, {"Category": 1, "Comment": 1, "Date": 1, "Severity": 1, "Priority": 1, "Suggested Action": 1})
    result = [{"Category": document["Category"], "Comment": document["Comment"], "Date": document["Date"], "Severity": document["Severity"], "Priority": document["Priority"], "Suggested Action": document["Suggested Action"]} for document in appendix_documents]
    return jsonify(result)

'''
Match values in an array
'''
# Get documents using tag
# Get all the document that has the 'tag' of 'math'    
@app.route('/get_math_tags', methods=['GET'])
def get_math_tags(): 
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
    return jsonify(result)

'''
Match array element with multiple criteria
'''
# Get documents using severity 
# Get mmt documents that have the tag of method and the severity of high and priority of high
@app.route('/get_mmt_severity_high', methods=['GET'])
def get_mmt_severity_high():
    documents = collection.find(
        #{
            #"Tags": {"$in": ["method"]},
            #"Severity": "High"
        #}, 
        #{'_id': 0})
        {
            "Tags": {"$elemMatch": {"name": "method"}},
            "Severity": "High",
            "Priority": "Critical"
        },
        {"_id": 0})
    result = list(documents)
    return jsonify(result)

'''
Match arrays containing all specified elements
'''
# Get documents using tag name 
# Get documents with the tag of appendix and missing content
@app.route('/get_appendix_missingContent_tag', methods=['GET'])
def get_appendix_missingContent_tag():
    documents = collection.find(
        {"Tags.name": {"$all": ["appendix", "missing content"]}},
    )
    result = []
    for document in documents:
        document["_id"] = str(document["_id"])
        result.append(document)
    return jsonify(result)

'''
Iterating over result sets
'''
# Get documents from 15/01/2024 onwards 
@app.route('/get_doc_15th_onwards', methods=['GET'])
def get_doc_15th_onwards():
    document_finder = collection.find({"Date": {"$gte": "20/01/2024"}}) 
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
    return jsonify(result)

'''
Query embedded documents and arrays
'''
# Get reviewers by their role
# Get reviewers with the role of editor
@app.route('/get_editor_reviewers', methods=['GET'])
def get_editor_reviewers():
    editor_reviewers = collection.find({"Reviewer Details.role": {"$regex": "^editor$", "$options": "i"}})
    result = [{"Reviewer Details": r_editor["Reviewer Details"]} for r_editor in editor_reviewers]
    return jsonify(result)

'''
Match elements in arrays with criteria
'''
# Get documents by their importance 
# Get documents with the tag of importance of 4 and over
@app.route('/get_important_technical_tag', methods=['GET'])
def get_important_technical_tag():
    documents = collection.find({
        "Tags": {"$elemMatch": {
            "category": "technical",
            "importance": {"$gte": 4}
        }}
    })
    result = []
    for document in documents:
        document["_id"] = str(document["_id"]) # Converts MongoDB ObjectID to a string
        # Code to only include tags with importance that is equal or more than 4
        filter_tags = []
        for tag in document["Tags"]:
            if tag["category"] == "technical" and tag["importance"] >= 4:
                filter_tags.append(tag)
        document["Tags"] = filter_tags # Updates the document with correct tag data
        result.append(document)
    return jsonify(result)

'''
Match arrays with all elements specified
'''
# Get all documents that has the tag information specified
@app.route('/get_specified_tag', methods=['GET'])
def get_specified_tag():
    documents = collection.find({"Tags":[
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

# "Perform text search"
# Get all status pending documents
'''
@app.route('/get_status_pending', methods=['GET'])
def get_status_pending():
    status_pending = collection.find({"\"$text": {"\"$search": "\"Fundamental flaws in methodology have been noted\""}})
    result = []
    for document in status_pending:
        document["_id"] = str(document["_id"])
        result.append(document)
    return jsonify(result)
'''
'''
collection.create_index([
    ("Comment", "text"),
    ("Category", "text")
    ("Additional notes", "text")
    ("Suggested action", "text")
])
@app.route('/search', methods=['GET'])
def text_search():
    search_text = request.args.get('query', '')
    try:
        results = collection.find(
            {"$text": {"$search": text_search}},
        )
    except Exception as err:
        return jsonify({"Error": str(err)}, 500)

'''



'''
Transformations
'''
# Analyse severity and impact
@app.route('/severity_impact', methods=['GET'])
def severity_impact_analysis():
    try:
        pipeline = [
            # Group by severity and impact
            {"$group": {
                "_id": {
                    "severity": "$Severity",
                    "impact": "$Impact"
                },
                # Issues
                "total_issues": {"$sum": 1},
                "resolved_counter": {"$sum": {"$cond": ["$Resolved", 1, 0]}},
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
            "unwound_tags": result
            })
    except Exception as err:
        return jsonify({"Error": str(err)}), 500
'''
MapReduce
'''
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
            {"$sort": {"total_issues": -1}},
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
# Update documents with priority to critical if severity is high and impact is major
@app.route('/update_priority', methods=['GET', 'PUT'])
def update_priority2():
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
                "modified_count": result.modified_count,
                "modified_documents": json.loads(dumps(updated_documents))
            })

        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    # Handle GET request
    return jsonify({"message": "Please use PUT method to update priorities"})

if __name__ == '__main__':
    app.run(debug=True, port=2000)