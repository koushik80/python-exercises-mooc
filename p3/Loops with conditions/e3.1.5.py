#E-3.1.5:Powers of base n

#Problem: Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2).

        #Upper limit: 27
        #Base: 3
        #1
        #3
        #9
        #27

        #Upper limit: 1234567
        #Base: 10
        #1
        #10
        #100
        #1000
        #10000
        #100000
        #1000000

#Solution:

limit = int(input("Upper limit: "))
base = int(input("Base: "))
num = 1

while num <= limit:
    print(num)
    num *= base
