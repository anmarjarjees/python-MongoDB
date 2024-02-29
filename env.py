# This file contains our secret keys to connect to MongoDB ATLAS:
# we have to add it to gitignore for GitHub ONLY but not for Heroku
import os

# we will use Atlas:
# The code we copied from MongoDB:
# mongodb+srv://root:<password>@myfirstcluster.XXXXX.mongodb.net/<dbname>?retryWrites=true&w=majority
os.environ.setdefault("CONN_URL","mongodb+srv://root:<password>@myfirstcluster.XXXXX.mongodb.net/<dbname>?retryWrites=true&w=majority")