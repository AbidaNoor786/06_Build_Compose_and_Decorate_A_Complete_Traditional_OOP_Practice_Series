# Define custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18"):
        super().__init__(message)

# Function that uses the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError()
    print("Age is valid.")

# Use try...except to handle the exception
try:
    check_age(16)
except InvalidAgeError as e:
    print(f"InvalidAgeError caught: {e}")
