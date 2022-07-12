# E-5.3.3: Histogram

# Problem: Please write a function named histogram,
# which takes a string as its argument. The function should print out a histogram representing the number of times each letter occurs in the string.
# Each occurrence of a letter should be represented by a star on the specific line for that letter.

# For example, the function call histogram("abba") should print out


# Sample output:

# a **
# b **

# while histogram("statistically") should print out

# s **
# t ** *
# a **
# i **
# c *
# l **
# y *

# Solution:

def histogram(exm: str):

    letters = {}

    for letter in exm:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1

    for key, value in letters.items():
        print(key, value * "*")


if __name__ == '__main__':
    histogram("abba")
    print()
    histogram("statistically")
