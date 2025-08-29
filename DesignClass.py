# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


# Derived class (Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.storage = storage
        self.__battery = battery   # Encapsulation (private attribute)

    def charge(self, amount):
        """Increase battery but max is 100%"""
        self.__battery = min(100, self.__battery + amount)
        return f"Battery charged to {self.__battery}%"

    def use(self, hours):
        """Decrease battery based on usage"""
        self.__battery = max(0, self.__battery - hours * 10)
        return f"Battery after usage: {self.__battery}%"

    def get_battery(self):
        """Getter for encapsulated battery"""
        return self.__battery


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", 80)
print(phone1.info())
print(phone1.charge(15))
print(phone1.use(3))
print("Battery Level:", phone1.get_battery())
