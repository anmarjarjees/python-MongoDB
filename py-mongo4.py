import pymongo

db_url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(db_url)

database = client["PyDB-Project"] # this line for creating a new db or using an existing one

# Step2: Since we got the database, now we can get the wanted collection inside this database
collection = database["employees"] # this line for creating a new collection or using an existing one
# Important: In MongoDB, a collection is not created until it gets content!

def show_menu():
    print("")
    print("1. Add a record")
    print("2. View a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    user_option = input("Enter option number: ")
    return user_option

# Creating our helper function to be used with the actual CRUD function for Reading a record
# We need to use/call this function to accomplish the following tasks:
# view records
# edit records
# delete records 
# All these listed functions are going to be called based on first name and last name
# We want to get the first name again and the last name
# Based on the function name:
# the following function is just for getting and returning a record (document)
def get_record():
    # Let's try to grab the wanted record based on the first and last name keys (fields)
    # Because in our main menu we have the option: 
    # - To find a record by "name"
    # Also we have the following 2 options will be based on the first and last names:
    # - To edit a record 
    # - To delete a record 
    print("") # just to have a space 
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")

    try:
        # in mongo shell, we can write this command to find a record based on the first_name key:
        # assuming that our collection is "users"
        # db.users.find ( {first_name: "Alex"} )
        # we will use find_one() method instead of find():
        # find_one() method returns ONLY the first occurrence in the selection.
        # we need to find the required document (record) 
        # based on the values of the two keys: "first" and "last"
        # Remember: document in MongoDB is like record in MySQL
        document=collection.find_one({'first':first.lower(), 'last':last.lower()})
        
        # for testing (It worked fine, we can comment the print line)
        # print (document) # will be printed as a JSON object
      
     # The except block lets you handle the error.
    except:
        print("Error accessing the database")
    
    # So what happens if no document is returned? 
    # if the record that we're looking for is not found!
    # then an empty variable will be returned, an empty object
    # If it's empty (document variable is empty), if there is nothing in there:
    # We want to print a warning/error message to the user
    if not document: # we are just saying if doc has no value (has nothing)
        # then we're going to print another blank line 
        print("")
        # and then say "Error! No results found"
        print("Error! No results found.")
   
    # And then after that, we're going to return our document object
    # It may be empty, or it may have results in it
    # in both cases, we will return the document
    # but we will have an error message above to tell us.
    return document # we will return document whether a record is found or not found


# Our first function for CRUD:
def add_record(): 
    print("") # just to have a space 
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")
    dob = input("Enter the date of birth: ")
    gender = input("Enter the gender: ")
    hair_colour = input("Enter the hair colour: ")
    occupation = input("Enter the occupation: ")
    nationality = input("Enter the nationality: ")

    # Now we can start building our dictionary to insert into the database.
    # in our life we use dictionary to search for the meaning of English word in an other language
    # The searched keyword is the key and the meaning could be the value
    # dictionary: Key and its value ==> the key is "first" and it's value is "alex"
    # NOTE: We want the first and the last name to be stored in the database in lowercase, 
    # which will make it much easier for us to find later.
    new_doc = { 
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender":gender.lower(),
        "hair_colour":hair_colour.lower(),
        "occupation": occupation.lower(),
        "nationality":nationality.lower()
    }

    # To be on the safe side, we'll create try except block:
    # it means we can try to insert the new record
    # if something goes wrong we can have an exception for the error that we might have 
    # In JS we have the same concept also called: try catch block

    # Check this link: https://www.w3schools.com/python/python_try_except.asp
    # The try block lets you test a block of code for errors.
    try:
        collection.insert_one(new_doc)
        print("")
        print("Document inserted")
    
     # The except block lets you handle the error.
    except:
        print("Error accessing the database")

# Our second function for CRUD:
# Read functionality:
# The function is named view record
# It's for displaying the record nicely in the terminal window
# Because the find steps are written inside get_record()
# We will call the function get_record() inside the function view_record()
def view_record():
   # We need to grab the record from the database first then we can view it later:
   # Define a variable, which gets the result (the returned record) of our get_record() function
   # get_record() our helper function to actually find (grab) the information
   # doc below is the python variable that will receive the returned document from get_record() function
   doc = get_record()

   # For testing: printing the doc variable:
   if doc: # if we do have some results we will continue with printing the full record
    # for testing
    # print (doc)
    # we need to use for loop to iterate through each "key" an "value" in this object:
    # we're calling the items() method here to step through each individual value in our dictionary (which the key and its value)
    # Notice that the items() method belongs to the document (record) object

    # for testing:
    # print (doc.items())
    # dict_items(
    # [
    # ('_id', ObjectId('5efdf06250fd0cea9d47486c')), 
    # ('first', 'martin'), ('last', 'smith'), 
    # ('dob', '2000-07-02'), ('gender', 'm'), 
    # ('hair_colour', 'yellow'), 
    # ('occupation', 'ceo'), ('nationality', 'amrican')
    # ])

    # Example (W3Schools)
    # Loop through both keys and values, by using the items() method/function:
    # for x, y in thisdict.items():
    # print(x, y)
    # To read more: https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp
       for key, value in doc.items():
            # As we know, MongoDB generates an "_id" field 
            # which is default key that is created by MongoDB and it contains a long complex value
            # That's why we don't want to display the "_id" field to the user
            # In this loop we need to display all the keys and their values
            # except the id key and its complex value (We don't want them)
            # So the first thing we want to check is: if the key is not equal to ID
            if key!="_id":
                # Remember that we saved and shorted our data in lowercase
                # But we need to display them in a nice format with capitalizing the first characters
                # Example: instead of displaying first: martin => we want to have First: Martin
                # We will put the capitalize method on it, so that we get the first letter capitalized.
                # Plus a colon.
                # And then plus the value again with the first letter capitalized.
                # Display them as Key: Value
                # The capitalize() method returns a string 
                # where the first character is upper case.
                # Note: Please remember that:
                # The + sign in Python for concatenating is NOT the same + sign in JS for concatenating
                # In JS we can concatenate string with numeric values using the + sign
                # In Python language we can concatenate string with string using the + sign
                # So in Python to concatenate string (text) and numbers, we can use the , sign
                
                # Very Important Note:
                # for my extra exercise (the micro project):
                # You have one of the values which salary in numeric datatype
                # Using capitalize() with numeric will generate an error
                # you will need to check first if the value is string then run capitalize()
                # The solution is by using isinstance() function:
                # The isinstance() function returns True if the specified object is of the specified type, 
                # otherwise False.
                # If the type parameter is a tuple, 
                # this function will return True if the object is one of the types in the tuple.
                # print(type(value))
                # for more details: https://www.w3schools.com/python/ref_func_isinstance.asp
                if (isinstance(value,str)):
                    print(key.capitalize(),": ", value.capitalize())    
                else:
                    print(key.capitalize(),": ", value)   
                # You can try this task if you like:
                # To make our code more secured (avoiding any errors) it work with any value:
                # if (the current value in not a number) then print(key.capitalize()+": "+ value.capitalize())  
                # else print  print(key.capitalize()+": "+ value)  

def main_loop():   
    while True: # It will be always true to keep running the while loop:        
        option = show_menu() # here is the line for activating/calling our our function show_menu()
        if option == "1":
            # You will print a nice short message to confirm the user selected option
            print("You have selected option 1 for adding a new record")
            # Then call a function to add a new record to the database
            add_record()
            # Yes, we can write our full code to insert a record here
            # but using functions make our code more concise and easier to read / debug
        elif option == "2":
            print("You have selected option 2 for viewing a record")
            view_record() 
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            # We should close our connection with MongoDB first:
            client.close()
            # Then we can exit the while loop and the entire application
            break
        else:
            print("Invalid Option!")

# 2: Call our function main_loop()
main_loop()