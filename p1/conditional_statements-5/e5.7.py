#E-5.7:Daily wages

#Problem: Please write a program which asks for the hourly wage, hours worked, and the day of the week.
#The program should then print out the daily wages,
#which equal hourly wage multiplied by hours worked,
#except on Sundays when the hourly wage is doubled.

            #Hourly wage: 8.5
            #Hours worked: 3
            #Day of the week: Monday
            #Daily wages: 25.5 euros

            #Hourly wage: 12.5
            #Hours worked: 10
            #Day of the week: Sunday
            #Daily wages: 250.0 euros

#Solution:

wage = float(input("Hourly wage:"))
work = int(input("Hours worked:"))
option = input("Day of the week:")
daily_wage = wage * work
dbl = 2 * daily_wage


def Monday(wage, work):
    return(wage * work)


def Tuesday(wage, work):
    return(wage * work)


def Wednesday(wage, work):
    return(wage * work)


def Thursday(wage, work):
    return(wage * work)


def Friday(wage, work):
    return(wage * work)


def Saturday(wage, work):
    return(wage * work)


def Sunday(wage, work):
    return((wage * work) * 2)


result = 0


if option == "Saturday":
    print("Daily wages:", daily_wage, "euros")
elif option == "Friday":
    print("Daily wages:", daily_wage, "euros")
elif option == "Monday":
    print("Daily wages:", daily_wage, "euros")
elif option == "Tuesday":
    print("Daily wages:", daily_wage, "euros")
elif option == "Wednesday":
    print("Daily wages:", daily_wage, "euros")
elif option == "Thursday":
    print("Daily wages:", daily_wage, "euros")
elif option == "Sunday":
    print("Daily wages:", dbl, "euros")
else:
    print()
