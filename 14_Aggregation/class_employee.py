class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")


class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  # Aggregation: reference to an existing Employee object

    def display_info(self):
        print(f"Department: {self.name}")
        self.employee.display_info()


# Example usage:

# Create an Employee (independent of any Department)
emp1 = Employee("Alice", 101)

# Create a Department and associate the existing employee
dept1 = Department("HR", emp1)

# Display info
dept1.display_info()
