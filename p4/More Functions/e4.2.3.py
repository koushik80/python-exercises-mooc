#E4.2.3: A square of hashes

#Problem: Please write a function named square_of_hashes,
#which draws a square of hash characters.
#The function takes one argument, which determines the length of the side of the square.

#The function should call the function line from the exercise above for the actual printing out.
#Copy your solution to that exercise above the code for this exercise.
#Please don't change anything in the line function.

#Some examples:

        #square_of_hashes(5)
        #print()
        #square_of_hashes(3)

#Sample output:

        #####
        #####
        #####
        #####
        #####

        ###
        ###
        ###

#Solution:


def line(num, str):
    if str == "":
        str = "*"
        print(num*str)
    else:
        print(num*str[0])

def square_of_hashes(size):
    # You should call function line here with proper parameters
    for i in range(0, size):
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
