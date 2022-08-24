# E-8.3.2: Three classes


# Problem: https://programming-22.mooc.fi/part-8/3-defining-classes#programming-exercise-three-classes


# Sample output:


# Solution:

class Checklist:
    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries


class Customer:
    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount


class Cable:
    def __init__(self, model: str, length: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional
