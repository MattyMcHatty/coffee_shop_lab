class CoffeeShop:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def check_customer_age(self, customer_age):
        return customer_age >= 16

    def check_energy_level(self, customer_energy_level):
        return customer_energy_level < 10
        
    