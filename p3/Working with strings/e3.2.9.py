#E-3.2.9: A framed word

#Problem: Please write a program which asks the user for a string and then prints out
#a frame of * characters with the word in the centre.
#The width of the frame should be 30 characters.
#You may assume the input string will always fit inside the frame.

#If the length of the input string is an odd number,
#you may print out the word in either of the two possible centre locations.

        #Word: testing
        #******************************
        #*          testing           *
        #******************************

        #Word: python
        #******************************
        #*           python           *
        #******************************

#Solution:

word = input("Word: ")
x = "*" * 30
n = 3

print(x)
for i in range(n):
    print("*" , word , "*")

print(x)
