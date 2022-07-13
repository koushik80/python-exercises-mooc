# E-5.3.9: Find movies

# Problem: Please write a function named find_movies(database: list, search_term: str),
# which processes the movie database created in the previous exercise.
# The function should formulate a new list,
# which contains only the movies whose title includes the word searched for.
# Capitalisation is irrelevant here.
# A search for ana should return a list containing both Anaconda and Management.

# An example of its use:

# database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
# {"name": "Pythons on a Plane", "director": "Renny Pytholin",
# "year": 2001, "runtime": 94},
# {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

#my_movies = find_movies(database, "python")
# print(my_movies)


# Sample output:

# [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
# {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]

# Solution:

def add_movie(database: list, name: str, director: str, year: int, runtime: int):

    dictionary = {}
    n = "name"
    d = "director"
    y = "year"
    r = "runtime"

    dictionary[n] = "name"
    dictionary[d] = "director"
    dictionary[y] = "year"
    dictionary[r] = "runtime"
    database.append(dictionary)


def find_movies(database: list, search_term: str):

    my_movies = []

    for dictionary in database:
        if search_term.lower() in dictionary["name"].lower():
            my_movies.append(dictionary)

    return my_movies


if __name__ == '__main__':
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
                {"name": "Pythons on a Plane", "director": "Renny Pytholin",
                    "year": 2001, "runtime": 94},
                {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)
