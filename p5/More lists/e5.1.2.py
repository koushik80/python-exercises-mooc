# E-5.1.2: Number of matching elements

# Problem:Please write a function named count_matching_elements(my_matrix: list, element: int),
# which takes a two-dimensional array of integers and a single integer value as its arguments.
# The function then counts how many elements within the matrix match the argument value.

# An example of how the function should work:

#m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
#print(count_matching_elements(m, 1))


# Sample output:

# 3

# Solution:

def count_matching_elements(my_matrix: list, element: int):
    item_match = 0
    for row in my_matrix:
        for num in row:
            if element == num:
                item_match += 1

    return item_match


if __name__ == '__main__':
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
