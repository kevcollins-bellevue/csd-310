# TITLE: pytech_delete.py
# AUTHOR: Kevin Collins
# DATE: 2023-07-09
# DESCRIPTION: Add and delete document from MongoDB database

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

# elmo jones document
elmo_jones = {
    "student_id": "1010",
    "first_name": "Elmo",
    "last_name": "Jones",
    "enrollment": [
        {
            "term": "2020-Summer",
            "gpa": "4.0",
            "start_date": "2020-06-01",
            "end_date": "2020-08-15",
            "course": [
                {
                    "course_id": "ENGL-100_2020-Summer",
                    "description": "Writing Composition 1",
                    "instructor": "James Jones, PhD",
                    "grade": "A"
                },
                {
                    "course_id": "MATH-120_2020-Summer",
                    "description": "College Algebra",
                    "instructor": "Susan Smith, MSc",
                    "grade": "A"
                }
            ]
        }
    ]
}

# Insert elmo_jones and output document_id
print("\n-- INSERT STATEMENTS --")
elmo_jones_student_id = students.insert_one(elmo_jones).inserted_id
print(f"Inserted student record into the students collection with document_id {elmo_jones_student_id}")

# Find student_id 1010 and display output
student_id_1010 = students.find_one({"student_id": "1010"})
print("\n-- DISPLAYING STUDENT TEST DOC --")
print("Student ID: " + student_id_1010["student_id"] + "\nFirst Name: " + student_id_1010["first_name"] + "\nLast Name: " + student_id_1010["last_name"] + "\n")

# Delete elmo jones document
deleted_elmo_jones = students.delete_one({"student_id": "1010"})

# Find all students in collection
students_list = students.find({})

# Display find header
print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop for all documents in collection and display student id, first name, and last name 
for document in students_list:
    print("Student ID: " + document["student_id"] + "\nFirst Name: " + document["first_name"] + "\nLast Name: " + document["last_name"] + "\n")

# Exit program 
input("\nEnd of program, press any key to exit...")
