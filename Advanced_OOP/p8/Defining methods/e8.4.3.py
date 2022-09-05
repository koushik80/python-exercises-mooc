# E-8.4.3: Statistics on numbers

# Problem: https://programming-22.mooc.fi/part-8/4-defining-methods#programming-exercise-statistics-on-numbers


# Sample output:

# Numbers added: 4

# Solution:


class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if len(self.numbers) == 0:
            return 0
        else:
            return sum(self.numbers) / len(self.numbers)


print("Please type in integer numbers: ")
stats = NumberStats()
even_num = NumberStats()
odd_num = NumberStats()

while True:
    input_num = int(input(""))

    if input_num == -1:
        print(f'Sum of numbers: {stats.get_sum()}')
        print(f'Mean of numbers: {stats.average()}')
        print(f'Sum of even numbers: {even_num.get_sum()}')
        print(f'Sum of odd numbers: {odd_num.get_sum()}')
        break
    else:
        if input_num % 2 == 0:
            even_num.add_number(input_num)
        elif input_num % 2 != 0:
            odd_num.add_number(input_num)

    stats.add_number(input_num)



stats = NumberStats()
stats.add_number(3)
stats.add_number(5)
stats.add_number(1)
stats.add_number(2)
print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
