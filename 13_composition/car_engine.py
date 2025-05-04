# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.
   
class Engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        return f"{self.type} engine is starting"

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def start_engine(self):
        return self.engine.start()

engine = Engine("W8")
car = Car("Honda", engine)
print(car.start_engine())      
                
    