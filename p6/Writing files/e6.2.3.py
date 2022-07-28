# E-6.2.3: Filtering the contents of a file


# Promlem: https://programming-22.mooc.fi/part-6/2-writing-files#programming-exercise-filtering-the-contents-of-a-file


# Sample output:


# Solution:

def filter_solutions():
    name_of_student = []
    point = []
    problem = []
    result = []

    with open("solutions.csv") as new_file, open("correct.csv", "w") as correct, open("incorrect.csv", "w") as incorrect:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name_of_student.append(parts[0])
            point.append(parts[1])

            if '+' in parts[1]:
                points = parts[1].split("+")
                total = int(points[0]) + int(points[1])
                problem.append(total)
            elif '-' in parts[1]:
                points = parts[1].split("-")
                difference = int(points[0]) - int(points[1])
                problem.append(difference)
            result.append(int(parts[2]))

        for i in range(len(name_of_student)):
            if problem[i] == result[i]:
                correct.write(
                    f'{name_of_student[i]};{point[i]};{result[i]}\n')
            else:
                incorrect.write(
                    f'{name_of_student[i]};{point[i]};{result[i]}\n')


if __name__ == '__main__':
    filter_solutions()
