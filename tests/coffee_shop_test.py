import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffee_shop = CoffeeShop('The Double R Diner', 100.00)
        self.customer = Customer('Dale Cooper', 100.00, 35, 4)
        self.drink_1 = Drink('Midnite Black Coffee', 3.50, 2)
        self.drink_2 = Drink('Hemlock Tea', 1.99, 1)
        self.food = Food('Cherry Pie', 4.50, 3)
        self.coffee_shop.drinks = [{'beverage' : self.drink_1, 'stock' :5}, {'beverage' : self.drink_2, 'stock' : 15}]

    def test_coffee_shop_name(self):
        self.assertEqual('The Double R Diner', self.coffee_shop.name)

    def test_increase_till(self):
        self.coffee_shop.increase_till(2.50)
        self.assertEqual(102.50, self.coffee_shop.till)

    def test_check_customer_age(self):
        old_enough = self.coffee_shop.check_customer_age(self.customer.age)
        self.assertEqual(True, old_enough)

    def test_increase_energy_level(self):
        self.customer.increase_energy_level(self.drink_1.caffeine_level)
        self.assertEqual(6, self.customer.energy_level)

    def test_check_customer_energy_level(self):
        self.customer.energy_level = 11
        too_much_energy = self.coffee_shop.check_energy_level(self.customer.energy_level)
        self.assertEqual(False, too_much_energy)

    def test_decrease_customer_energy_level(self):
        self.customer.decrease_energy_level(self.food.rejuvination_level)
        self.assertEqual(1, self.customer.energy_level)

    def test_stock_value(self):
        stock_value = self.coffee_shop.stock_value(self.coffee_shop.drinks)
        self.assertEqual(47.35, stock_value)