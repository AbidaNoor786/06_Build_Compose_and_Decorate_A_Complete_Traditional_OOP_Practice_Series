class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The iterator is the object itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Example usage:
for number in Countdown(5):
    print(number)
