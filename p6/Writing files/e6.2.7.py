# E-6.2.7: Dictionary stored in a file


# Promlem:https://programming-22.mooc.fi/part-6/2-writing-files#programming-exercise-dictionary-stored-in-a-file


# Sample output:


# Solution:

def backup_dictionary():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        function = int(input("Function: "))

        if function == 1:
            fi = input("The word in Finnish: ")
            en = input("The word in English: ")
            with open("dictionary.txt", "a") as new_file:
                new_file.write(f'{str(fi)} - {str(en)}\n')
            print("Dictionary entry added")

        elif function == 2:
            search = input("Search term: ")
            with open("dictionary.txt") as new_file:
                for line in new_file:
                    if search.lower() in line.lower():
                        line = line.strip()
                        print(line)

        elif function == 3:
            print("Bye!")
            break


backup_dictionary()
