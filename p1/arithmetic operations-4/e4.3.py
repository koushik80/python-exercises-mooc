#E-4.3:Seconds in a day

#Problem:Please write a program which asks the user for a number of days.
#The program then prints out the number of seconds in the amount of days given.

#The program should function as follows:


            #How many days? 1
            #Seconds in that many days: 86400

#Solution:

days = int(input("How many days? "))
hours = 24
mins = 60
secs = 60
total = days * hours * mins * secs
print(f"Seconds in that many days: {total}")

