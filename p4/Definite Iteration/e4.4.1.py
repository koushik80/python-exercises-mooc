# E-4.4.1:Star-studded

# Problem: Please write a program which asks the user to type in a string.
# The program then prints each input character on a separate line.
# After each character there should be a star (*) printed on its own line.

# This is how it should work:

# Sample output:

# Please type in a string: Python
# P
# *
# y
# *
# t
# *
# h
# *
# o
# *
# n
# *

# NB: this exercise doesn't ask you to write any functions,
# so you should not place any code within an if __name__ == "__main__" block.
# Solution:


user_input = input("Please type in a string: ")

for letter in user_input:
    print(letter)
    print("*")
