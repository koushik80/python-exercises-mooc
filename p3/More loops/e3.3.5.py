#E-3.3.5: Taking turns

#Problem: Please write a program which asks the user to type in a number.
#The program then prints out the positive integers between 1 and the number itself,
#alternating between the two ends of the range as in the examples below.

#Please type in a number: 5
#1
#5
#2
#4
#3

#Please type in a number: 6
#1
#6
#2
#5
#3
#4

#Solution:

num = int(input("Please type in a number: "))

alt_num = [i+1 for i in range(num)]

while alt_num:
    print(alt_num.pop(0))
    alt_num.reverse()


