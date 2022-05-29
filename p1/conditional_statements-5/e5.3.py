#E-5.3:Soup or no soup

#Problem: Please write a program which asks for the user's name.
#If the name is anything but "Jerry",
#the program then asks for the number of portions and prints out the total cost.
#The price of a single portion is 5.90.

#Two examples of the program's execution:

                #Please tell me your name: Kramer
                #How many portions of soup? 2
                #The total cost is 11.8
                #Next please!

                #Please tell me your name: Jerry
                #Next please!

#Solution:

name = str(input("Please tell me your name:"))

if name == "Jerry":
    print("Next please!")
if name != "Jerry":
    portion = int(input("How many portions of soup?"))
    price = portion * 5.90
    print("The total cost is", price)
    print("Next please!")



