# E-7.2.2:Password generator, part 1


# Problem:Please write a function which creates passwords of a desired length, consisting of lowercase characters a to z.

# An example of how the function should work:

# for i in range(10):
# print(generate_password(8))


# Sample Output:

# lttehepy
# olsxttjl
# cbjncrzo
# dwxqjdgu
# gpfdcecs
# jabyvgar
# xnbbonbl
# ktmsjyww
# ejhprmel
# rjkoacib


# Solution:

from random import sample
from string import ascii_lowercase


def generate_password(length: int):
    list = sample(ascii_lowercase, length)
    password = ""

    for letter in list:
        password += letter
    return password


if __name__ == '__main__':
    for letter in range(10):
        print(generate_password(8))
