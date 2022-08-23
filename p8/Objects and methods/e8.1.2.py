# E-8.1.2: Row sums


# Problem: https://programming-22.mooc.fi/part-8/1-objects-and-methods#programming-exercise-row-sums


# Sample output:

#[[1, 2, 3], [3, 4, 7]]

# Solution:

def row_sums(my_matrix: list):
    for row in my_matrix:
        row.append(sum(row))


if __name__ == '__main__':
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
