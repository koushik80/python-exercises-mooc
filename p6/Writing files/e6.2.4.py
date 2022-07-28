# E-6.2.4: Store personal data


# Promlem:https://programming-22.mooc.fi/part-6/2-writing-files#programming-exercise-store-personal-data


# Sample output:


# Solution:

def store_personal_data(person: tuple):
    with open("people.csv", "w") as new_file:
        Name = person[0]
        Age = int(person[1])
        Height = float(person[2])
        new_file.write(f'{Name};{Age};{Height}')


if __name__ == '__main__':
    ("Paul Paulson", 37, 175.5)
