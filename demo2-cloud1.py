# demo01-cloud1.py: to connect our current Application to our Atlas Cloud Database
# This file has he same logic like demo01-local.py just with using the Cloud Atlas DB
# This file contains the standard way for connection based on W3Schools
# This file has a review about how to import a function/method from a package
# We can ignore this line because of the from command later:
# ***************
# import pymongo
# ***************

# if you add this line below (the same idea of your challenge1 with practical python module)
# you don't have to specify pymongo.MongoClient()
# you can just call the class: MongoClient to use its method (function) MongoClient()
from pymongo import MongoClient

# We need to initialize mongodb client:
# client has access to all the databases in the mongodb atlas server
# we will use Atlas:
# The code we copied from MongoDB Atlas by going to "Clusters" then "Connect" button:
# mongodb+srv://root:<password>@myfirstcluster.XXXXX.mongodb.net/<dbname>?retryWrites=true&w=majorit
# NOTE: You will have to modify these values:
# "myfirstcluster" is the default name, but we can change it also
# <password> for the root user (NOT the password to login to MongoDB)
# <dbname> the name of database that we need to use for this application
# XXXXX => this will be a unique code for each one
# mongodb+srv://root:<password>@myfirstcluster.-----.mongodb.net/<dbname>?retryWrites=true&w=majority
conn_url = "Please copy your own Atlas connection string here!"
client = MongoClient(conn_url) # NO NEED FOR: client = pymongo.MongoClient(conn_url)

# Using this database "aj-demo":
database = client['ajTestDB']
print (database)

# calling this collection "students":
# NOTE: remember that a collection in MongoDB is the same as a table in SQL databases.
# Notice "myFirstMDB" is just a collection
collection = database['myFirstMDB'] 
print (collection)

# In MongoDB we use the find() and findOne() [Later] methods to find data in a collection.
# Just like the SELECT statement is used to find data in a table in a MySQL database.

# Find One() Method:
# ******************
# To select data from a collection in MongoDB, we can use the find_one() method.
# The find_one() method returns the first occurrence in the selection.
# db.students.find({}) <= the command we used with mongo shell
# instead of using db.students => we can just call our variable collection:
documents=collection.find({}) # or just type .find()
# So: No parameters in the find() method gives you the same result as SELECT * in MySQL.

# the code below will not print the students as we expect (remember with MySQL)!
print (documents)    
# the output will be: <pymongo.cursor.Cursor object at 0x039CF3E8>
# which is the object in this memory address 0x0325B9E8
# so students will act as the cursor in MySQL-Python

# To view all the databases, you can check if a database exist by listing all databases in you system:
print (client.list_database_names())

# so the same as before, we need to use for:
for doc in documents:
    print(doc)