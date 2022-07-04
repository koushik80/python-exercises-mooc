#E-4.4.1:Even numbers

#Problem:Please write a function named even_numbers,
#which takes a list of integers as an argument.
#The function returns a new list containing the even numbers from the original list.

        #my_list = [1, 2, 3, 4, 5]
        #new_list = even_numbers(my_list)
        #print("original", my_list)
        #print("new", new_list)

#Sample output:

        #original [1, 2, 3, 4, 5]
        #new[2, 4]

#Solution:

def even_numbers(lst: list):

    e_n = []

    for num in lst:
        if num % 2 == 0:
            e_n.append(num)
    return e_n


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)