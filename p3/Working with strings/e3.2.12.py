#E-3.2.12:Does it contain vowels

#Problem:Please write a program which asks the user to input a string.
#The program then prints out different messages if the string contains any of the vowels a, e or o.

#You may assume the input will be in lowercase entirely.
#Have a look at the examples below.

        #Please type in a string: hello there
        #a not found
        #e found
        #o found

        #Please type in a string: hiya
        #a found
        #e not found
        #o not found

#Solution:

str = input("Please type in a string: ")

if "a" in str:
    print("a found")
else:
    print("a not found")

if "e" in str:
    print("e found")
else:
    print("e not found")

if "o" in str:
    print("o found")
else:
    print("o not found")
