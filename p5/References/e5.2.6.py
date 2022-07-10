# E-5.2.6: Transpose a matrix

# Problem:Please write a function named transpose(matrix: list),
# which takes a two-dimensional integer array, i.e., a matrix, as its argument.
# The function should transpose the matrix.
# Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.

# You may assume the matrix is a square matrix,
# so it will have an equal number of rows and columns.

# The following matrix

# 1 2 3
# 4 5 6
# 7 8 9
# transposed looks like this:

# 1 4 7
# 2 5 8
# 3 6 9


# The function should not have a return value.
# The matrix should be modified directly through the reference.


# Sample output:

#[1, 4, 7]
#[2, 5, 8]
#[3, 6, 9]

# Solution:

def transpose(matrix: list):
    l = len(matrix)
    for row in range(l):
        for column in range(row, l):
            # square matrix: equal no. of rows and columns
            m_2 = matrix[row][column]
            matrix[row][column] = matrix[column][row]
            matrix[column][row] = m_2

    for i in matrix:
        print(i)


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    transpose(matrix)
