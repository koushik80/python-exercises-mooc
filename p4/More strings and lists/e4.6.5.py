# E-4.6.5:Neighbours in a list

# Problem:Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1.
# So, items 1 and 2 would be neighbours, and so would items 56 and 55.

# Please write a function named longest_series_of_neighbours,
# which looks for the longest series of neighbours within the list, and returns its length.

# For example, in the list[1, 2, 5, 4, 3, 4] the longest list of neighbours would be[5, 4, 3, 4], with a length of 4.

# An example function call:

#my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
# print(longest_series_of_neighbours(my_list))


# Sample output:

# 4

# Solution:

def longest_series_of_neighbours(lst: list):

    l = len(lst)
    calculation = 0
    list_of_neighbours = 0

    for i in range(l-1):
        if abs(lst[i] - lst[i + 1]) == 1:
            calculation += 1
        else:
            calculation = 0
        if calculation > list_of_neighbours:
            list_of_neighbours = calculation

    return list_of_neighbours + 1


if __name__ == '__main__':
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
