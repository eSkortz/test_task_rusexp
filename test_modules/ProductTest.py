import unittest

from utils.Models import Product
from database.DatabaseUtils import get_markup, \
    get_percent_delivery, get_percent_logistics

class Test1(unittest.TestCase):

    def test_cost_price_calculation(self):
        product = Product(sid=1, category=2, name="Test Product", price=50)
        expected_cost_price = 50 + Product.OWN_EXPENSES + Product.SORTING + Product.COMISSION_FOR_RETURNS
        self.assertEqual(product.cost_price, expected_cost_price)

    def test_markup_calculation(self):
        product = Product(sid=1, category=2, name="Test Product", price=50)
        expected_markup = get_markup(cost_price=product.cost_price, category=product.category)
        self.assertEqual(product.markup, expected_markup)

    def test_logistics_calculation(self):
        product = Product(sid=1, category=2, name="Test Product", price=50)
        expected_logistics = product.cost_price * get_percent_logistics()
        self.assertEqual(product.logistics(), expected_logistics)

    def test_delivery_calculation(self):
        product = Product(sid=1, category=2, name="Test Product", price=50)
        expected_delivery = product.cost_price * get_percent_delivery()
        self.assertEqual(product.delivery(), expected_delivery)

    