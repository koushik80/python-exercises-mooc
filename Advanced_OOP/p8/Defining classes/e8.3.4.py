# E-8.3.4: The older book


# Problem: Please write a function named older_book(book1: Book, book2: Book)
# which takes two objects of type Book as its arguments.
# The function should print out a message with the details of whichever is the older. It should print out a different message if the two books were written in the same year.
# Please see the examples below.

#python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
#everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
#norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

#older_book(python, everest)
#older_book(python, norma)


# Sample output:

# High Adventure is older, it was published in 1956
# Fluent Python and Norma were published in 2015

# Solution:

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------


def older_book(book1: Book, book2: Book):
    if book1.year < book2.year:
        print(f'{book1.name} is older, it was published in {book1.year}')
    elif book2.year < book1.year:
        print(f'{book2.name} is older, it was published in {book2.year}')
    elif book1.year == book2.year:
        print(f'{book1.name} and {book2.name} were published in {book1.year}')
        # or were published in {book2.year}


if __name__ == '__main__':
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    older_book(python, everest)
    older_book(python, norma)
