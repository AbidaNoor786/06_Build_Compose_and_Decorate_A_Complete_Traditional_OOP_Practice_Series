
class Person:
    def __init__(self, name):
        self.name = name

class Mother(Person):
    def __init__(self, name, chores):
        super().__init__(name)        
        self.chores = chores
    def display(self):
        print(f"Name: {self.name}, Chores: {self.chores}")

mother = Mother("Fatima", "Cooking")
mother.display()            
     