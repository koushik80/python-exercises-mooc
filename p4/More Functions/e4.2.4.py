#E4.2.4: A square

#Problem: Please write a function named square,
#which prints out a square of characters, and takes two arguments.
#The first parameter specifies the length of the side of the square.
#The second parameter specifies the character used to draw the square.

#The function should call the function line from the exercise above for the actual printing out.
#Copy your solution to that exercise above the code for this exercise.
#Please don't change anything in the line function.

#Some examples:
        #square(5, "*")
        #print()
        #square(3, "o")


#Sample output:

        #*****
        #*****
        #*****
        #*****
        #*****

        #ooo
        #ooo
        #ooo

#Solution:

# Copy here code of line function from previous exercise

def line(num, str):
    if str == "":
        str = "*"
        print(num*str)
    else:
        print(num*str[0])


def square(size, character):
    # You should call function line here with proper parameters
    for i in range(0, size):
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
