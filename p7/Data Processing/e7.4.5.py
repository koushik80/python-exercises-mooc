# E-7.4.5: Spell checker, version 2

# Problem: https://programming-22.mooc.fi/part-7/4-data-processing#programming-exercise-spell-checker-version-2


# Sample output:


# Solution:

from difflib import get_close_matches


def spellchecker_v2():
    wordlist = []

    with open("wordlist.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            wordlist.append(line)

    list = []
    sentence = input("Write text: ")
    sentence = sentence.split()

    for word in sentence:
        if word.lower() in wordlist:
            list.append(word)
        else:
            word = word.replace(word, f'*{word}*')
            list.append(word)

    for wrd in list:
        print(wrd, end=" ")
    print("\nsuggestions:")

    proposals = {}
    for wrd in list:
        if wrd.startswith('*'):
            proposals[wrd[1:len(wrd)-1]
                      ] = get_close_matches(wrd[1:len(wrd)-1], wordlist)

    for wrd, proposal in proposals.items():
        p = ", ".join(proposal)
        print(f"{wrd}: {p}")


spellchecker_v2()
