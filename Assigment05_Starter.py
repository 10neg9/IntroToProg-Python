# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "lstTable"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# NSmith,5.14.020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   #name of file
objFile = None # File handle, An object that represents a file
strData = ""  # A row of text data from the file
lstRow = []    # Text data from file stored as a list
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
count = 0 # A number to count the rows in table
strMax = "" # A string to store the count as a string
intChoice = 0 # A number to store the strChoice as integer


# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "a")
objFile = open(strFile, "r")
for strData in objFile:
    lstRow = strData.split(",")
    dicRow = {"task":lstRow[0],"priority":lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = input("Which option would you like to perform? [1 to 5]: ")
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("\t---ToDo List---")
        print("\tTask | Priority")
        for row in lstTable:
            print("\t",row["task"]," | ",row["priority"],sep='')
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        dicRow = {"task":input("Enter task: "),"priority":input("Enter Priority: ")}
        lstTable.append(dicRow)
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        count = 0
        for row in lstTable:
            count += 1
            print("\t",count,": ",row["task"]," ",row["priority"],sep='')
        if count == 0:
            print("Nothing to remove. Try option 2 to add a task/priority.")
        else:
            strMax = str(count)
            strChoice = input("\nWhich item should be removed?[1 - " + strMax +"]: ")
            try:
                intChoice = int(strChoice.strip())
                if (intChoice >= 1 and intChoice <= count):
                    lstTable = lstTable[:intChoice-1] + lstTable[intChoice:]
                else:
                    print("'",strChoice.strip(),"' is not an option! Let's start over.",sep='')
            except:
                print("'",strChoice.strip(),"' is not valid. Did you choose a number? Let's start over.",sep='')
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["task"] + "," + row["priority"] + "\n")
        objFile.close()
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Goodbye!")
        break  # and Exit the program
    # None of the above - Invalid Choice
    else:
        print("You entered '%s'. Please choose a number 1 to 5." % strChoice)
