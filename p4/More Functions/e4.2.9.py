#E4.2.9:Same characters

#Problem: Please write a function named same_chars,
#which takes one string and two integers as arguments.
#The integers refer to indexes within the string.
#The function should return True if the two characters at the indexes specified are the same.
#Otherwise, and especially if either of the indexes falls outside the scope of the string,
#the function returns False.

#Some examples of how the function is used:

# same characters m and m
#print(same_chars("programmer", 6, 7)) # True

# different characters p and r
#print(same_chars("programmer", 0, 4)) # False

# the second index is not within the string
#print(same_chars("programmer", 0, 12)) # False


#Solution:

def same_chars(s, int_1, int_2):

    i = len(s)
    if int_1 >= i and int_1 != int_2:
        return False
    if int_2 >= i and int_1 != int_2:
        return False
    elif s[int_1] != s[int_2]:
        return False
    elif s[int_1] == s[int_2]:
        return True


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
