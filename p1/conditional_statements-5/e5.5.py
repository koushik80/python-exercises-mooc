#E-5.5:Calculator

#Problem:Please write a program which asks the user for two numbers and an operation.
#If the operation is add, multiply or subtract, the program should calculate
#and print out the result of the operation with the given numbers.
#If the user types in anything else, the program should print out nothing.

#Some examples of expected behaviour:

            #Number 1: 10
            #Number 2: 17
            #Operation: add

            #10 + 17 = 27

            #Number 1: 4
            #Number 2: 6
            #Operation: multiply

            #4 * 6 = 24

            #Number 1: 4
            #Number 2: 6
            #Operation: subtract

            #4 - 6 = -2

#Solution:


num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
option = input("Operation:")


def add(x, y):
    return(x + y)

def multiply(x, y):
    return(x * y)

def subtract(x, y):
    return(x - y)

result = 0

if option == "add":
    result = add(num1,num2)
    print (num1,"+",num2,"=",result)
elif option == "multiply":
    result = multiply(num1, num2)
    print (num1,"*",num2,"=",result)
elif option == "subtract":
    result = subtract(num1, num2)
    print (num1,"-",num2,"=",result)
else:
    print()