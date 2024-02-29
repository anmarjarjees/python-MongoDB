# demo01-cloud2.py: to connect our current Application to our Atlas Cloud Database
# Has the same job as demo01-cloud1.py 
# but it has some new lines (different way of coding) from LMS (Code Inst.)
import pymongo

# Important: In MongoDB, a database is not created until it gets content!
# Using this database as CONSTANT
DBS_NAME = "ajTestDB" # with double quotes  # <== Please change this database name with yours

# calling this collection and save it into a constant:
COLLECTION_NAME = 'myFirstMDB' # with single quote

# Python constants are all written in Capital Letters with _ 

# We need to initialize mongodb client:
# client has access to all the databases in the mongodb server
# we will use Atlas:
# The code we copied from MongoDB:
# mongodb+srv://root:<password>@myfirstcluster.XXXXX.mongodb.net/<dbname>?retryWrites=true&w=majority
conn_url = "Please copy your own Atlas connection string here!"
client = pymongo.MongoClient(conn_url)  # conn will contain the MongoClient url

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