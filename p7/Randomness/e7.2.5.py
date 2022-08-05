# E-7.2.5:Random words


# Problem: The exercise template contains the file words.txt,
# which contains some English language words, one on each line.

# Please write a function named words(n: int, beginning: str),
# which returns a list containing n random words from the words.txt file.
# All words should begin with the string specified by the second argument.

# The same word should not appear twice in the list.
# If there are not enough words beginning with the specified string,
# the function should raise a ValueError exception.

# An example of the function in action:

#word_list = words(3, "ca")
# for word in word_list:
# print(word)


# Sample Output:

# cat
# car
# carbon


# Solution:

import random


def words(n: int, beginning: str):
    random_words = []

    with open("words.txt") as new_file:
        for lines in new_file:
            lines = lines.strip()
            if beginning in lines[:len(beginning)]:
                random_words.append(lines)

    try:
        return random.sample(random_words, n)
    except:
        raise ValueError


if __name__ == '__main__':
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
