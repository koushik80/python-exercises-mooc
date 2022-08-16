# E-7.4.4: Who cheated, version 2

# Problem: https://programming-22.mooc.fi/part-7/4-data-processing#programming-exercise-who-cheated-version-2


# Sample output:


# Solution:

from datetime import datetime, timedelta
import csv


def final_points():
    with open("submissions.csv") as file:
        accnt = []
        for line in csv.reader(file, delimiter=";"):
            points = {}
            name = line[0]
            points[name] = [line[1], line[2], line[3]]
            accnt.append(points)
        accnt = remove_cheaters(accnt)
        return handled(accnt)


def remove_cheaters(times: dict):
    with open("start_times.csv") as start:
        non_cheating = []
        for line in csv.reader(start,  delimiter=";"):
            name = line[0]
            time = datetime.strptime(line[1], "%H:%M")
            for s_time in times:
                for id, exam in s_time.items():
                    if name == id:
                        if (datetime.strptime(exam[2], "%H:%M") - time) > timedelta(hours=3):
                            continue
                        right_student = {}
                        right_student[id] = exam
                        if right_student not in non_cheating:
                            non_cheating.append(right_student)
        return non_cheating


def handled(information: dict):
    with open("start_times.csv") as file:
        index = {}
        for line in csv.reader(file, delimiter=";"):
            name = line[0]
            index[name] = {}
            for notebook in information:
                for id, exam in notebook.items():
                    exam_num = exam[0]
                    exam_points = exam[1]

                    if line[0] == id:
                        if exam_num not in index[id]:
                            index[name][exam_num] = exam_points
                        if int(exam_points) > int(index[id][exam_num]):
                            index[name][exam_num] = exam_points
    final_score = {}
    print(index["erkki"])
    for id, task in index.items():
        total = 0
        for exam_num, grade in task.items():
            total += int(grade)
        final_score[id] = total
    return final_score


if __name__ == "__main__":
    final_points()
