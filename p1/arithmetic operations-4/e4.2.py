#E-4.2: Name and age

#Problem:Please write a program which asks the user for their name and year of birth.
#The program then prints out a message as follows:

            #What is your name? Frances Fictitious
            #Which year were you born? 1990
            #Hi Frances Fictitious, you will be 31 years old at the end of the year 2021

#Solution:

name = input("What is your name?")
born = input("Which year were you born?")
birth_year = int(born)
print(f"Hi {name}, you will be {2021 - birth_year} years old at the end of the year 2021")
