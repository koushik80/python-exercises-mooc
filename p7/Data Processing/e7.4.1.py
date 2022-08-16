# E-7.4.1: Handling JSON files

# Problem: https://programming-22.mooc.fi/part-7/4-data-processing#programming-exercise-handling-json-files


# Sample output:


# Solution:
import json


def print_persons(filename: str):
    with open(filename) as new_file:
        data = new_file.read()
    student_details = json.loads(data)

    for contents in student_details:
        name = contents['name']
        age = contents['age']
        hobbies = ", ".join(contents['hobbies'])
        print(f"{name} {age} years ({hobbies})")


if __name__ == '__main__':
    student = print_persons("file1.json")
    print(student)
