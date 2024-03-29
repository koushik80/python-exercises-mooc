# E-6.3.3: Incorrect lottery numbers

# Problem:The file lottery_numbers.csv containts winning lottery numbers in the following format:

# Sample data:

# week 1;5,7,11,13,23,24,30
# week 2
#9, 13, 14, 24, 34, 35, 37
# ...etc...


# Each line should contain a header week x, followed by seven integer numbers which are all between 1 and 39 inclusive.

# The file has been corrupted. Lines in the file may contain the following kinds of errors(these exact lines may not be present in the file, but errors in a similar format will be):

# The week number is incorrect:
# Sample data:
# week zzc;1,5,13,22,24,25,26


# One or more numbers are not correct:
# Sample data:
# week 22;1,**,5,6,13,2b,34


# Too few numbers:
# Sample data:
# week 13;4,6,17,19,24,33


# The numbers are too small or large:
# Sample data:
# week 39;5,9,15,35,39,41,105


# The same number appears twice:
# Sample data:
# week 41;5,12,3,35,12,14,36

# Please write a function named filter_incorrect(),
# which creates a file called correct_numbers.csv.
# The file should contain only those lines from the original file which are in the correct format.


# Solution:
def filter_incorrect():
    weeks = ""
    for i in range(1, 53):
        weeks += str(i)
    values = ""
    for i in range(1, 40):
        values += str(i)
    with open("lottery_numbers.csv") as new_file:
        correct = {}

        for line in new_file:
            all = {}
            line = line.replace('\n', '')
            parts = line.split(';')
            all[parts[0]] = parts[1]

            for week, numbers in all.items():
                if week[7:] not in weeks:
                    continue
            m = numbers.split(',')
            y = True
            z = []
            for i in m:
                if i not in values or len(m) != 7:
                    y = False
                    break
            for i in m:
                if i not in z:
                    z.append(i)
                else:
                    y = False
                    break
            if y == False:
                continue
            correct[week] = numbers

    with open("correct_numbers.csv", "w") as new_file:
        for week, lotteries in correct.items():
            new_file.write(f'{week} x;{lotteries}\n')
