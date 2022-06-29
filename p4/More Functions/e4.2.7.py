#E4.2.7:A spruce

#Problem:

#Please write a function named spruce, which takes one argument.
#The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.

#Calling spruce(3) should print out


#Sample output:

        #a spruce!
        #   *
        #  ***
        # *****
        #   *

#Calling spruce(5) should print out

        #a spruce!
        #     *
        #    ***
        #   *****
        #  *******
        # *********
        #     *

#Solution:


def spruce(n):
    print("a spruce!")
    i = 1
    x = 0
    y = "**"

    while i <= n:
        print(" " * (n-i) + "*" + y*x)
        i += 1
        x += 1

    print(" " * (n-1) + "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
