# E-5.2.4: Sudoku: add number to a copy of the grid

# Problem:This is the very last sudoku task.
# This time we will create a slightly different version of the function for adding new numbers to the grid.

# The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid,
# two integers referring to the row and column indexes of a single square,
# and a single digit between 1 and 9, as its arguments.
# The function should return a copy of the original grid with the new digit added in the correct location.
# The function should not change the original grid received as a parameter.

# The print_sudoku function from the previous exercise could be useful for testing,
# and it is used in the example below:

# sudoku = [
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

#grid_copy = copy_and_add(sudoku, 0, 0, 2)
# print("Original:")
# print_sudoku(sudoku)
# print()
# print("Copy:")
# print_sudoku(grid_copy)


# Sample output:

# Original:
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# Copy:
# 2 _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# Hint When dealing with nested lists you should be extra careful when copying.
# What all needs to be explicitly copied,
# and where do changes actually have an effect?
# The visualisation tool is a great help here, too,
# although the size of the sudoku grid will make the view less orderly than usual.

# Solution:

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):

    grid_copy = []

    for x in sudoku:
        row = []
        for i in x:
            row.append(i)
        grid_copy.append(row)

    grid_copy[row_no][column_no] = number
    return grid_copy


def print_sudoku(sudoku: list):

    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                sudoku[x][y] = "_"

    grid = sudoku[:]

    for row in range(9):
        if row > 0 and row % 3 == 0:
            print()

        for column in range(0, 9):
            print(grid[row][column], end=" ")
            column += 1
            if column % 3 == 0:
                print(end=" ")

        print()


if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
