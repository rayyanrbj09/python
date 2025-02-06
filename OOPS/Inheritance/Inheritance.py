class Vehicle:
    """A base class to represent a vehicle."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def vehicle_info(self):
        return f"{self.year} {self.make} {self.model}"

class FuelVehicle(Vehicle):
    """A class to represent a fuel-based vehicle."""
    def __init__(self, make, model, year, fuel_capacity):
        super().__init__(make, model, year)  # Corrected to only pass make, model, year
        self.fuel_capacity = fuel_capacity

    def fuel_info(self):
        return f"Fuel Capacity: {self.fuel_capacity} gallons"

class ElectricVehicle(Vehicle):
    """A class to represent an electric vehicle."""
    def __init__(self, make, model, year, battery_capacity=0 ):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def battery_info(self):
        return f"Battery Capacity: {self.battery_capacity} kWh"

class HybridVehicle(FuelVehicle, ElectricVehicle):
    """A class to represent a hybrid vehicle."""
    def __init__(self, make, model, year, fuel_capacity, battery_capacity):
        FuelVehicle.__init__(self, make, model, year, fuel_capacity)  # Correctly call FuelVehicle constructor
        ElectricVehicle.__init__(self, make, model, year, battery_capacity)  # Correctly call ElectricVehicle constructor
        
    def display_info(self):
        return f"{self.vehicle_info()}, {self.fuel_info()}, {self.battery_info()}"

# Create an object of FuelVehicle
fuel_car = FuelVehicle("Toyota", "Corolla", 2021, 13)

# Create an object of ElectricVehicle   
electric_car = ElectricVehicle("Tesla", "Model S", 2021, 100)

# Create an object of HybridVehicle
hybrid_car = HybridVehicle("Toyota", "Prius", 2021, 11, 8.8)

# Display information for the fuel car
print(f"This is the fuel car details : {fuel_car.vehicle_info()},  {fuel_car.fuel_info()}")

# Display information for the electric car
print(f"This is the electric car : {electric_car.vehicle_info()},{electric_car.battery_info()}")

# Display information for the hybrid car
print(f"This is the hybird car : {hybrid_car.vehicle_info()} {hybrid_car.display_info()}")
