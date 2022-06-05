#E-3.1.3:Numbers

#Problem: Please write a program which asks the user for a number.
#The program then prints out all integer numbers greater than zero but smaller than the input.

        #Upper limit: 5
        #1
        #2
        #3
        #4

#Solution:

number1 = int(input("Upper limit: "))
number2 = 1
while number1 > 0 and number2 < number1:
    print(number2)
    number2 += 1
