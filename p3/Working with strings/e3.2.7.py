#E-3.2.7:Underlining

#Problem: Please write a program which asks the user for strings using a loop.
#The program prints out each string underlined as shown in the examples below.
#The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.

        #Please type in a string: Hi there!

        #Hi there!
        #---------
        #Please type in a string: This is a test

        #This is a test
        #--------------
        #Please type in a string: a

        #a
        #-
        #Please type in a string:

#Solution:

while True:
    str = input("Please type in a string: ")
    if str == "":
        break
    elif str:
        print(str)
        print("-"*len(str))
