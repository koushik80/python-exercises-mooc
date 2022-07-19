# E-6.1.3: Matrix

# Problem:The file matrix.txt contains a matrix in the format specified in the example below:

#1, 0, 2, 8, 2, 1, 3, 2, 5, 2, 2, 2
#9, 2, 4, 5, 2, 4, 2, 4, 1, 10, 4, 2
# ...etc...

# Please write two functions, named matrix_sum and matrix_max.
# Both go through the matrix in the file,
# and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.

# Please also write the function row_sums, which returns a list containing the sum of each row in the matrix.
# For example, calling row_sums when the matrix in the file is defined as

#1, 2, 3
#2, 3, 4

# the function should return the list [6, 9].

# Hint: you can also include other helper functions in your program.
# It is very worthwhile to spend a moment considering which functionalities are shared by the three functions you are asked to write.
# Notice that the three functions named above do not take any arguments,
# but any helper functions you write may take arguments.
# The file you are working with is always named matrix.txt.

# NB: If Visual Studio Code can't find the file and you have checked that there are no spelling errors, take a look at the instructions before this exercise.

# Sample output:


# Solution:

def matrix(txt: str):
    matrix = []
    with open(txt) as new_file:
        for line in new_file:
            elements = []
            value = line.split(",")
            for s in value:
                elements.append(int(s))
            matrix.append(elements)

    return matrix


def row_sums():
    list = matrix("matrix.txt")
    p = []
    for i in range(len(list)):
        number = 0
        for j in range(len(list[i])):
            number += list[i][j]
        p.append(number)
    return p


def matrix_sum():
    value_sums = row_sums()
    return sum(value_sums)


def matrix_max():
    list = matrix("matrix.txt")
    initial = True
    for index in range(len(list)):
        for value in list[index]:
            if initial or greatest < value:
                greatest = value
                initial = False
    return greatest


if __name__ == '__main__':
    print(row_sums())
    print(matrix_sum())
    print(matrix_max())
