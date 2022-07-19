# E-6.1.7: Spell checker

# Problem: https://programming-22.mooc.fi/part-6/1-reading-files#programming-exercise-spell-checker


# Sample output:


# Solution:

def spellchecker():
    wordlist = []

    with open("wordlist.txt") as file:
        for word in file:
            word = word.replace("\n", "")
            wordlist.append(word)

    output = ""
    sentence = input("Write text: ")
    sentence = sentence.split()

    for word in sentence:
        if word.lower() not in wordlist:
            word = word.replace(word, f'*{word}*')

        if len(output) == 0:
            output += word
        else:
            output += " " + word

    print(output)


spellchecker()
