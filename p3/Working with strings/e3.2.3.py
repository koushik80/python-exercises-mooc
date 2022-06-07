#E-3.2.3:End to beginning

#Problem:Please write a program which asks the user for a string.
#The program then prints out the input string in reversed order,
#from end to beginning. Each character should be on a separate line.

#An example of expected behaviour:

#Please type in a string: hiya
#a
#y
#i
#h

#Solution:

str = input("Please type in a string: ")

#reverse string using while loop
reverse = ''  # store reversed string char by char
length = len(str) - 1
while length >= 0:
    print(str[length])
    reverse = reverse + str[length]
    length -= 1
