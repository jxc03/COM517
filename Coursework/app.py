from flask import Flask, request, jsonify
from pymongo import MongoClient
import json
from bson.json_util import loads, dumps

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
# Get documents with the tag of importance of 
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
@app.route('/get_status_pending', methods=['GET'])
def get_status_pending():
    status_pending = collection.find({"\"$text": {"\"$search": "\"Fundamental flaws in methodology have been noted\""}})
    result = []
    for document in status_pending:
        document["_id"] = str(document["_id"])
        result.append(document)
    return jsonify(result)

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
Transformations
'''
# Update 


'''
@app.route('/reviewer-analytics', methods=['GET'])
def reviewer_analytics():
    pipeline = [
        {
            '$addFields': {
                'parsedResolutionDate': {
                    '$dateFromString': {
                        'dateString': '$Resolution Date',
                        'format': '%d/%m/%Y'
                    }
                },
                'parsedDate': {
                    '$dateFromString': {
                        'dateString': '$Date',
                        'format': '%d/%m/%Y'
                    }
                }
            }
        },
        {
            '$project': {
                '_id': 0,
                'reviewerInfo': {
                    'reviewerId': '$Reviewer ID',
                    'name': '$Reviewer Details.name',
                    'role': '$Reviewer Details.role'
                },
                'issueMetrics': {
                    'category': '$Category',
                    'severity': '$Severity',
                    'daysToResolve': {
                        '$cond': {
                            'if': '$Resolved',
                            'then': {
                                '$toString': {
                                    '$round': [
                                        {'$divide': [
                                            {'$subtract': ['$parsedResolutionDate', '$parsedDate']},
                                            (1000 * 60 * 60 * 24)
                                        ]}, 
                                        1
                                    ]
                                }
                            },
                            'else': None
                        }
                    }
                },
                'tagAnalysis': {
                    '$map': {
                        'input': '$Tags',
                        'as': 'tag',
                        'in': {
                            'tagName': '$$tag.name',
                            'importanceLevel': '$$tag.importance',
                            'categoryType': '$$tag.category'
                        }
                    }
                },
                'status': '$Status',
                'impact': '$Impact',
                'additionalNotes': '$Additional Notes'
            }
        },
        {
            '$sort': {
                'issueMetrics.severity': -1,
                'status': 1
            }
        }
    ]
    
    results = list(collection.aggregate(pipeline))
    return jsonify(results)
'''

if __name__ == '__main__':
    app.run(debug=True, port=2000)