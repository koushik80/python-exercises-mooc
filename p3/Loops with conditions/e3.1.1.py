#E-3.1.1: Please write a program which prints out all the even numbers between two and thirty, using a loop.
#Print each number on a separate line.

#The beginning of your output should look like this:

        #2
        #4
        #6
        #8
        #etc...

#Solution:

num = 2


while num >= 2 and num <= 30:
    if num % 2 == 0:
        print(num)
    num += 1
