# E-4.6.2:Most common character

# Problem:Please write a function named most_common_character,
# which takes a string argument. The function returns the character which has the most occurrences within the string.
# If there are many characters with equally many occurrences,
# the one which appears first in the string should be returned.

# An example of expected behaviour:

#first_string = "abcdbde"
# print(most_common_character(first_string))

#second_string = "exemplaryelementary"
# print(most_common_character(second_string))

# Sample output:

# b
# e

# Solution:

def most_common_character(word: str):
    text = ""
    chr = 0
    for i in word:
        if word.count(i) > chr:
            chr = word.count(i)
            text = i
    return text


if __name__ == '__main__':
    first_string = "abcdbde"
    print(most_common_character(first_string))

    first_string = "abcdbde"
    print(most_common_character(first_string))
