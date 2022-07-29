# E-6.3.1: Reading Input

# Problem:Please write a function named read_input,
# which asks the user for input until the user types in an integer which falls within the bounds given as arguments to the function.
# The function should return the final valid integer value typed in by the user.

# An example of the function in action:

#number = read_input("Please type in a number: ", 5, 10)
#print("You typed in:", number)


# Sample output:

# Please type in a number: seven
# You must type in an integer between 5 and 10
# Please type in a number: -3
# You must type in an integer between 5 and 10
# Please type in a number: 8
# You typed in: 8


# Solution:


def read_input(txt: str, starts: int, ends: int):
    while True:
        try:
            text = int(input("Please type in a number: "))
            if text >= starts and text <= ends:
                return text
        except ValueError:
            pass
        print(f'You must type in an integer between {starts} and {ends}')


if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
