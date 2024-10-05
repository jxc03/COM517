<h1 align="center">
    Week 2 - PyMongo Tasks
</h1>

<p>
    Tasks aimed to be fimiliar with MongoDB and PyMongo. The tasks start from basic CRUD operations and progressively goes through slightly more advanced operations to support understanding of non-relational database development using MongoDB. Tasks should be completed using Jupyter notebook.
</p>

## Tasks 
**T1**<br>
Install PyMongo

```python
pip install pymongo
```

**T2**<br>
Use the PyMongo library to connect to a running MongoDB instance.

```python
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
```

**T3**<br>
Create a new database named ‘student_records’ using the PyMongo client.

```python
db = client.student_records
```

**T4**<br>
Within the ‘student_records’ database, create a collection called ‘students’.

```python
students = db.students
```

**T5**<br>
Insert a single document into the ‘students’ collection. The document should have fields for the student’s ‘name’, ‘age’, and ‘major’.

```python
student = {"name": "Johnathan Casino", "age": 22, "major": "Computing Technologies"}
students.insert_one(student)
```
```
InsertOneResult(ObjectId('67001d845903fe95c70a2f21'), acknowledged=True)
```

**T6**<br>
Insert multiple student documents into the ‘students’ collection at once. Use the ‘insert_many()’ function.

```python
new_students = [
    {"name": "Jake Smith", "age": 21, "major": "Computer Science"},
    {"name": "mike Tyson", "age": 23, "major": "Software Engineer"}
]
students.insert_many(new_students)
```
```
InsertManyResult([ObjectId('670024e85903fe95c70a2f22'), ObjectId('670024e85903fe95c70a2f23')], acknowledged=True)
```

**T7**<br>
Use the ‘find_one()’ method to retrieve a student document where the ‘name‘ is ‘Johnathan Casino‘.

```python
student = students.find_one( {"name": "Johnathan Casino"} )
print(student)
```
```
{'_id': ObjectId('67001d845903fe95c70a2f21'), 'name': 'Johnathan Casino', 'age': 22, 'major': 'Computing Technologies'}
```

**T8**<br>
Use the ‘find()’ method to retrieve and print all student documents in the collection.

```python
for student in students.find():
    print(student)
```
```
{'_id': ObjectId('67001d845903fe95c70a2f21'), 'name': 'Johnathan Casino', 'age': 22, 'major': 'Computing Technologies'}
{'_id': ObjectId('670024e85903fe95c70a2f22'), 'name': 'Jake Smith', 'age': 21, 'major': 'Computer Science'}
{'_id': ObjectId('670024e85903fe95c70a2f23'), 'name': 'mike Tyson', 'age': 23, 'major': 'Software Engineer'}
```

**T9**<br>
Query the ‘students’ collection to find all students who are over 21 years old.

```python
for student in students.find( {"age": {"$gt": 21} } ):
    print(student)
```
```
{'_id': ObjectId('67001d845903fe95c70a2f21'), 'name': 'Johnathan Casino', 'age': 22, 'major': 'Computing Technologies'}
{'_id': ObjectId('670024e85903fe95c70a2f23'), 'name': 'mike Tyson', 'age': 23, 'major': 'Software Engineer'}
```

**T10**<br>
Update the ‘major’ field of ‘Jake Smith’ from ‘Computer Science’ to ‘Data Science‘.

```python
students.update_one(
    {"name": "Jake Smith"},
    {"$set": {"major": "Data Science" } }
)
```
```
UpdateResult({'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}, acknowledged=True)
```

**T11**<br>
Add a new field “graduation_year” for Johnathan Casino and set it to 2025.

```python
students.update_one(
    {"name": "Johnathan Casino"},
    {"$set": {"graduation_year": 2025 } }
)
```
```
UpdateResult({'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}, acknowledged=True)
```

**T12**<br>
Delete a document where the ‘name‘ is ‘Mike Tyson‘.

```python
students.delete_one( {"name": "Mike Tyson"} )
```
```
DeleteResult({'n': 1, 'ok': 1.0}, acknowledged=True)XX
```

**T13**<br>
Insert a list of multiple student documents into the ‘students’ collection using bulk inserts.

```python
bulk_students = [
    {"name": "Alice Brown", "age": 24, "major": "Chemistry"},
    {"name": "Bobby White", "age": 23, "major": "Biology"}
]
students.insert_many(bulk_students)
```
```
InsertManyResult([ObjectId('670170f4d47536432a6150f5'), ObjectId('670170f4d47536432a6150f6')], acknowledged=True)
```

**T14**<br>
Count the total number of student documents in the ‘students’ collection.

#Numbers are different since I've came back to it on another day

```python
student_count = students.count_documents({})
print(student_count)
```
```
2
```

**T15**<br>
Retrieve all students who are younger than 23 years old.

```python
for student in students.find( {"age": {"$lt": 23} } ):
    print(student)
```
```
{'_id': ObjectId('67017461d47536432a6150f9'), 'name': 'Jake Smith', 'age': 21, 'major': 'Computer Science'}
```

**T16**<br>
Sort the students by age in ascending order and print them.

```python
for student in students.find().sort("age", 1):
    print(student)
```
```
{'_id': ObjectId('67017461d47536432a6150f9'), 'name': 'Jake Smith', 'age': 21, 'major': 'Computer Science'}
{'_id': ObjectId('670170f4d47536432a6150f6'), 'name': 'Bobby White', 'age': 23, 'major': 'Biology'}
{'_id': ObjectId('67017461d47536432a6150fa'), 'name': 'Mike Tyson', 'age': 23, 'major': 'Software Engineer'}
{'_id': ObjectId('670170f4d47536432a6150f5'), 'name': 'Alice Brown', 'age': 24, 'major': 'Chemistry'}

```

**T17**<br>
Create an index on the ‘name’ field to improve search performance.

```python
students.create_index( [("name", 1)] )
```
```
'name_1'
```

**T18**<br>
Query the ‘students’ collection using the indexed ‘name‘ field to find ‘Alice Brown‘.

```python
student = students.find_one( {"name": "Alice Brown"} )
print(student)
```
```
{'_id': ObjectId('670170f4d47536432a6150f5'), 'name': 'Alice Brown', 'age': 24, 'major': 'Chemistry'}
```

**T19**<br>
Drop the ‘students’ collection from the ‘student_records‘ database.

```python
students.drop()
```

**T20**<br>
Export the student records to a CSV file using Pythons ‘csv’ module.

```python
import csv

with open("students.csv", mode = "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow( ["Name", "Age", "Major"] )

    for studnet in students.find():
        writer.writerow( [student["name"], student["age"], student["major"]] )
```

**T21**<br>
May need to update multiple documents in the future that match a specific query. Use update_many() to update the major field for all students who are majoring in "Physics" to "Astrophysics".

```python
students.update_many(
    {"major": "Physics"},
    {"$set": {"major": "Astrophysics"} } 
)
```

**T22**<br>
How to delete multiple documents from a collection. Delete all student documents where the major is "Mathematics".

```python
students.delete_many( {"major": "Mathamatics"} )
```

**T23**<br>
Querying documents with specific fields. Modify your query to return only the name and age fields of students.

```python
for student in students.find({}, {"name": 1, "age": 1, "_id": 0} ):
    print(student)
```

**T24**<br>
You may want to check if a document exists in the collection without retrieving the whole document. Use find_one() to check if a student named "Alice Brown" exists in the collection.

```python
student_exists = students.find_one( {"name": "Alice Brown"} )
if student_exists:
    print("Student found")
else:
    print("Student not found")
```

**T25**<br>
You may need to count how many documents match a specific condition. Count how many students are aged 21 or older.

```python
count = students.count_documents( {"age": {"gte": 21}} )
print(f"Number of students aged 21 or older: {count}")
```

**T26**<br>
Query for documents where a specific field either exists or does not exist. Find all students that do not have the field graduation_year.

```python
for student in students.find( {"graduation_year": {"$exists": False}} ):
    print(student)
```

**T27**<br>
Increment a field value in MongoDB using the $inc operator. Increase the age of all students by 1.

```python
students.update_many( {}, {"$inc": {"age": 1}} )
```

**T28**<br>
Query for documents where a specific field either exists or does not exist. Find all students that do not have the field graduation_year.

```python
for student in students.find().sort("age", -1):
    print(student)
```

**T29**<br>
Use find_one_and_update() to find a document and modify it in one operation. Find a student named "John Smith" and update his age to 25.

```python
updated_student = students.find_one_and_update(
    {"name": "John Smith"},
    {"$set": {"age": 25}},
    return_document = True
)
print(updated_student)
```

**T30**<br>
You may want to limit the number of results returned by a query. Retrieve only the first 2 students in the collection.

```python
for student in students.find().limit(2):
    print(student)
```
