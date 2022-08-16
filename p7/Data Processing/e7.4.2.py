# E-7.4.2: Course statistics

# Problem: https://programming-22.mooc.fi/part-7/4-data-processing#programming-exercise-course-statistics


# Sample output:


# Solution:


import urllib.request
import certifi
import json
from math import floor
#import ssl

#Part: 1


def retrieve_all():
    #context = ssl._create_unverified_context()
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    request = urllib.request.urlopen(address, cafile=certifi.where())
    data = json.loads(request.read())
    list = []

    for valid in data:
        active = valid["enabled"]
        if active == False:
            continue
        course_name = valid["fullName"]
        name = valid["name"]
        year = valid["year"]
        assignments = sum(valid["exercises"])
        valid = course_name, name, year, assignments
        list.append(valid)
    return list

#Part: 2


def retrieve_course(course_name: str):
    address = " https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats"
    request = urllib.request.urlopen(address, cafile=certifi.where())
    data = json.loads(request.read())
    hours = 0
    exercises = 0
    students = 0

    for x, y in data.items():
        hours += y['hour_total']
        exercises += y['exercise_total']
        if y['students'] > students:
            students = y['students']

    hours_average = floor(hours/students)
    exercises_average = floor(exercises/students)

    return {
        'weeks': len(data),
        'students': students,
        'hours': hours,
        'hours_average': hours_average,
        'exercises': exercises,
        'exercises_average': exercises_average
    }


if __name__ == '__main__':
    print(retrieve_all())
    print(retrieve_course("docker2019"))
