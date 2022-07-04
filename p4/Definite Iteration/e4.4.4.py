#E-4.4.1:Anagrams

#Problem:Please write a function named anagrams,
#which takes two strings as arguments.
#The function returns True if the strings are anagrams of each other.
#Two words are anagrams if they contain exactly the same characters.

#Some examples of how the function should work:

#Sample output:

        #print(anagrams("tame", "meta")) # True
        #print(anagrams("tame", "mate"))  # True
        #print(anagrams("tame", "team"))  # True
        #print(anagrams("tabby", "batty"))  # False
        #print(anagrams("python", "java"))  # False


#Solution:

def anagrams(s_1: str, s_2: str):
    s_1 = sorted(s_1)
    s_2 = sorted(s_2)
    return s_1 == s_2


if __name__ == '__main__':
    print(anagrams("tame", "meta"))  # True
    print(anagrams("tame", "mate"))  # True
    print(anagrams("tame", "team"))  # True
    print(anagrams("tabby", "batty"))  # False
    print(anagrams("python", "java"))  # False
