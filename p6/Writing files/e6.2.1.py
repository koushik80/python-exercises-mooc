# E-6.2.1: Inscription


# Promlem:Please write a program which asks for the name of the user and then creates an "inscription" in a file specified by the user.
# Please see the example below.


# Sample output:

# Whom should I sign this to: Ada
# Where shall I save it: inscribed.txt


# The contents of the file inscribed.txt would be

# Sample output:
# Hi Ada, we hope you enjoy learning Python with us! Best, Mooc.fi Team


# Solution:
def inscription():

    whom = input("Whom should I sign this to: ")
    where = input("Where shall I save it: ")

    with open(where, "w") as new_file:
        new_file.write(
            f'Hi {whom}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')

    with open(where) as new_file:
        print(new_file.read())


inscription()
