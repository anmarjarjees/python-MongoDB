# demo01-local.py: 
# to connect our current Application to our MongoDB local server
import pymongo
# If the above code was executed with no errors, 
# "pymongo" is installed and ready to be used.
# We need to make sure that we have the server mongodb running:
# run the command: mongod ==> if you want to connect to your local database 

# the address for mongod server is the localhost: 127.0.0.1
# you will need to know your port: 27017

# We need to initialize mongodb client:
# client has access to all the databases in the mongodb server
# we will use the database: "aj-demo" 

# Initial Steps to do either with shell or compass:
# you can create a new one YourInitial-demo if you want
# add a collection (like a table in MySQL) "students" with these fields with any values you like:
# name: "martin"
# program: "fssd"
# average: 84

# By default, we all have the same local connection:
client = pymongo.MongoClient("mongodb://localhost:27017/")
# For more info: https://www.w3schools.com/python/python_mongodb_create_db.asp

# for testing:
# print(client)
# output: MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)

# ********************************
# Error: Unable to import mongodb
# ********************************
# The solution based on MS VScode docs:
# In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). 
# Then select the Python: Select Interpreter command:
# The command presents a list of available interpreters 
# that VS Code can locate automatically (your list will vary)
# From the list, select the virtual environment in your project folder 
# that starts with ./env or .\env:
# for more info:
# https://code.visualstudio.com/docs/python/tutorial-flask
# ************************************************************************************************ 

# Important: In MongoDB, a database is not created until it gets content!
# Using this database
database = client['aj-demo']

# calling this specific collection named "students":
collection = database['students']

# db.students.find({}) OR db.students.find() <= the command we used with mongo shell
# instead of using db.students => we can just call our variable collection
# collection (simple python variable) will be our object to access the CRUD operations
students = collection.find({}) # OR students = collection.find() 

# For testing:
# the code below will not print the students as we expect (remember with MySQL)!
# print(students) 
# the output will be:  <pymongo.cursor.Cursor object at 0x038C7208> !!!!
# which is the object in this memory address 0x0325B9E8
# so students will act as the cursor as we had before in MySQL-Python

# so the same as before, we need to use for:
for student in students:
    print(student)

# The result:
# {'_id': ObjectId('5ff487d0ab2204745e0f6fe2'), 'name': 'martin smith', 'program': 'fssd', 'average': '88'}
# {'_id': ObjectId('5ff4884eab2204745e0f6fe3'), 'name': 'Alex Chow', 'program': 'fssd', 'average': '87'}
# {'_id': ObjectId('5ff48881ab2204745e0f6fe4'), 'name': 'Sarah Clarkson', 'program': 'DMWD', 'average': '91'} 

# Checking if a database exist:
# To view all the databases, you can check if a database exist by listing all databases in your system:
print (client.list_database_names())
# The output (depending on how many databases you have created):
# ['PyDB-Project', 'abc-school', 'admin', 'aj-demo', 'config', 'finalDB', 'just-tryDB', 'learn-mongodb', 'local', 'mpy-project', 'test', 'thorin-companyDB']