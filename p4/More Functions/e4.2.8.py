#E4.2.8:The greatest number

#Problem: Please write a function named greatest_number,
#which takes three arguments. The function returns the greatest in value of the three.

#An example of how the function is used:

#print(greatest_number(3, 4, 1)) # 4
#print(greatest_number(99, -4, 7)) # 99
#print(greatest_number(0, 0, 0)) # 0


#Solution:

def greatest_number(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)




#def greatest_number(x, y, z):
    #numbers = [x, y, z]
    #return max(numbers)


#if __name__ == "__main__":
    #greatest = greatest_number(5, 4, 8)
    #print(greatest)
