# E-8.1.1: The smallest average result


# Problem: https://programming-22.mooc.fi/part-8/1-objects-and-methods#programming-exercise-the-smallest-average-result


# Sample output:

#{'name': 'Larry', 'result1': 3, 'result2': 1, 'result3': 1}

# Solution:


# ref isinstance(): https://www.w3schools.com/python/ref_func_isinstance.asp#:~:text=The%20isinstance()%20function%20returns,the%20types%20in%20the%20tuple.
# ref zip(): https://realpython.com/python-zip-function/#:~:text=Python's%20zip()%20function%20is,%2C%20sets%2C%20and%20so%20on.

def smallest_average(person1: dict, person2: dict, person3: dict):
    p1 = 0
    p2 = 0
    p3 = 0
    studies = []

    while True:
        for value1, value2, value3 in zip(person1.values(), person2.values(), person3.values()):
            if isinstance(value1, int):
                p1 += value1
            if isinstance(value2, int):
                p2 += value2
            if isinstance(value3, int):
                p3 += value3

        studies.append(p1/3)
        studies.append(p2/3)
        studies.append(p3/3)

        if min(studies) == studies[0]:
            return person1
        if min(studies) == studies[1]:
            return person2
        else:
            return person3


if __name__ == '__main__':
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))
