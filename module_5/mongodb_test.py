# TITLE: mongodb_test.py
# AUTHOR: Kevin Collins
# DATE: 2023-07-02
# DESCRIPTION: Test for connecting to MongoDB Atlas collection - Displays collection names

# imports
from pymongo import MongoClient

# MongoDB application connection string
url = "mongodb+srv://admin:admin@cluster0.rg8d0ix.mongodb.net/?retryWrites=true&w=majority"

# Connect to cluster
client = MongoClient(url)

# Specify the pytech database
db = client.pytech

# Display collections
print('-- Pytech Collection List --')
print(db.list_collection_names())

# Exit program
input('\nEnd of program, press any key to exit...')