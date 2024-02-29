import os
import pymongo

if os.path.exists("env.py"):
    import env

# We can also use a CONSTANT:
MONGO_CONN = os.environ.get("CONN_URL")

# Important: In MongoDB, a database is not created until it gets content!
# Using this database as CONSTANT
DBS_NAME = "ajTestDB" # with double quotes  # <== Please change this database name with yours

# calling this collection and save it into a constant:
COLLECTION_NAME = 'myFirstMDB' # with single quote

# Python constants are all written in Capital Letters with _ 

# we will code it with Py function using try/except block:
# define a function that will take one argument: url (from atlas connect link)
def mongo_connect(url):
    try:
        # my code for trying to connect
        conn = pymongo.MongoClient(url) # the major line
        print("MongoDB is connected")
        # if it's connected then return the connection object
        return conn
    
    # The "except" code below is for exception if PyMongo is not connected, 
    # throws an error with connection failure only
    # Below we used ex for exception but it could be any other name you like:
    except pymongo.errors.ConnectionFailure as ex:
        # print("Could not connect to the MongoDB:", ex)
        # Or we can use the string format that we used with MySQL with %s
        # two % one for the placeholder %s and another one for the variable %ex
        print ("Could not connect to the MongoDB: %s") %ex

# let's call our function for the connection:
client = mongo_connect(MONGO_CONN) # conn will contain the MongoClient url
print(client) # will print the object details

# Set our collection by passing the database name and the collection name:
collection = client[DBS_NAME][COLLECTION_NAME]

print(collection)

# Let's try to print:
# Very similar to how we did from the command line, we'll do coll.find.
# We'll call the find() method. That will be returned in documents.
documents = collection.find({}) # or you can just type .find()

# notice that documents will be a MongoDB object 
# So to iterate through that, we'll do for doc in document
for doc in documents:
    print (doc)