# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Providing Examples of Error Handling and Pickling using a program
# that requests and stores a list of numbers from the user
# ChangeLog (Who,When,What):
# Jbentzen,5.30.2022,Created Script
# ---------------------------------------------------------------------------- #

import pickle # This allows reading and writing to binary file types

lstMain = [] # Empty List for data storage
strChoice = ""
strFileName = "NumbersList.dat"

class ValueNotNumberError(Exception):
    '''Raised when the value entered is not a number'''
    pass

print("This is a list of your favorite numbers.")
while(strChoice != "5"):
    print('''
    Menu of Options
    1) Add a new number
    2) Remove an existing number
    3) Read Current File
    4) Save List to File        
    5) Exit Program
    ''')
    print("Your Current List:")
    print(lstMain)
    strChoice = input("Please choose an option (1-5): ")

    if (strChoice == "1"): # Using append to add values to the list.
        strAdd = input("Please provide a number to add to list: ")
        try:
            if strAdd.isnumeric():
                lstMain.append(strAdd)
            else:
                raise ValueNotNumberError
        except Exception as e:
            print("Please only use the number characters (1-9) for input!")

    elif (strChoice == "2"): # Using remove to remove values from the list
        strRemove = input("Number to remove from list: ")
        try:
            lstMain.remove(strRemove)
        except ValueError as e:
            print("This number is not in the list!")

    elif (strChoice == "3"):
        try:
            print("Here is the current list in the file: ")
            objFile = open(strFileName, "rb")
            objFileData = pickle.load(objFile)
            objFile.close()
            for item in objFileData:
                print(item)

        except Exception as e:
            print("There was an error!")

    elif (strChoice == "4"):
        try:
            objFile = open(strFileName, "wb")
            pickle.dump(lstMain, objFile)
            objFile.close()
            print("Data Saved!")
        except Exception as e:
            print("There was an error!")
    else:
        print("Please enter 1-5")

print("***Exiting Program***")