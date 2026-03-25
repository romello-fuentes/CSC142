class Vehicle:
    def __init__(self, name, fuel_capacity, cost_per_gallon, mpg):
        self._name = name
        self._fuel_capacity = fuel_capacity
        self._cost_per_gallon = cost_per_gallon
        self._mpg = mpg

    @property
    def name(self):
        return self._name

    @property
    def range(self):
        return self._fuel_capacity * self._mpg

    @property
    def cost_per_mile(self):
        return self._cost_per_gallon / self._mpg


# List of vehicles 
v1 = Vehicle("Car", 15, 3.50, 30)
v2 = Vehicle("Motorcycle", 4, 3.50, 55)
v3 = Vehicle("Bus", 200, 3.50, 6)
v4 = Vehicle("Plane", 5000, 5.00, 0.2)

vehicles = [v1, v2, v3, v4]

# Sort
vehicles_sorted = sorted(vehicles, key=lambda v: v.cost_per_mile)

# Print table
print(f"{'Name':<15}{'Range':<15}{'Cost per Mile'}")
for v in vehicles_sorted:
    print(f"{v.name:<15}{v.range:<15.2f}${v.cost_per_mile:.4f}")
