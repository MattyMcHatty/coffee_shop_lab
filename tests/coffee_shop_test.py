import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffee_shop = CoffeeShop('The Double R Diner', 100.00)
        self.customer = Customer('Dale Cooper', 100.00, 35, 4)
        self.drink = Drink('Midnite Black Coffee', 3.50, 2)

    def test_coffee_shop_name(self):
        self.assertEqual('The Double R Diner', self.coffee_shop.name)

    def test_increase_till(self):
        self.coffee_shop.increase_till(2.50)
        self.assertEqual(102.50, self.coffee_shop.till)

    def test_check_customer_age(self):
        old_enough = self.coffee_shop.check_customer_age(self.customer.age)
        self.assertEqual(True, old_enough)

    def test_increase_caffeine_level(self):
        self.customer.increase_caffeine_level(self.drink.caffeine_level)
        self.assertEqual(6, self.customer.energy_level)

    def test_check_customer_energy_level(self):
        self.customer.energy_level = 11
        too_much_energy = self.coffee_shop.check_energy_level(self.customer.energy_level)
        self.assertEqual(False, too_much_energy)

    