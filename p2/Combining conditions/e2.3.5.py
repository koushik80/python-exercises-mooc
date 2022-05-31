#E-2.3.5:Leap year

#problem:Generally, any year that is divisible by four is a leap year.
#However, if the year is additionally divisible by 100,
# it is a leap year only if it also divisible by 400.

#Please write a program which asks the user for a year,
#and then prints out whether that year is a leap year or not.

#Some examples:

#Please type in a year: 2011
#That year is not a leap year.

#Please type in a year: 2020
#That year is a leap year.

#Please type in a year: 1800
#That year is not a leap year.

#Solution:

year = int(input("Please type in a year: "))

l_year = 0

if year % 100 == 0:
    if year % 400 == 0:
        l_year = True
elif year % 4 == 0:
    l_year = True

if l_year:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")


