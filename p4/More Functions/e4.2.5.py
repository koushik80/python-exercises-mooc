#E4.2.5:A triangle

#Problem:Please write a function named triangle,
#which draws a triangle of hashes, and takes one argument.
#The triangle should be as tall and as wide as the value of the argument.

#The function should call the function line from the exercise above for the actual printing out.
#Copy your solution to that exercise above the code for this exercise.
#Please don't change anything in the line function.

#Some examples:

        #triangle(6)
        #print()
        #triangle(3)

#Sample output:

        #
        ##
        ###
        ####
        #####
        ######

        #
        ##
        ###

#Solution:

# Copy here code of line function from previous exercise

def line(num, str):
    if str == "":
        str = "*"
        print(num*str)
    else:
        print(num*str[0])


def triangle(size):
    # You should call function line here with proper parameters
    for i in range(0, size+1):
        line(i, "#")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
