#E-3.2.1:String multiplied

#Problem: Please write a program which asks the user for a string and an amount.
#The program then prints out the string as many times as specified by the amount.
#The printout should all be on one line, with no extra spaces or symbols added.

#An example of expected behaviour:

        #Please type in a string: hiya
        #Please type in an amount: 4
        #hiyahiyahiyahiya

#Solution:

str = input("Please type in a string: ")
amnt = int(input("Please type in an amount: "))

print(str * amnt)
