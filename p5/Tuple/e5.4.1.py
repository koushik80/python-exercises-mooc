# E-5.4.1: Create a tuple

# Problem: Please write a function named create_tuple(x: int, y: int, z: int),
# which takes three integers as its arguments,
# and creates and returns a tuple based on the following criteria:

# 1.The first element in the tuple is the smallest of the arguments
# 2.The second element in the tuple is the greatest of the arguments
# 3.The third element in the tuple is the sum of the arguments

# An example of its use:


# if __name__ == "__main__":
#print(create_tuple(5, 3, -1))

# Sample output:

#(-1, 5, 7)

# Solution:
def create_tuple(x: int, y: int, z: int):

    tuple = ()
    list = [x, y, z]
    list.sort()
    first_elm = list[0]   # smallest arguments
    second_elm = list[-1]  # greatest arguments
    third_elm = sum(list)  # total arguments
    tuple = (first_elm, second_elm, third_elm)
    return tuple


if __name__ == '__main__':
    print(create_tuple(5, 3, -1))
