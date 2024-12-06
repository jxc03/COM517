
# Show all documents
@app.route('/show_all', methods=['GET'])
def show_all():
    '''
    all_documents = collection.find({})
    documents_list = []
    for documents in all_documents:
        documents["_id"] = str(documents["_id"]) 
        documents_list.append(documents)
    return jsonify(documents_list), 200

    https://www.mongodb.com/docs/languages/python/pymongo-driver/current/read/retrieve/?msockid=20511825578569d936200d1856b9683a
    https://www.w3schools.com/python/python_mongodb_find.asp
    https://www.slingacademy.com/article/pymongo-how-to-convert-objectid-to-string-and-vice-versa/
    '''

   # all_documents = #collection.find({})
    #documents = [{**document, "_id": str(document["_id"])} for document in all_documents]
    return #jsonify(documents), 200
    '''
    https://geekflare.com/python-unpacking-operators/
    https://docs.python.org/3/tutorial/controlflow.html#index-4
    '''
