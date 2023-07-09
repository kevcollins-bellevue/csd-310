# TITLE: pytech_update.py
# AUTHOR: Kevin Collins
# DATE: 2023-07-09
# DESCRIPTION: Update documents in Pytech database 

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
    print("Student ID: " + document["student_id"] + "\nFirst Name: " + document["first_name"] + "\nLast Name: " + document["last_name"] + "\n")

# update student_id 1007 last_name
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Hammerfist"}})

# Find student_id 1007
student_id_1007 = students.find_one({"student_id": "1007"})

# Display header for student_id 1007 find
print("\n-- DISPLAYING STUDENT DOCUMENT 1007 --")

# Display student_id 1007 find
print("Student ID: " + student_id_1007["student_id"] + "\nFirst Name: " + student_id_1007["first_name"] + "\nLast Name: " + student_id_1007["last_name"] + "\n")

# Exit program 
input("\nEnd of program, press any key to exit...")
