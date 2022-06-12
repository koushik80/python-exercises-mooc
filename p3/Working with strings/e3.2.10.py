#E-3.2.10:Substrings, part 1

#Problem: Please write a program which asks the user to type in a string.
#The program then prints out all the substrings which begin with the first character,
#from the shortest to the longest.
#Have a look at the example below.

        #Please type in a string: test
        #t
        #te
        #tes
        #test

#Solution:

str = input("Please type in a string: ")


print(str[0])
print(str[0:2])
print(str[0:3])
print(str[0:])

