# E-7.2.3:Password generator, part 2


# Problem: Please write an improved version of your password generator.
# The function now takes three arguments:

# .If the second argument is True, the generated password should also contain one or more numbers.
# .If the third argument is True, the generated password should also contain one or more of these special characters: !?= +-()
# Despite these two additional arguments,
# the password should always contain at least one lowercase alphabet.
# You may assume the function will only be called with combinations of arguments that are possible to formulate into passwords following these rules.
# That is , the arguments will not specify e.g. a password of length 2 which contains both a number and a special characters,
# for then there would not be space for the mandatory lowercase letter.

# An example of how the function should work:

# for i in range(10):
#print(generate_strong_password(8, True, True))


# Sample Output:

# 2?0n+u31
# u=m4nl94
# n#=i6r#(
# da9?zvm?
# 7h)!)g?!
# a=59x2n5
# (jr6n3b5
# 9n(4i+2!
# 32+qba#=
# n?b0a7ey


# Solution:

from random import choice, shuffle
from string import ascii_lowercase, digits


def generate_strong_password(length: int, num: bool, spcl_char: bool):
    list_a = []
    signs = list('!?=+-()#')
    strong_password = ""
    password = ""

    for letter in range(length):
        list_a.append(choice(ascii_lowercase))
        if num:
            list_a.append(choice(digits))
        if spcl_char:
            list_a.append(choice(signs))

    for letter in range(length):
        strong_password += list_a[letter]

    password = list(strong_password)
    shuffle(password)
    strong_password = "".join(password)

    return strong_password


if __name__ == '__main__':
    for letter in range(10):
        print(generate_strong_password(8, True, True))
