# E-8.5.4: Series

# Problem: https://programming-22.mooc.fi/part-8/5-more-examples-of-classes#programming-exercise-series


# Sample output:



# Solution:

class Series:

    def __init__(self, title: str, num_of_seasons: int, genre : list):
        self.title = title
        self.num_of_seasons = num_of_seasons
        self.genre = genre
        self.rated = []


    def rate(self, rating: int):
        if rating >= 0 or rating <= 5:
            self.rated.append(rating)

    def average(self):
        return sum(self.rated)/ len(self.rated)

    def __str__(self):
        genres = ", ".join(self.genre)
        if self.rated:
            amount = len(self.rated)
            grade = self.average()
            return f"{self.title} ({self.num_of_seasons} seasons)\ngenres: {genres}\n {amount} ratings, average {grade:.1f} points"

        return f"{self.title} ({self.num_of_seasons} seasons)\ngenres: {genres}\nno ratings"

def minimum_grade(rating: float, series_list: list):
    list = []
    for i in series_list:
        if i.average() >= rating:
            list.append(i)

    return list

def includes_genre(genre: str, series_list: list):
    list = []
    for i in series_list:
        if genre in i.genre:
            list.append(i)

    return list



if __name__ == '__main__':
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
