#E-2.2.2:Greater than or equal to

#Problem: Please write a program which asks for two integer numbers.
#The program should then print out whichever is greater.
#If the numbers are equal, the program should print a different message.

#Some examples of expected behaviour:

        #Please type in the first number: 5
        #Please type in another number: 3
        #The greater number was: 5

        #Please type in the first number:: 5
        #Please type in another number: 8
        #The greater number was: 8

        #Please type in the first number: 5
        #Please type in another number: 5
        #The numbers are equal!

#Solution:

n_1 = int(input("Please type in the first number: "))
n_2 = int(input("Please type in another number: "))

if n_1 > n_2:
    print("The greater number was:", n_1)
elif n_1 < n_2:
    print("The greater number was:", n_2)
else:
    print("The numbers are equal!")
