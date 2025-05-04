
#2. Using cls
#Assignment:
#Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        print(f"Total objects created: {cls.count}")

object1 = Counter()
object2 = Counter()
object3 = Counter()
object4 = Counter()
Counter.get_count()            