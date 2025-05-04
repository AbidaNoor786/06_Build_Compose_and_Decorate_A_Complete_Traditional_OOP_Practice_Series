class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create an instance with a factor
double = Multiplier(2)

# Test if the object is callable
print(callable(double))  # Output: True

# Use the object like a function
result = double(10)
print(result)  # Output: 20
