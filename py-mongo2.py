# NOTE: Please notice that we still have the same code (template)
# to communicate with our database and the collection
# But we didn't use this code in this file, we just have them for reviewing only
import pymongo

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

# Step1: Create/Define a function that display a list of options named "show_menu()"
# The menu will be about the full CRUD: Create, Read, Update, and Delete.
# Remember in JS we can write function showMenu() using camelCase
# like the native (built-in) functions in JS: getElementById()
def show_menu():
    print("")
    print("1. Add a record")
    print("2. View a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    # Create a variable named "user_option" 
    # for example to refer to the user option that she/he is going to input
    # And it's going to take the return of our input
    # We're going to ask to enter an option.
    # Remember that input() method will return any value the user enters
    # We don't want to lose the inserted user's value, 
    # we will assign (=) the returned value of input() method
    # to a Variable named "user_option"
    user_option = input("Enter option number: ")

    # Note: Please remember that input function will return a string data type:
    # if we input 1 as a number => input() function will return "1" as a string

    # Our function will then return the option that we've selected.

    # To Review: Variable Scope:
    # the variable "option" is only defined and used inside this function so it's a local variable
    # local variable can be seen only by the function itself
    # for quick testing:
    # print ("your selected option was:",user_option)
    # the return keyword (like in JavaScript) will return a value to the main script (the code outside the function)
    return user_option

# Review: For testing the variable scope:
# ***************************************
# print ("your selected option was:", user_option) # NameError: name 'user_option' is not defined

# my_option=show_menu()
# notice here that the variable "my_option" is a global variable 
# because it's defined in the main script (not inside a function)
# Global variable can be accessed inside/outside the function and that's why it has a global scope
# for testing:
# print("My option:",my_option)

# Step2: Create/Define a function main_loop()
def main_loop():
    # We're going to use while True, 
    # which means that it will basically run forever 
    # until we terminate it (we don't want to use CTRL+C to break it!)
    while True: # It will be always true to keep running the while loop:
        # Step2: call the function (run the function):
        # because our function is returning a value (1,2,3,4, 5) base on the user input
        # We can save this returned value into a variable named "option"
        # Or store the result of our show menu function in a variable called "option".
        option = show_menu() # here is the line for activating/calling our our function show_menu()
        if option == "1":
            print("You have selected option 1")
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            # As we know before, loops iterate over a block of code until the test expression is false, 
            # but we want to terminate/stop/break the current iteration or even the whole loop 
            # when the user selects 5  without checking test expression:
            # break: The break statement terminates the loop containing it.
            # which exits from the while loop (program).
            # print("You have selected option 5")

            # One last thing we should do before exit the application
            # Is to close our connection with the database
            # We're going to use the same connection variable "client" with a method named "close()"
            # close(): Cleanup client resources and disconnect from MongoDB.
            client.close()

            # Now we can return to our keyword "break" to stop the while loop:

            # Just for fun :-):
            input ("So you are going to exit the application! Oh no! we are going to miss you, but Good Buy any way!")
            # we need to use the Python keyword break to break the while loop
            break
        # Our else statement:
        # if we don't select options 1, 2, 3, 4, or 5, 
        # then it's going to print "Invalid Option!"
        else:
            print("Invalid Option!")

# Step3: Call our function main_loop()
main_loop()
# To summarize:
# print() and input() methods
# print() will print the text in between the brackets and jump to the next line in our code
# input() will print the text in between the brackets but it will wait for us to enter any value or just press enter
# then it will jump to the next line in our code

# input() can return the user input and that's why it's assigned into a variable