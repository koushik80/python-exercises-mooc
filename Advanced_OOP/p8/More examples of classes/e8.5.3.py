# E-8.5.3: LunchCard

# Problem: https://programming-22.mooc.fi/part-8/5-more-examples-of-classes#programming-exercise-lunchcard


# Sample output:



# Solution:

class LunchCard:
    def __init__(self, initial_balance: float):
        self.balance = initial_balance

    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60

    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60

    def deposit_money(self, amount: int):
        if amount >= 0:
            self.balance += amount
        else:
            raise ValueError("You cannot deposit an amount of money less than zero")

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"


peters_card = LunchCard(20)
graces_card = LunchCard(30)

peters_card.eat_special()
graces_card.eat_lunch()

print("Peter:", peters_card)
print("Grace:", graces_card)

peters_card.deposit_money(20)
graces_card.eat_special()

print("Peter:", peters_card)
print("Grace:", graces_card)

peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)

print("Peter:", peters_card)
print("Grace:", graces_card)
