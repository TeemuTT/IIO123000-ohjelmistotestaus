# Unit test for basket.py

import unittest
import numbers
from basket import Basket

class BasketTests(unittest.TestCase):

    def setUp(self):
        print("setUp()")
        self.keijon_ostoskori = Basket("Keijo", ["Kissa", "Pasi"], 20)

    def tearDown(self):
        print("tearDown()")
        del self.keijon_ostoskori

    def test_customer_is_string(self):
        self.assertIsInstance(self.keijon_ostoskori.customer, str, "Variable customer should be string")

    def test_contents_is_list(self):
        self.assertIsInstance(self.keijon_ostoskori.contents, list, "Variable contents should be a list")

    def test_price_is_a_number(self):
        self.assertIsInstance(self.keijon_ostoskori.price, numbers.Number, "Variable price should be a number")

    def test_add_product(self):
        self.keijon_ostoskori.add_product("Kala", 5)
        self.assertIn("Kala", self.keijon_ostoskori.contents, "Product didn't get added to contents")

    def test_delete_product(self):
        self.keijon_ostoskori.delete_product("Kala", 5)
        self.assertNotIn("Kala", self.keijon_ostoskori.contents, "Product is still in contents")

if __name__ == '__main__':
    unittest.main()
