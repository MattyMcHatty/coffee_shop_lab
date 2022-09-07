import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer('Dale Cooper', 100.00, 35, 4)

    def test_decrease_wallet(self):
        self.customer.decrease_wallet(2.50)
        self.assertEqual(97.50, self.customer.wallet)