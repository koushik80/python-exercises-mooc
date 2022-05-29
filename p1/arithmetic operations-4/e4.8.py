#E-4.8: Food expenditure

#Problem: Please write a program which estimates a user's typical food expenditure.

#The program asks the user how many times a week they eat at the student cafeteria.
#Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

#Based on this information the program calculates the user's typical food expenditure both weekly and daily.

#The program should function as follows:

            #How many times a week do you eat at the student cafeteria? 4
            #The price of a typical student lunch? 2.5
            #How much money do you spend on groceries in a week? 28.5

            #Average food expenditure:
            #Daily: 5.5 euros
            #Weekly: 38.5 euros

#Solution:

eat_cafeteria = int(input("How many times a week do you eat at the student cafeteria?"))
price_lunch = float(input("The price of a typical student lunch?"))
spend_groceries = float(input("How much money do you spend on groceries in a week?"))

x = (spend_groceries + (eat_cafeteria * price_lunch)) / 7


print("Average food expenditure:")
print(f'Daily: {x} euros')
print(f'Weekly: {x * 7} euros')
