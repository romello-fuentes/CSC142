from abc import ABC, abstractmethod

# Part 1

class Item(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def calculate_cost(self):
        pass

# Part 2

class ByWeightItem(Item):
    def __init__(self, name, weight, cost_per_pound):
        super().__init__(name)
        self._weight = weight
        self._cost_per_pound = cost_per_pound

    def calculate_cost(self):
        return self._weight * self._cost_per_pound


class ByQuantityItem(Item):
    def __init__(self, name, quantity, cost_each):
        super().__init__(name)
        self._quantity = quantity
        self._cost_each = cost_each

    def calculate_cost(self):
        return self._quantity * self._cost_each

# Part 3

class Grapes(ByWeightItem):
    def __init__(self, weight):
        super().__init__("Grapes", weight, cost_per_pound=2.99)


class Bananas(ByWeightItem):
    def __init__(self, weight):
        super().__init__("Bananas", weight, cost_per_pound=0.79)


class Oranges(ByQuantityItem):
    def __init__(self, quantity):
        super().__init__("Oranges", quantity, cost_each=0.89)


class Cantaloupes(ByQuantityItem):
    def __init__(self, quantity):
        super().__init__("Cantaloupes", quantity, cost_each=3.49)

# Part 4

class Order:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def calculate_total(self):
        return sum(item.calculate_cost() for item in self._items)

    def get_items(self):
        return self._items

    def __len__(self):
        return len(self._items)

# Receipt

if __name__ == "__main__":
    order = Order()

    order.add_item(Grapes(1.5))       
    order.add_item(Bananas(2.0))      
    order.add_item(Oranges(4))         
    order.add_item(Cantaloupes(1))     

    print("Receipt:")
    for item in order.get_items():
        print(f"{item.name}: ${item.calculate_cost():.2f}")

    print("\nNumber of items:", len(order))
    print("Total cost: $", round(order.calculate_total(), 2))
