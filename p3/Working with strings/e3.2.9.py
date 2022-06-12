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

import math

word = input("Word: ")
print("*" * 30)
print("*" * 1 + " " * math.floor((28 - math.floor(len(word)))/2) +
      word + " " * math.floor((28 - math.floor(len(word)))/2) + 1 * "*")
print("*" * 30)
