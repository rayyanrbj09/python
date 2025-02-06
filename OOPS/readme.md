# Object-Oriented Programming (OOP) in Python

## Classes and Objects

### Classes
A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. Classes encapsulate data and functions that operate on the data.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
```

### Objects
An object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created.

```python
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # Output: 2020 Toyota Corolla
```

### Blueprint
A class serves as a blueprint for objects. It defines the structure and behavior that the objects created from the class will have.

```python
# Blueprint: Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Creating objects from the blueprint
car1 = Car("Honda", "Civic", 2019)
car2 = Car("Ford", "Mustang", 2021)

car1.display_info()  # Output: 2019 Honda Civic
car2.display_info()  # Output: 2021 Ford Mustang
```