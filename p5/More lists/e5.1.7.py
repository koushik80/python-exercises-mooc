# E-5.1.7: Sudoku: check grid

# Problem:Please write a function named sudoku_grid_correct(sudoku: list),
# which takes a two-dimensional array representing a sudoku grid as its argument.
# The function should use the functions from the three previous exercises to determine whether the complete sudoku grid is filled in correctly.
# Copy the functions from the exercises above into your Python code file for this exercise.

# The function should check each of the nine rows,
# columns and 3 by 3 blocks in the grid. If all contain each of the numbers 1 to 9 at most once,
# the function returns True. If a single one is filled in incorrectly, the function returns False.

# The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with thicker borders.
# These are the blocks the function should check,
# and they begin at the indexes(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).

# sudoku1 = [
#[9, 0, 0, 0, 8, 0, 3, 0, 0],
#[2, 0, 0, 2, 5, 0, 7, 0, 0],
#[0, 2, 0, 3, 0, 0, 0, 0, 4],
#[2, 9, 4, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 7, 3, 0, 5, 6, 0],
#[7, 0, 5, 0, 6, 0, 4, 0, 0],
#[0, 0, 7, 8, 0, 3, 9, 0, 0],
#[0, 0, 1, 0, 0, 0, 0, 0, 3],
#[3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]

# print(sudoku_grid_correct(sudoku1))

# sudoku2 = [
#[2, 6, 7, 8, 3, 9, 5, 0, 4],
#[9, 0, 3, 5, 1, 0, 6, 0, 0],
#[0, 5, 1, 6, 0, 0, 8, 3, 9],
#[5, 1, 9, 0, 4, 6, 3, 2, 8],
#[8, 0, 2, 1, 0, 5, 7, 0, 6],
#[6, 7, 4, 3, 2, 0, 0, 0, 5],
#[0, 0, 0, 4, 5, 7, 2, 6, 3],
#[3, 2, 0, 0, 8, 0, 0, 5, 7],
#[7, 4, 5, 0, 0, 3, 9, 0, 1]
# ]

# print(sudoku_grid_correct(sudoku2))

# Sample output:

# False
# True

# Solution:
# NB:
# functions:  row_correct(sudoku:sudoku_grid_correct),
# column_correct(sudoku: list, column_no: int),
# block_correct(sudoku: list, row_no: int, column_no: int)
# taken from previous solutions

def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    numbers = []

    for num in row:
        if num > 0 and num in numbers:
            return False
        numbers.append(num)

    return True


def column_correct(sudoku: list, column_no: int):

    numbers = []

    for row in sudoku:
        column_s = row[column_no]
        if column_s > 0 and column_s in numbers:
            return False
        numbers.append(column_s)

    return True


def block_correct(sudoku: list, row_no: int, column_no: int):

    lst = []
    x = 0
    y = 0

    for i in range(9):
        j = sudoku[row_no + x][column_no + y]
        lst.append(j)
        y += 1
        if y == 3:
            x += 1
            y = 0

    numbers = []

    for num in lst:
        if num > 0 and num in numbers:
            return False
        numbers.append(num)

    return True


def sudoku_grid_correct(sudoku: list):

    for k in range(0, 7, 3):
        for l in range(0, 7, 3):
            if not block_correct(sudoku, k, l):
                return False

    for k in range(9):
        if not (row_correct(sudoku, k) and column_correct(sudoku, k)):
            return False

    return True


if __name__ == '__main__':
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))
