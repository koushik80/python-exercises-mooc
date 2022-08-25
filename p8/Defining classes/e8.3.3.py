# E-8.3.3: Define class:Pet


# Problem: https://programming-22.mooc.fi/part-8/3-defining-classes#programming-exercise-define-class-pet


# Sample output:

# Fluffy
# dog
# 2017

# Solution:

class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth


def new_pet(name: str, species: str, year_of_birth: int):
    new_pet = Pet(name, species, year_of_birth)
    return new_pet


if __name__ == '__main__':
    fluffy = new_pet("Fluffy", "dog", 2017)
    print(fluffy.name)
    print(fluffy.species)
    print(fluffy.year_of_birth)
