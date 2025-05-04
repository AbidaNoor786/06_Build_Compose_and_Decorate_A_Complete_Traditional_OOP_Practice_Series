# 5. Static Variables and Static Methods
#Assignment:
#Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.


class MathUtils:
    @staticmethod
    def add(a, b, c):
        return a + b + c
    
result = MathUtils.add(5, 9, 7)
print(result)    