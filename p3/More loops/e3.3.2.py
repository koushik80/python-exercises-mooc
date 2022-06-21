#E-3.3.2: First letters of words

#Problem:Please write a program which asks the user to type in a sentence.
#The program then prints out the first letter of each word in the sentence, each letter on a separate line.

#An example of expected behaviour:

#Please type in a sentence: Humpty Dumpty sat on a wall
#H
#D
#s
#o
#a
#w

#Solution:

sentence = input("Please type in a sentence: ")
words = sentence.split()

for word in words:
    print(word[0])
else:
    print()
