import pymongo

db_url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(db_url)

database = client["PyDB-Project"] # this line for creating a new db or using an existing one

collection = database["employees"] # this line for creating a new collection or using an existing one
# Important: In MongoDB, a collection is not created until it gets content!

def show_menu():
    # using doctype string below:
    """
    return the user input as a string datatype
    """
    print("")
    print("1. Add a record")
    print("2. View a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    user_option = input("Enter option number: ")
    return user_option

def get_record():
    print("") # just to have a space 
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")

    try:
        document=collection.find_one({'first':first.lower(), 'last':last.lower()})      
    except:
        print("Error accessing the database")
    
    if not document: # we are just saying if doc has no value (has nothing)
        print("")
        print("Error! No results found.")
   
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
    # It's a very good idea to print the record that the user wants to delete:
    # we will call our function view_record():
    # Task1: will get the record based on these fields: first and last calling get_record()
    # Task2: display/print the record (document)
    doc = view_record()
    
    print("")
    # We should check if the record is exist => by checking of doc has any value:
    if doc:
        # We should ask the user for confirmation with this message 
        # and we put a new line in there with Y for yes and N for No:
        confirm = input("Is this the document you want to delete?\nY or N: ")
        print("")

        # Our if condition to perform the delete operation or just ignore it based on the user's input
        if confirm.lower()=='y':
            try:
                # Notice that the remove() method is now deprecated 
                # we should use:
                # delete_one(): To delete one document
                # delete_many(): To delete more than one document
                # for more details: https://www.w3schools.com/python/python_mongodb_delete.asp
                collection.delete_one(doc)
                print("")
                print("Document deleted") 

            # The except block lets you handle the error.
            except:
                print("Error accessing the database or the current record")
        else:
            print("Document/record not deleted") 
            
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