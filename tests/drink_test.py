import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink('Midnite Black Coffee', 3.50, 2)

    def test_drink_has_name(self):
        self.assertEqual('Midnite Black Coffee', self.drink.name)