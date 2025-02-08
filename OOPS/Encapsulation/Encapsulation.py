"""
In this example, the `Employee` class encapsulates the `name` and `salary` attributes by making them private.
 Access to these attributes is provided through public getter and setter methods.
"""
class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private variable
        self.__salary = salary  # Private variable

    # Getter method for name
    def get_name(self):
        return self.__name
    
    # Setter method for name
    def set_name(self, name):
        self.__name = name
        
    # Getter method for salary
    def get_salary(self):
        return self.__salary
    
    # Setter method for salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError("Salary must be positive")

# Example usage
emp = Employee("John Doe", 50000)
print(emp.get_name())  # Output: John Doe
emp.set_salary(60000)
print(emp.get_salary())  # Output: 60000