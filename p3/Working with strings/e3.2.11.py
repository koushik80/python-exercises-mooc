#E-3.2.11:Substrings, part 2

#Problem: Please write a program which asks the user to type in a string.
#The program then prints out all the substrings which end with the last character,
#from the shortest to the longest.
#Have a look at the example below.

        #Please type in a string: test
        #t
        #st
        #est
        #test

#Solution:

str = input("Please type in a string: ")


print(str[-1])
print(str[-2:])
print(str[-3:])
print(str[0:])
