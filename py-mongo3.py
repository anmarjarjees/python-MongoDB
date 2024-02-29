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

    # TIP/HINT: This part for your Micro Project2:
    # salary = input("Enter your salary") # => "20"
    # You can use float to convert the string into float value
    # salary = float(input("Enter your salary")) # => 20.0
    
    # Now we can start building our dictionary to insert into the database.
    # in our life we use dictionary to search for the meaning of English word in an other language
    # The searched keyword is the key and the meaning could be the value
    # dictionary: Key and its value ==> the key is "first" and it's value is "alex"
    # NOTE: We want the first, the last name, or any text value to be stored in the database in lowercase, 
    # which will make it much easier for us to find/retrieve them later.
    # In Python we use lower() method. In JS we used toLower()
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
            print("You have selected option 2")
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

# Call our function main_loop()
main_loop()