#E-3.2.2:The length and index of a string

#Problem: Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is,
#whichever has the more characters. If the strings are of equal length,
#the program should print out "The strings are equally long".

#Some examples of expected behaviour:

        #Please type in string 1: hey
        #Please type in string 2: hiya
        #hiya is longer

        #Please type in string 1: howdy doody
        #Please type in string 2: hola
        #howdy doody is longer

        #Please type in string 1: hey
        #Please type in string 2: bye
        #The strings are equally long

#Solution:

str_1 = input("Please type in string 1: ")
str_2 = input("Please type in string 2: ")

l_1 = len(str_1)
l_2 = len(str_2)

if l_1 == l_2:
    print("The strings are equally long")
elif l_1 > l_2:
    print(f'{str_1} is longer')
elif l_2 > l_1:
    print(f'{str_2} is longer')
