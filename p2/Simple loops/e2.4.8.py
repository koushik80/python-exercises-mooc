#E-2.4.8:Working with numbers

#Problems:

#Pre-task

#Please write a program which asks the user for integer numbers.
#The program should keep asking for numbers until the user types in zero.

        #Please type in integer numbers. Type in 0 to finish.
        #Number: 5
        #Number: 22
        #Number: 9
        #Number: -2
        #Number: 0

#Part 1: Count

#After reading in the numbers the program should print out how many numbers were typed in.
#The zero at the end should not be included in the count.

#You will need a new variable here to keep track of the numbers typed in.

        #... the program asks for numbers
        #Numbers typed in 4

#Part 2: Sum

#The program should also print out the sum of all the numbers typed in.
#The zero at the end should not be included in the calculation.

#The program should now print out the following:

        #... the program asks for numbers
        #Numbers typed in 4
        #The sum of the numbers is 34

#Part 3: Mean

#The program should also print out the mean of the numbers.
#The zero at the end should not be included in the calculation.
#You may assume the user will always type in at least one valid non-zero number.

        #... the program asks for numbers
        #Numbers typed in 4
        #The sum of the numbers is 34
        #The mean of the numbers is 8.5

#Part 4: Positives and negatives

#The program should also print out statistics on how many of the numbers were positive and how many were negative.
#The zero at the end should not be included in the calculation.

        #... the program asks for numbers
        #Numbers typed in 4
        #The sum of the numbers is 34
        #The mean of the numbers is 8.5
        #Positive numbers 3
        #Negative numbers 1

#Solution:

print(f'Please type in integer numbers. Type in 0 to finish.')

total_num = 0
summ_num = 0
mean = 0
pos_num = 0
neg_num = 0


while True:
        num = int(input("Number: "))
        if num == 0:
             break
        if num < 0 and num > 1:
             continue
        total_num += 1
        summ_num += num
        if num >= 0:
            pos_num += 1
        elif num < 0:
            neg_num += 1


print(" ")
print(f'Numbers typed in {total_num}')
print(f'The sum of the numbers is {summ_num}')
print(f'The mean of the numbers is {mean}')
print(f'Positive numbers {pos_num}')
print(f'Negative numbers {neg_num}')
