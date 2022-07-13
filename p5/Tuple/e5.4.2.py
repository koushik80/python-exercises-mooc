# E-5.4.2: The oldest person

# Problem: Please write a function named oldest_person(people: list),
# which takes a list of tuples as its argument. In each tuple,
# the first element is the name of a person, and the second element is their year of birth.
# The function should find the oldest person on the list and return their name.

# An example of the function in action:

#p1 = ("Adam", 1977)
#p2 = ("Ellen", 1985)
#p3 = ("Mary", 1953)
#p4 = ("Ernest", 1997)
#people = [p1, p2, p3, p4]

# print(oldest_person(people))


# Sample output:

# Mary


# Solution:

def oldest_person(people: list):

    oldest_person = ()

    for person in people:
        l = len(oldest_person)
        if l == 0:
            oldest_person = people[0]
        elif l > 0:
            if person[1] < oldest_person[1]:
                oldest_person = person

    return oldest_person[0]


if __name__ == '__main__':
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))
