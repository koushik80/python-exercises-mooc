# E-4.4.1:The shortest in the list

# Problem:Please write a function named shortest,
# which takes a list of strings as its argument.
# The function returns whichever of the strings is the shortest.
# If more than one are equally short,
# the function can return any of the shortest strings (there will be no such situation in the tests).
# You may assume there will be no empty strings in the list.

#my_list = ["first", "second", "fourth", "eleventh"]

#result = shortest(my_list)
# print(result)
# ------------------------------------------------------------

#my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

#result = shortest(my_list)
# print(result)

# Sample output:

# first
# tim

# Solution:

def shortest(lst: list):
    lst.sort(key=len)
    shortest_str = lst[0]
    return shortest_str


if __name__ == '__main__':
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)


# or

# def shortest(lst: list):
    #shortest = ""

    # for i in lst:
    #     if shortest == "" or len(i) < len(shortest):
    #shortest = i
    # return shortest
