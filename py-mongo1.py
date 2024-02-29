import pymongo

# we can connect to our local or cloud database:
# This is the only line you will change:
# localhost => mongodb://localhost:27017
# atlas db => mongodb+srv://root:<password>@myfirstcluster.XXXXX.mongodb.net/<dbname>?retryWrites=true&w=majority
# Or using env.py steps
db_url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(db_url)

# We need to get these two things: database name + the collection name

# Step1: we have to get the database name first (access our database: PyDB-Project)
# mpy-project is short for MyPython-Project database
database = client["PyDB-Project"] # this line for creating a new db or using an existing one
# Important: In MongoDB, a database is not created until it gets content (at least one collection)!

# Step2: Since we got the database, now we can get the wanted collection inside this database
collection = database["employees"] # this line for creating a new collection or using an existing one
# Important: In MongoDB, a collection is not created until it gets content!

# To summarize: 
# 1. in order to create a database, we have to have a collection
# 2. in order to create a collection, we have to have at least one document inside this collection
# 3. We need to insert at least one document into our collection

# In order to examine our database and our collection, let's try to insert this document
doc = {
 "first":"allen",
 "last":"delon",
 "dob":"19/09/1972",
 "gender":"m",
 "hair_colour":"black",
 "occupation":"programmer",
 "nationality":"American"
}

collection.insert_one(doc)