# E-6.1.4: Course grading, part 1

# Problem: https://programming-22.mooc.fi/part-6/1-reading-files#programming-exercise-course-grading-part-1


# Sample output:


# Solution:


if False:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

students = {}


with open(student_info) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "student_id":
            continue
        name = parts[1] + " " + parts[2].strip()
        students[parts[0]] = name

exercises = {}

with open(exercise_data) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "student_id":
            continue
        value = 0
        for i in range(1, len(parts)):
            value += int(len(parts[i]))
        exercises[parts[0]] = value

#print(("Student information: "), student_info)
#print(("Exercises completed: "), exercise_data)
print(students)
print(exercises)

for student_nr, name in students.items():
    print(f'{name} {exercises[student_nr]}')
