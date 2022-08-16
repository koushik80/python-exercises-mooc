# E-7.5.1: String helper

# Problem: Please write a module named string_helper, which contains the following functions:

# The function change_case(orig_string: str) creates and returns a new version of the parameter string. The lowercase letters in the original should be uppercase, and uppercase letters should be lowercase.

# The function split_in_half(orig_string: str) splits the parameter string in half, and returns the results in a tuple. If the original has an odd number of characters, the first half should be shorter.

# The function remove_special_characters(orig_string: str) returns a new version of the parameter string, with all special characters removed. Only lowercase and uppercase letters, numbers and spaces are allowed in the returned string.

# Some examples of how the module would be used:

# import string_helper

# my_string = "Well hello there!"

# print(string_helper.change_case(my_string))

# p1, p2 = string_helper.split_in_half(my_string)

# print(p1)
# print(p2)

# m2 = string_helper.remove_special_characters(
# "This is a test, lets see how it goes!!!11!")
# print(m2)


# Sample output:

# wELL HELLO THERE!
# Well hel
# lo there!
# This is a test lets see how it goes11


# Solution:

from string import punctuation


def change_case(orig_string: str):
    word = ""
    for x in orig_string:
        if x.isupper():
            x = x.lower()
        else:
            x = x.upper()
        word += x
    return word


def split_in_half(orig_string: str):
    l = len(orig_string) // 2
    p = orig_string[:l]
    q = orig_string[l:]
    return p, q


def remove_special_characters(orig_string: str):
    for x in orig_string:
        if x in punctuation or x == '¤':
            orig_string = orig_string.replace(x, '')
    return orig_string


if __name__ == '__main__':
    my_string = "Well hello there!"
    print(change_case(my_string))
    p1, p2 = split_in_half(my_string)

    print(p1)
    print(p2)

    m2 = remove_special_characters(
        "This is a test, lets see how it goes!!!11!")
    print(m2)
