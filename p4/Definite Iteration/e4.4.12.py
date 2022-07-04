# E-4.4.1:All the longest in the list

# Problem:Please write a function named all_the_longest,
# which takes a list of strings as its argument.
# The function should return a new list containing the longest string in the original list.
# If more than one are equally long,
# the function should return all of the longest strings.

# The order of the strings in the returned list should be the same as in the original.

#my_list = ["first", "second", "fourth", "eleventh"]

#result = all_the_longest(my_list)
# print(result)  # ['eleventh']

# -----------------------------------------------------

#my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

#result = all_the_longest(my_list)
# print(result)  # ['dorothy', 'richard']

# Sample output:


# Solution:

def all_the_longest(lst: list):
    longest = len(max(lst, key=len))
    new_list = []
    l = len(lst)

    for i in range(l):
        if (len(lst[i]) == longest):
            new_list.append(lst[i])
    return new_list


if __name__ == '__main__':
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)  # ['dorothy', 'richard']
