#E-3.1.6:Please write a program which asks the user to type in a limit.
#The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. The program should function as follows:

#Limit: 2
#3

#Limit: 10
#10

#Limit: 18
#21

#If you have trouble understanding how the desired output is calculated,
#the sample outputs in the next exercise may help.
#You may assume the number typed in by the user is always equal to 2 or higher.

#Solution:

limit = int(input("Limit: "))
base = 0
num = 1
num_total = 0
calculation = "sum of consecutive numbers"

while base < limit:
    calculation += f"{num} + "
    base += num
    num += 1

print(base)
