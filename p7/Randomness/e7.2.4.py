# E-7.2.4:Dice rolller


# Problem: https://programming-22.mooc.fi/part-7/2-randomness


# Sample Output:


# Solution:

from random import choice


def roll(die: str):
    A = 3, 3, 3, 3, 3, 6
    B = 2, 2, 2, 5, 5, 5
    C = 1, 4, 4, 4, 4, 4
    if die == "A":
        return choice(A)
    elif die == "B":
        return choice(B)
    else:
        return choice(C)


def play(die1: str, die2: str, times: int):
    x = 0
    y = 0
    ties = 0

    for i in range(times):
        item_1 = roll(die1)
        item_2 = roll(die2)
        if item_1 > item_2:
            x += 1
        elif item_1 < item_2:
            y += 1
        else:
            ties += 1

    return x, y, ties


if __name__ == '__main__':
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
