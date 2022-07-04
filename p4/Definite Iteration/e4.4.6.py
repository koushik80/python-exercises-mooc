#E-4.4.1:The sum of positive numbers

#Problem:Please write a function named sum_of_positives,
#which takes a list of integers as its argument.
#The function returns the sum of the positive values in the list.

        #my_list = [1, -2, 3, -4, 5]
        #result = sum_of_positives(my_list)
        #print("The result is", result)

#Sample output:

        #The result is 9

#Solution:

def sum_of_positives(lst :list):

    positive_num = []

    for i in lst:
        if i > 0:
            positive_num.append(i)
    return sum(positive_num)


if __name__ == '__main__':
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)