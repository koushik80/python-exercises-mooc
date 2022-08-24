# E-8.2.1: List of years


# Problem: Please write a function named list_years(dates: list) which takes a list of date type objects as its argument.
#The function should return a new list,
#which contains the years in the original list in chronological order,
#from earliest to latest.

#An example of the function in action:

#date1 = date(2019, 2, 3)
#date2 = date(2006, 10, 10)
#date3 = date(1993, 5, 9)

#years = list_years([date1, date2, date3])
#print(years)

# Sample output:

#[1993, 2006, 2019]


# Solution:
from datetime import date


def list_years(dates: list):
    new_years_list = []

    for y in dates:
        dates = y.year
        new_years_list.append(dates)
    new_years_list.sort()

    return new_years_list


if __name__ == '__main__':
    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)

    years = list_years([date1, date2, date3])
    print(years)
