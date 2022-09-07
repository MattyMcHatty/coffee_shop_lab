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
        
    def stock_value(self, drinks_list):
        total_value = 0
        for drink in drinks_list:
            total_value += drink["beverage"].price * drink["stock"]
        return total_value