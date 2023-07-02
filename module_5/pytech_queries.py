# TITLE: pytech_queries.py
# AUTHOR: Kevin Collins
# DATE: 2023-07-02
# DESCRIPTION: Query the students collection 

# imports
from pymongo import MongoClient

# MongoDB application connection string
url = "mongodb+srv://admin:admin@cluster0.rg8d0ix.mongodb.net/?retryWrites=true&w=majority"

# Connect to cluster
client = MongoClient(url)

# Specify the pytech database
db = client.pytech

# Get studnets collection
students = db.students

# Find all students in collection
students_list = students.find({})

# Display find header
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop for all documents in collection and display student id, first name, and last name 
for document in students_list:
    print("Student ID: " + document["student_id"] + "\n  First Name: " + document["first_name"] + "\n  Last Name: " + document["last_name"] + "\n")

# Find one student in the collection
john_doe = students.find_one({"student_id": "1007"})

print("\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + john_doe["student_id"] + "\n  First Name: " + john_doe["first_name"] + "\n  Last Name: " + john_doe["last_name"] + "\n")

# Exit program 
input("\nEnd of program, press any key to exit...")