#E4.2.6:A shape

#Problem:Please write a function named shape,
#which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it.
#The first parameter also specifies the width of a rectangle,
#while the third parameter specifies its height. The fourth parameter specifies the filler character of the rectangle.
#The function prints first the triangle, and then the rectangle below it.

#The function should call the function line from the exercise above for the actual printing out.
#Copy your solution to that exercise above the code for this exercise.
#Please don't change anything in the line function.

#Some examples:

        #shape(5, "X", 3, "*")
        #print()
        #shape(2, "o", 4, "+")
        #print()
        #shape(3, ".", 0, ",")


#Sample output:

        #X
        #XX
        #XXX
        #XXXX
        #XXXXX
        #*****
        #*****
        #*****

        #o
        #oo
        #++
        #++
        #++
        #++

        #.
        #..
        #...


#Solution:

# Copy here code of line function from previous exercise and use it in your solution

def line(num, str):
    if str == "":
        str = "*"
        print(num*str)
    else:
        print(num*str[0])


def shape(sqr_size, sqr_char, rect_size, rect_char):
    for i in range(0, sqr_size+1):
        line(i, sqr_char)

    for i in range(0, rect_size):
        line(sqr_size, rect_char)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "o")
