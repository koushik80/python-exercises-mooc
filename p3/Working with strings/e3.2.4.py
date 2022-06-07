#E-3.2.4:Second and second to last characters

#Problem: Please write a program which asks the user for a string.
#The program then prints out a message based on whether the second character and the second to last character are the same or not.
#See the examples below.

        #Please type in a string: python
        #The second and the second to last characters are different

        #Please type in a string: pascal
        #The second and the second to last characters are a

#Solution:

str = input("Please type in a string: ")

if str[1] != str[-2]:
    print("The second and the second to last characters are different")
elif str[1] == str[-2]:
    print(f'The second and the second to last characters are {str[1]}')
