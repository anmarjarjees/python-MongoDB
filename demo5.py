import pymongo

# To make easy, we created a variable just to save the url:
# whether to connect to local DB or Atlas DB, you can just change the value of this variable

# This is the only line you will change:
# localhost => mongodb://localhost:27017
# atlas db => mongodb+srv://root:<password>@myfirstcluster.XXXXX.mongodb.net/<dbname>?retryWrites=true&w=majority

# NOTE:
# Whether you want to use the Atlas DB or Local one the code is EXACTLY the same
# Only change the connection string!
db_url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(db_url)

# We need to get the database name + the collection name
# We can use CONSTANTS as LMS or use this way below:
# in my local PC, the database name is "aj-demo"
database = client["aj-demo"] # to access our existing database named "aj-demo"
# in my local PC, the collection name is "students"
collection = database["students"] # to access our existing collection named "students"

# the find command: db.students.find({}) OR db.students.find()
students = collection.find({}) # OR .find()
print(students) # <pymongo.cursor.Cursor object at 0x03844730>

for student in students:
    print(student) # {'_id': ObjectId('5eea88ee637b49102b68c7a5'), 'name': 'Martin', 'program': 'FSSD', 'average': 84.0}

# **********************
# Insert a new document:
# **********************

# All in one line
# collection.insert_one({ "name": "Kate Willson", "program":"fssd", "average": 82 })

# Or using two lines:
# Creating a new document (new object) and insert this document to our collection
# We will insert a new document (record) then comment this code after 
# because we will also learn how insert more than one document (multiple records):
# Mongo Shell: db.students.insert({ "name": " Alex Chow", "program":"FSSD","average":84 })
new_doc = { "name": "Kate Willson", "program":"FSSD","average":82 }

# then using insert_one method:
# insert is deprecated. Use insert_one or insert_many instead.
collection.insert_one(new_doc)

# With W3Schools:
# To insert a record, or document as it is called in MongoDB, into a collection,
# We use the insert_one() method
# The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert.

# Then try inserting more than one record (inserting many documents/objects):
# First, comment the code for creating and inserting one document to try the following:
# To do this, we're going to create a variable called new_docs.
# We send an array of dictionaries.
# review: my_list = [ element1, element2, element3]
# The following array "new_docs" has 3 elements
new_docs = [
{
 "first":"alexa","last":"chow",
 "dob":"19/09/1984",
 "gender":"f",
 "hair_colour":"black",
 "occupation":"designer",
 "nationality":"American"
},
{
 "first":"george",
 "last":"martin",
 "dob":"19/09/1974",
 "gender":"m",
 "hair_colour":"black",
 "occupation":"programmer",
 "nationality":"American"
},
{
 "first":"Sarah","last":"Grayson",
 "dob":"19/09/1977",
 "gender":"f",
 "hair_colour":"brown",
 "occupation":"dba",
 "nationality":"Italian"
}
# ,
# {
#     "car":"Honda",
#     "Year":"2010",
#     "Model":"SUV",
#     "KM":123123
# }
]

# We use the insert_many() method.
# it'll send new_docs.
# instead of insert, it's now insert many.
collection.insert_many(new_docs)

for student in students:
    print(student)