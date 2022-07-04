#E-4.4.1:The length of the longest in the list

#Problem:Please write a function named length_of_longest,
#which takes a list of strings as its argument.
#The function returns the length of the longest string.

            #my_list = ["first", "second", "fourth", "eleventh"]

            #result = length_of_longest(my_list)
            #print(result)
#------------------------------------------------------------------------------
            #my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

            #result = length_of_longest(my_list)
            #print(result)

#Sample output:

            #8
            #7

#Solution:

def length_of_longest(lst: list):
    longest_str = 0
    for i in lst:
        if len(i) > longest_str:
            longest_str = len(i)
    return longest_str


if __name__ == '__main__':
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)
