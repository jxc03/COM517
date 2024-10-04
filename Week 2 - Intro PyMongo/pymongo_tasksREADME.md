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
DeleteResult({'n': 1, 'ok': 1.0}, acknowledged=True)
```

**T10**<br>

```python
```
```
```

**T10**<br>

```python
```
```
```

**T10**<br>

```python
```
```
```