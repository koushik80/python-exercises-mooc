#E-4.4.1:The sum of lists

#Problem:Please write a function named list_sum which takes two lists of integers as arguments.
#The function returns a new list which contains the sums of the items at each index in the two original lists.
#You may assume both lists have the same number of items.

#An example of the function at work:

        #a = [1, 2, 3]
        #b = [7, 8, 9]
        #print(list_sum(a, b))  # [8, 10, 12]


#Sample output:


#Solution:

def list_sum(lst_1: list, lst_2: list):
    lst_3 = []

    for i in range(len(lst_1)):
        lst_3.append(lst_1[i] + lst_2[i])
    return lst_3


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))  # [8, 10, 12]
