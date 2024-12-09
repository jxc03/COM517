import pytest
from flask import Flask
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from app import app

#python -m pytest test/test_app.py -v

# Fixture for test
@pytest.fixture
def test_client():
    app = Flask(__name__)
    app.testing = True
    with app.test_client() as client:
        yield client

# Database connection
@pytest.fixture
def db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['coursework_db']
    collection = db['categories']
    yield collection

# Test /show_all endpoint
def test_show_all(test_client, db):
    test_docs = [
        {"Category": "Method, Mathematics and Terminology", "Comment": "Test 1"},
        {"Category": "Appendix-related concerns", "Comment": "Test 2"}
    ]
    db.insert_many(test_docs)
    
    response = test_client.get('/show_all')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert all(isinstance(doc.get("_id"), str) for doc in data)

# Test /all_appendix endpoint
def test_all_appendix(test_client, db):
    test_docs = [
        {"Category": "Appendix-related concerns", "Comment": "App 1"},
        {"Category": "Other", "Comment": "Non-appendix"},
        {"Category": "Appendix-related concerns", "Comment": "App 2"}
    ]
    db.insert_many(test_docs)
    
    response = test_client.get('/all_appendix')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert all(doc["Category"] == "Appendix-related concerns" for doc in data)

# Test /all_MMT endpoint
def test_all_mmt(test_client, db):
    test_docs = [
        {"Category": "Method, Mathematics and Terminology", "Comment": "MMT 1"},
        {"Category": "Other", "Comment": "Non-MMT"},
        {"Category": "Method, Mathematics and Terminology", "Comment": "MMT 2"}
    ]
    db.insert_many(test_docs)
    
    response = test_client.get('/all_MMT')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert all(doc["Category"] == "Method, Mathematics and Terminology" for doc in data)
    
# Test /get_appendix endpoint
def test_get_appendix(test_client, db):
    test_doc = {
        "Category": "Method, Mathematics and Terminology",
        "Comment": "Test comment",
        "Date": "2024-01-01",
        "Severity": "High",
        "Priority": "High",
        "Suggested Action": "Review"
    }
    db.insert_one(test_doc)
    
    response = test_client.get('/get_appendix')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

# Test /get_mmt endpoint
def test_get_mmt(test_client, db):
    test_doc = {
        "Category": "Method, Mathematics and Terminology",
        "Comment": "Test comment",
        "Date": "2024-01-01",
        "Severity": "High",
        "Priority": "High",
        "Suggested Action": "Review"
    }
    db.insert_one(test_doc)
    
    response = test_client.get('/get_mmt')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

# Test /get_math_tags endpoint
def test_get_math_tags(test_client, db):
    test_docs = [
        {
            "Category": "MMT",
            "Tags": [{"name": "math"}],
            "Comment": "Math test",
            "Date": "2024-01-01",
            "Type": "Issue",
            "Severity": "High",
            "Priority": "High",
            "Suggested Action": "Review",
            "Status": "Open"
        },
        {
            "Category": "MMT",
            "Tags": [{"name": "other"}],
            "Comment": "Non-math test",
            "Date": "2024-01-01",
            "Type": "Issue",
            "Severity": "Low",
            "Priority": "Low",
            "Status": "Open"
        }
    ]
    db.insert_many(test_docs)
    
    response = test_client.get('/get_math_tags')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert any("math" in [tag["name"] for tag in doc["Tags"]] for doc in data)

# Test /get_mmt_severity_high endpoint
def test_get_mmt_severity_high(test_client, db):
    test_docs = [
        {
            "Tags": [{"name": "method"}],
            "Severity": "High",
            "Priority": "Critical"
        },
        {
            "Tags": [{"name": "method"}],
            "Severity": "Low",
            "Priority": "Low"
        }
    ]
    db.insert_many(test_docs)
    
    response = test_client.get('/get_mmt_severity_high')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

# Test /get_appendix_missingContent_tag endpoint
def test_get_appendix_missingContent_tag(test_client, db):
    test_docs = [
        {
            "Tags": [{"name": "appendix"}, {"name": "missing content"}],
            "Comment": "Should find this"
        },
        {
            "Tags": [{"name": "appendix"}],
            "Comment": "Should not find this"
        }
    ]
    db.insert_many(test_docs)
    
    response = test_client.get('/get_appendix_missingContent_tag')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1

# Test /get_doc_15th_onwards endpoint
def test_get_doc_15th_onwards(test_client, db):
    test_docs = [
        {
            "Date": "19/01/2024",
            "Comment": "Before cutoff",
            "Category": "Test",
            "Type": "Issue",
            "Severity": "Low",
            "Priority": "Low",
            "Status": "Open",
            "Tags": [],
            "Date Reviewed": "20/01/2024",
            "Reviewer ID": "TEST001",
            "Reviewer Details": {},
            "Resolved": False,
            "Resolution Date": "",
            "Additional Notes": "",
            "Impact": "Minor",
            "Suggested Action": "Review"
        },
        {
            "Date": "21/01/2024",
            "Comment": "After cutoff",
            "Category": "Test",
            "Type": "Issue",
            "Severity": "Low",
            "Priority": "Low",
            "Status": "Open",
            "Tags": [],
            "Date Reviewed": "22/01/2024",
            "Reviewer ID": "TEST002",
            "Reviewer Details": {},
            "Resolved": False,
            "Resolution Date": "",
            "Additional Notes": "",
            "Impact": "Minor",
            "Suggested Action": "Review"
        }
    ]
    db.insert_many(test_docs)
    
    response = test_client.get('/get_doc_15th_onwards')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert all(doc["Date"] >= "20/01/2024" for doc in data)

# Test /get_important_technical_tag endpoint
def test_get_important_technical_tag(test_client, db):
    test_docs = [
        {
            "Tags": [{
                "category": "technical",
                "importance": 5,
                "name": "test1"
            }]
        },
        {
            "Tags": [{
                "category": "technical",
                "importance": 3,
                "name": "test2"
            }]
        }
    ]
    db.insert_many(test_docs)
    
    response = test_client.get('/get_important_technical_tag')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

# Test /get_specified_tag endpoint
def test_get_specified_tag(test_client, db):
    test_doc = {
        "Tags": [
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
        ]
    }
    db.insert_one(test_doc)
    
    response = test_client.get('/get_specified_tag')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

#Test /update_priority endpoint
def test_update_priority(test_client, db):
    test_doc = {
        "Severity": "High",
        "Impact": "Major",
        "Resolved": False,
        "Priority": "Medium"
    }
    db.insert_one(test_doc)
    
    # Test GET method
    get_response = test_client.get('/update_priority')
    assert get_response.status_code == 200
    
    # Test PUT method
    put_response = test_client.put('/update_priority')
    assert put_response.status_code == 200
    data = put_response.get_json()
    assert isinstance(data, dict)
    assert "modified_count" in data
    
    # Verify database update
    updated_doc = db.find_one({"_id": test_doc["_id"]})
    if updated_doc:
        assert updated_doc["Priority"] == "Critical"
        assert "Last_Modified" in updated_doc
        assert "Update_History" in updated_doc