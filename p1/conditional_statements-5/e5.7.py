#E-5.7:Daily wages

#Problem: Please write a program which asks for the hourly wage, hours worked, and the day of the week.
#The program should then print out the daily wages, which equal hourly wage multiplied by hours worked,
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
option2 = "Sunday"
daily_wages = wage * work

if option == True:
    print("Daily wages:",daily_wages)
elif option2:
    print("Daily wages:",daily_wages * 2)

