# E-8.4.1: Decreasing counter

# Problem: https://programming-22.mooc.fi/part-8/4-defining-methods#programming-exercise-decreasing-counter


# Sample output:


# Solution:


# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.initial = self.value

    def print_value(self):
        print("value:", self.value)


    # Write the rest of the methods here!

# Part 1 + 2:
    def decrease(self):
        if self.value > 0:
            self.value -= 1


# Part 3:

    def set_to_zero(self):
        self.value = 0


# Part 4:

    def reset_original_value(self):
        self.value = self.initial




if __name__ == '__main__':
    counter = DecreasingCounter(10)
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.set_to_zero()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()
