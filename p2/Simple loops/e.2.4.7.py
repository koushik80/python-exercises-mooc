#E-2.4.7:Story

#Problem:

#Part 1:Please write a program which keeps asking the user for words.
#If the user types in end, the program should print out the story the words formed, and finish.

        #Please type in a word: Once
        #Please type in a word: upon
        #Please type in a word: a
        #Please type in a word: time
        #Please type in a word: there
        #Please type in a word: was
        #Please type in a word: a
        #Please type in a word: girl
        #Please type in a word: end
        #Once upon a time there was a girl

#Part 2:Change the program so that the loop ends also if the user types in the same word twice.

        #Please type in a word: It
        #Please type in a word: was
        #Please type in a word: a
        #Please type in a word: dark
        #Please type in a word: and
        #Please type in a word: stormy
        #Please type in a word: night
        #Please type in a word: night
        #It was a dark and stormy night

#Solution Part 1 + 2:

sentence = " "
temp_word = None

while True:
    word = input("Please type in a word: ")
    if word == "end":
        break
    if temp_word == word:
        break
    temp_word = word
    sentence += word + " "

print(sentence)

