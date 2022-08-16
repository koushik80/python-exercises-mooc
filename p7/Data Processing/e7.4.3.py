# E-7.4.3: Who cheated

# Problem: https://programming-22.mooc.fi/part-7/4-data-processing#programming-exercise-who-cheated


# Sample output:


# Solution:

from datetime import datetime, timedelta
import csv


def cheaters():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        starting_time = {}
        for line in csv.reader(start,  delimiter=";"):
            name = line[0]
            time = datetime.strptime(line[1], "%H:%M")
            starting_time[name] = time

        submission_time = {}
        for line in csv.reader(submission,  delimiter=";"):
            name = line[0]
            time = datetime.strptime(line[3], "%H:%M")

            if name not in submission_time:
                submission_time[name] = time
            elif time > submission_time[name]:
                submission_time[name] = time

        cheaters = []
        for name in starting_time:
            if submission_time[name] - starting_time[name] > timedelta(hours=3):
                cheaters.append(name)

        return cheaters


if __name__ == '__main__':
    print(cheaters())
