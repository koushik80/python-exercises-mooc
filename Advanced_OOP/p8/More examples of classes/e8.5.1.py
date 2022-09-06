# E-8.5.1: Stopwatch

# Problem: https://programming-22.mooc.fi/part-8/5-more-examples-of-classes#programming-exercise-stopwatch


# Sample output:


# Solution:

class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0

    def __str__(self) -> str:
        return f"{self.minutes:02}:{self.seconds:02}"


if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()
