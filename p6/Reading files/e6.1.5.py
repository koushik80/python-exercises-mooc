# E-6.1.5: Course grading, part 2

# Problem: https://programming-22.mooc.fi/part-6/1-reading-files#programming-exercise-course-grading-part-2


# Sample output:


# Solution:
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")


#student_info = "students1.csv"
#exercise_data = "exercises1.csv"
#exam_points = "exam_points1.csv"

def grade(points):
    x = 0
    limits = [15, 18, 21, 24, 28]
    while x < 5 and points >= limits[x]:
        x += 1
    return x


def awarded_points(awarded):
    return awarded // 4


students = {}


with open("students1.csv") as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "student_id":
            continue
        name = parts[1] + " " + parts[2].strip()
        students[parts[0]] = name

exercises = {}

with open("exercises1.csv") as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "student_id":
            continue
        value = 0
        for i in range(1, len(parts)):
            value += int(len(parts[i]))
        exercises[parts[0]] = value


points = {}

with open("exam_points1.csv") as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "student_id":
            continue
        value = 0
        for j in range(1, len(parts)):
            value += int(len(parts[j]))
        points[parts[0]] = value


for exr_num, amount in exercises.items():
    sum_exam = points[exr_num] + awarded_points[amount]
    print(f'{students[exr_num]} {grade[sum_exam]}')
