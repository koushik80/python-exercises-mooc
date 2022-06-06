#E-3.1.7:The sum of consecutive numbers, version 2

#Problem: Please write a new version of the program in the previous exercise.
#In addition to the result it should also print out the calculation performed:

        #Limit: 2
        #The consecutive sum: 1 + 2 = 3

        #Limit: 10
        #The consecutive sum: 1 + 2 + 3 + 4 = 10

        #Limit: 18
        #The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

#Solution:

limit = int(input("Limit: "))
base = 0
num = 1
num_total = 0
calculation = "The consecutive sum: "

while base < limit:
    calculation += f"{num} + "
    base += num
    num += 1

print(f"{calculation[:-3]} = {base}")
