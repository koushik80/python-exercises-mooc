# E-9.1.2: Passing submissions

# Problem: https://programming-22.mooc.fi/part-9/1-objects-and-references#programming-exercise-passing-submissions

# Sample output:

#ExamSubmission (examinee: Pippa, points: 19)
#ExamSubmission (examinee: Paul, points: 15)
#ExamSubmission (examinee: Persephone, points: 17)

# Solution:
# Write your solution after the class ExamSubmission
# Do not make changes to the class!


class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

    def __str__(self):
        return f'ExamSubmission (examinee: {self.examinee}, points: {self.points})'

# # WRITE YOUR SOLUTION HERE:

def passed(submissions: list, lowest_passing: int):
    passed_examinee = []

    for submission in submissions:
        if submission.points >= lowest_passing:
            passed_examinee.append(submission)
    return passed_examinee



if __name__ == "__main__":
    s1 = ExamSubmission("Peter", 12)
    s2 = ExamSubmission("Pippa", 19)
    s3 = ExamSubmission("Paul", 15)
    s4 = ExamSubmission("Phoebe", 9)
    s5 = ExamSubmission("Persephone", 17)

    passes = passed([s1, s2, s3, s4, s5], 15)
    for passing in passes:
        print(passing)
