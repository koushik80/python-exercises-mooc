# E-5.1.3: Go

# Problem:In a game of Go two players take turns to place black and white stones on a game board.
# The winner is the player who manages to encircle a bigger area on the board with their own game pieces.

# Please write a function named who_won(game_board: list),
# which takes a two-dimensional array as its argument.
# The array consists of integer values, which represent the following situations:

# 0: empty square
# 1: player 1 game piece
# 2: player 2 game piece
# The scoring rules of Go can be quite complex,
# but in this exercise it is enough to compare the number of pieces each player has on the game board.
# Also, the size of the game board is not limited.

# The function should return the value 1 if player 1 won, and the value 2 if player 2 won.
# If both players have the same number of pieces on the board, the function should return the value 0.


# Sample output:


# Solution:

def who_won(game_board: list):

    player_1 = 0
    player_2 = 0

    for i in range(0, 1):
        for row in game_board:
            for column in row:
                if column == 1:
                    player_1 += 1
                elif column == 2:
                    player_2 += 1

    if player_1 > player_2:  # player_1 winner with value 1
        return 1
    elif player_2 > player_1:  # player_2 winner with value 2
        return 2
    elif player_1 == player_2:  # both winner with same number
        return 0


if __name__ == "__main__":
    go = [[0, 1, 2, 1], [2, 0, 1, 1], [1, 1, 2, 0]]
    print(who_won(go))
