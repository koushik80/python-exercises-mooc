#E-3.2.8: Right-aligned

#Problem: Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed.
#If the input is shorter than 20 characters,
#the beginning of the line is filled in with * characters.

#You may assume the input string is at most 20 characters long.

        #Please type in a string: python
        #**************python

        #Please type in a string: alongerstring
        #*******alongerstring

        #Please type in a string: averyverylongstring
        #*averyverylongstring

#Solution:

str = input("Please type in a string: ")
length = len(str)
j = 0

if length == 20:
    print(str)
elif length < 20:
    j = (20 - length)
    print("*" * (j) + str)
