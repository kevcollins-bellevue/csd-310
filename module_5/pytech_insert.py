# TITLE: mongodb_test.py
# AUTHOR: Kevin Collins
# DATE: 2023-07-02
# DESCRIPTION: Insert three student documents to MongoDB Atlas database 

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

# John Doe document
john_doe = {
    "student_id": "1007",
    "first_name": "John",
    "last_name": "Doe",
    "enrollment": [
        {
            "term": "2020-Summer",
            "gpa": "2.5",
            "start_date": "2020-06-01",
            "end_date": "2020-08-15",
            "course": [
                {
                    "course_id": "ENGL-100_2020-Summer",
                    "description": "Writing Composition 1",
                    "instructor": "James Jones, PhD",
                    "grade": "B"
                },
                {
                    "course_id": "MATH-120_2020-Summer",
                    "description": "College Algebra",
                    "instructor": "Susan Smith, MSc",
                    "grade": "C"
                }
            ]
        }
    ]
}

# Hank Hill document
hank_hill = {
    "student_id": "1008",
    "first_name": "Hank",
    "last_name": "Hill",
    "enrollment": [
        {
            "term": "2020-Fall",
            "gpa": "3.67",
            "start_date": "2020-08-28",
            "end_date": "2020-11-16",
            "course": [
                {
                    "course_id": "FINA-110_2020-Fall",
                    "description": "Introduction to Personal Finance",
                    "instructor": "Wanda Wilson, MSc",
                    "grade": "A"
                },
                {
                    "course_id": "HUMS-240_2020-Fall",
                    "description": "Origins of Ancient Cultures",
                    "instructor": "James Jones, PhD",
                    "grade": "B"
                },
                {
                    "course_id": "ECON-130_2020-Fall",
                    "description": "Macroeconomics",
                    "instructor": "Paul Jackson, PhD",
                    "grade": "A"
                }
            ]
        }
    ]
}

# Bill Billops document
bill_billops = {
    "student_id": "1009",
    "first_name": "Bill",
    "last_name": "Billops",
    "enrollment": [
        {
            "term": "2020-Summer",
            "gpa": "3.67",
            "start_date": "2020-06-01",
            "end_date": "2020-08-15",
            "course": [
                {
                    "course_id": "FINA-210_2020-Summer",
                    "description": "Intro to Accounting",
                    "instructor": "William Wiley, MSc",
                    "grade": "A"
                },
                {
                    "course_id": "HUMS-260_2020-Summer",
                    "description": "Origins of Bronze Age Cultures",
                    "instructor": "Edward Planter, PhD",
                    "grade": "B"
                },
                {
                    "course_id": "ECON-140_2020-Summer",
                    "description": "Microeconomics",
                    "instructor": "Toby Toodle, PhD",
                    "grade": "c"
                }
            ]
        }
    ]
}

# Insert documents and output document ID
print("\n  -- INSERT STATEMENTS --")

john_doe_student_id = students.insert_one(john_doe).inserted_id
print(f"Inserted student record John Doe into the students collection with document_id {john_doe_student_id}")

hank_hill_student_id = students.insert_one(hank_hill).inserted_id
print(f"Inserted student record Hank Hill into the students collection with document_id {hank_hill_student_id}")

bill_billops_student_id = students.insert_one(bill_billops).inserted_id
print(f"Inserted student record Bill Billops into the students collection with document_id {bill_billops_student_id}")

# Exit program
input("\nEnd of program, press any key to exit...")