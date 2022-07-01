#E4.3.8: The range of a list

#Problem:Please write a function named range_of_list,
#which takes a list of integers as an argument.
#The function returns the difference between the smallest and the largest value in the list.

        #my_list = [1, 2, 3, 4, 5]
        #result = range_of_list(my_list))
        #print("The range of the list is", result)



#Sample output:

        #The range of the list is 4

#Solution:

def range_of_list(my_list):
    return max(my_list) - min(my_list)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(f'The range of the list is {result}')
