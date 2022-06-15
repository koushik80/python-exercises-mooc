#E-3.2.13:Find the first substring

#Problem: Please write a program which asks the user to type in a string and a single character.
#The program then prints the first three character slice which begins with the character specified by the user.
#You may assume the input string is at least three characters long. The program must print out three characters,
#or else nothing.

#Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for.
#In that case nothing should be printed out,
#and there should not be any indexing errors when executing the program.

        #Please type in a word: mammoth
        #Please type in a character: m
        #mam

        #Please type in a word: banana
        #Please type in a character: n
        #nan

        #Please type in a word: tomato
        #Please type in a character: x

        #Please type in a word: python
        #Please type in a character: n

#Solution:

str = input("Please type in a word: ")
chrct = input("Please type in a character: ")
index = str.find(chrct)
l = len(str)

while True:
    if str[index] == chrct:
        print(str[index:3])
        break
    else:
        print()
