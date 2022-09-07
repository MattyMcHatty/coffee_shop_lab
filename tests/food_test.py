import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food('Cherry Pie', 4.50, 3)

    def test_food_name(self):
        self.assertEqual('Cherry Pie', self.food.name)