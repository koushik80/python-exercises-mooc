#E-3.4.7:A word squared

#Problem:Please write a function named squared,
#which takes a string argument and an integer argument,
#and prints out a square of characters as specified by the examples below.

            #squared("ab", 3)
            #print()
            #squared("aybabtu", 5)

            #aba
            #bab
            #aba

            #aybab
            #tuayb
            #abtua
            #ybabt
            #uayba

#Solution:

from itertools import cycle, islice


def squared(text, length):
    letters = cycle(text)
    for i in range(length):
        print("".join(islice(letters, length)))


if __name__ == "__main__":
    squared("abc", 5)
