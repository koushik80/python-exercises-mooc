#E-4.7:Sum and mean

#Problem: Please write a program which asks the user for four numbers.
#The program then prints out the sum and the mean of the numbers.

#The program should function as follows:

            #Number 1: 2
            #Number 2: 1
            ##Number 3: 6
            #Number 4: 7
            #The sum of the numbers is 16 and the mean is 4.0

#Solution:

num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
num3 = int(input("Number 3:"))
num4 = int(input("Number 4:"))
n_sum = num1 + num2 + num3 +num4
n_mean = n_sum / 4
print(f"The sum of the numbers is {n_sum} and the mean is {n_mean}")
