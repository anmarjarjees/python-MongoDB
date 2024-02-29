import pymongo

db_url = 'mongodb://localhost:27017' # you can place here your Atlas DB connection string
client = pymongo.MongoClient(db_url)

database = client["PyDB-Project"] # this line for creating a new db or using an existing one

collection = database["employees"] # this line for creating a new collection or using an existing one
# Important: In MongoDB, a collection is not created until it gets content!

def show_menu():
    # using doctype string below:
    """
    Return the user input as a string datatype
    """
    print("")
    print("1. Add a record")
    print("2. View a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    user_option = input("Enter option number: ")
    return user_option

# Helper Function
def get_record():
    """
    Return a document that contains the values of the first and last names
    """
    print("") # just to have a space 
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")

    try:
        # Finding (Select) one document based on the first and last keys (fields)
        document=collection.find_one({'first':first.lower(), 'last':last.lower()})      
    except:
        print("Error accessing the database")
    
    if not document: # we are just saying if doc has no value (has nothing)
        print("")
        print("Error! No results found.")
   
    return document # we will return document whether a record is found or not found


# Our first function for CRUD:
def add_record():
    """
    Insert a new record to our database
    """ 
    print("") # just to have a space 
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")
    dob = input("Enter the date of birth: ")
    gender = input("Enter the gender: ")
    hair_colour = input("Enter the hair colour: ")
    occupation = input("Enter the occupation: ")
    nationality = input("Enter the nationality: ")

    new_doc = { 
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender":gender.lower(),
        "hair_colour":hair_colour.lower(),
        "occupation": occupation.lower(),
        "nationality":nationality.lower()
    }

    try:
        collection.insert_one(new_doc)
        print("")
        print("Document inserted")
    
     # The except block lets you handle the error.
    except:
        print("Error accessing the database")

def view_record():
    """
    1. Print/Display the full document keys 
    2. Return the document that contains the full information (all keys and values)
    """
    doc = get_record()
    if doc: # if we do have some results we will continue with printing the full record
        for key, value in doc.items():
                if key!="_id":
                    if (isinstance(value,str)):
                        print(key.capitalize(),": ", value.capitalize())    
                    else:
                        print(key.capitalize(),": ", value)  
    
    # Very Important Note:
    # We had to modify this function by returning the doc info about the record we selected
    # For just viewing the record => return doc will be useless! But no problems
    # This return statement is needed inside delete_record()
    return doc

def delete_record():
    """
    Delete the full document based on the values of these two keys (fields): first and last
    """   
    doc=view_record() # receive the first and the last name
    print("")
    if doc:
        confirm = input("Is this the document you want to delete?\nY or N: ")
        print("")
        if confirm.lower()=='y':
            try:
                collection.delete_one(doc) # delete one document based on the first and last keys
                print("")
                print("Document deleted") 

            # The except block lets you handle the error.
            except:
                print("Error accessing the database or the current record")
        else:
            print("Document/record not deleted") 

def edit_record():
    """
    1. Print/Display the full document information that we want to modify
    2. Print/Display the full document after inserting the new values
    3. Update the document that contains the full information (all keys and values)
    """
    # the same logic, we need to select the record to modify by first and last keys (columns)    
    
    # We can view the full record by calling view_record()
    doc=view_record() # receive the first and the last name
    # Or we can get the user input for the first and last keys for the record to be deleted
    # doc=get_record()

    # check if there is something (any value) in doc // or if doc is True
    if doc:
        # We're going to create an empty dictionary called "update_doc"
        # In Python => dictionary => like in JS is just an empty object/JSON object
        update_doc = {} # to create a new empty document (it's just like an empty object in JS/JSON)
        # this "update_doc" is empty now 
        # but later it will contain the field(s) values that the user inserted/typed
        print("") # Just printing a blank line
        # Again, it's the same thing. We're going to iterate through doc items using k,v in doc.items:
        # and we're going to add values to that dictionary. 
        # We're going to build that as we go on to iterate through our keys and our values.
        
        # The layout/format example to format our output:
        # First [alex] : alexa
        # Last [chow] : 
        # Dob [1970-08-07] : 
        # Gender [m] : f
        # Hair_colour [black] : red
        # Occupation [teacher] : 
        # Nationality [canadian] : 
        # In the micro project we have the salary key which is should be numeric
        # Salary: Numeric value (int or float)
        for key, value in doc.items():
        # We also want to filter out the ID field. We don't want to be editing that.
            if key != "_id":
                # As we're iterating through the keys/values of the selected document
                # we're going to add values to our "update_doc" dictionary variable
                # And the values for each key is going to be equal to our input here: 
                # using input() method
                # We need the value to nicely appears in a square brackets to see it clearly:
                
                # We need our last check for the key "salary":
                # if the current key is "salary" we need to change the input into a numeric value 
                if key == "salary":
                    # we will comment this general input message:
                    # update_doc[key] = input("input your value: ").lower()
                
                    # The pattern/format: Key_name [ current_key_value ] : X
                    # Example:
                    # First [alex] : alexa
                    # Last [chow] :
                    # like JS: parseFloat(prompt("Enter your salary")) 
                    # Before calling the built-in function float()
                    # We do need to:
                    # 1. check if the user inserted a number 
                    # 2. calling the float() function
                    salary =input(f"{key} [{value}]: ") # 30 as number => "30" as string
                    # First: Check if the user input is valid
                    # Question: How can we check if the value of a variable is a number (is numeric)
                    # Python String isnumeric() Method
                    # https://www.w3schools.com/python/ref_string_isnumeric.asp
                    # object_name.isnumeric() 
                    # Example:
                    # txt = "565543"
                    # x = txt.isnumeric()
                    # print(x) => True
                    if (salary.isnumeric()):
                        update_doc[key] = float(salary)
                    else:
                        update_doc[key] = value 
                    
                else: # if the key is anything else other than "salary" => text field                   
                    update_doc[key] = input(f"{key} [{value}]: ").lower()
                    # or you can use this way:
                    # update_doc[key] = input(key+ " ["+ str(value) + "] :").lower() 
                    # first [alex] : type any thing or just leave it empty

                # we don't always want to change every single piece of information (every key's value)
                # So what we're going to do here: 
                # is to check update_doc[the current key] if it has a value or empty
                # If we haven't actually entered anything for update_doc, we've just left it blank
                # we don't actually want to delete the information that's in there already
                # we just want to leave it the same as it was before
                # In case if the user doesn't update/insert/type a new value
                # because they can leave it empty by just pressing Enter key
                # Which means we need to use again the same current value of this key   
                if update_doc[key] =="":
                    # we will reassign the current value to the same key again
                    update_doc[key] = value
                

        # For more clarity (optional):
        # We can loop => "update_doc" object that contains the new values [Before updating our Database]
        print("") # Just printing a blank line
        print ("The new updated document:")
        print ("=========================")
        for key, value in update_doc.items():
            print(key,": [",value,"]")

        # myquery = { "address": "Valley 345" }
        # newvalues = { "$set": { "address": "Canyon 123" } }
        # mycol.update_one(myquery, newvalues)
        
        # The last step is to save this document "update_doc" into the database
        # ************
        # update_one()
        # ************
        # The pure update command for mongodb example: 
        # db.users.update({first_name:"martin"},{ $set: {"last_name":"smith" }})
        # our pattern: collection_name.update_one(doc, {'$set': update_doc})
        # first argument (doc): contains our search criteria: first and last
        # second argument (update_doc): contains the new (same) values
        # We will have a try except block again:
        try:
            # we're going to call the collection.update_one() method: 
            collection.update_one(doc, { '$set': update_doc})     
            # doc: is the current document we want to update (the one that mongodb will search for)
            # $set: the MongoDB keyword to set/write the new values
            # update_doc: the dictionary (object) that we're going to pass in, the one we have just created
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")

def main_loop():   
    """
    - Print/Display the menu for CRUD operations or Exit the app 
    """
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
            print("You have selected option 3 for editing a record")
            edit_record()
        elif option == "4":
            print("You have selected option 4 for deleting a record")
            delete_record()
        elif option == "5":
            # We should close our connection with MongoDB first:
            client.close()
            # Then we can exit the while loop and the entire application
            break
        else:
            print("Invalid Option!")

# 2: Call our function main_loop()
main_loop()