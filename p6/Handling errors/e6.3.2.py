# E-6.3.2: Parameter validation

# Problem: Please write a function named new_person(name: str, age: int),
# which creates and returns a tuple containing the data in the arguments.
# The first element should be the name and the second the age.

# If the values stored in the parameter variables are not valid,
# the function should throw a ValueError exception.

# Invalid parameters in this case include:

# name is an empty string
# name contains less than two words
# name is longer than 40 characters
# age is a negative number
# age is greater than 150


# Sample output:


# Solution:

def new_person(name: str, age: int):
    x = name.split(" ")
    if len(name) == 0 or len(x) < 2 or len(name) > 40:
        raise ValueError
    if age < 0 or age > 150:
        raise ValueError
    return name, age


if __name__ == '__main__':
    person = new_person("John", 42)
    print(person)
