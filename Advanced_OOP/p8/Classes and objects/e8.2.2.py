# E-8.2.2: Shopping list


# Problem: https://programming-22.mooc.fi/part-8/2-classes-and-objects#programming-exercise-shopping-list


# Sample output:


# Solution:

# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------



def total_units(my_list: ShoppingList):
    count = 0
    for i in range(1, my_list.number_of_items()+1):
        item = my_list.item(i)
        amount = my_list.amount(i)
        count += my_list.amount(i)
        print(f"{item}: {amount} units")
    return count


if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)

    print(total_units(my_list))
