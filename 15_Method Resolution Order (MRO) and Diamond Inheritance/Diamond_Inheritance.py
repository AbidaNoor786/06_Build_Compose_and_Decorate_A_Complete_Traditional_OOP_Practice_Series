class A:
    def show(self):
        print("Show method in class A")

class B(A):
    def show(self):
        print("Show method in class B")

class C(A):
    def show(self):
        print("Show method in class C")

class D(B, C):
    pass

# Create an object of class D
d = D()

# Call the show method
d.show()

# Print the Method Resolution Order
print(D.__mro__)
