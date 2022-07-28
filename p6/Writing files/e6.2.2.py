# E-6.2.2: Diary


# Promlem: https://programming-22.mooc.fi/part-6/2-writing-files#programming-exercise-diary


# Sample output:


# Solution:

def diary():
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        function = int(input("Function: "))

        if function == 1:
            entry = input("Diary entry: ")
            with open("diary.txt", "a") as new_file:
                new_file.write(f'{entry}\n')
            print("Diary saved")

        elif function == 2:
            print("Entries:")
            with open("diary.txt") as new_file:
                print(new_file.read())

        elif function == 0:
            print("Bye now!")
            break


diary()
