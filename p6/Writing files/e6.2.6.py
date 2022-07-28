# E-6.2.6: Word search


# Promlem: https://programming-22.mooc.fi/part-6/2-writing-files#programming-exercise-word-search


# Sample output:


# Solution:

def find_words(search_term: str):
    words_list = []
    with open("words.txt") as new_file:
        content = new_file.read()
        line = content.split()

        if search_term.endswith("*"):
            for word in line:
                if word.startswith(search_term[0: len(search_term) - 1]):
                    words_list.append(word)

        elif search_term.startswith("*"):
            for word in line:
                if word.endswith(search_term[1:]):
                    words_list.append(word)

        else:
            for word in line:
                if len(word) == len(search_term):
                    test_1 = []
                    test_2 = []
                    for i in range(len(search_term)):
                        if search_term[i] == '.':
                            continue
                        test_1.append(search_term[i])
                        test_2.append(word[i])
                    if test_1 == test_2 and word not in words_list:
                        words_list.append(word)
    return words_list


if __name__ == '__main__':
    print(find_words("*vokes"))
