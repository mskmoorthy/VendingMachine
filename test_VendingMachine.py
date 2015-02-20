import unittest

from VendingMachine import *


class ItemTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_item(self):
        name = "Gum"
        price = .75
        quantity = 20
        self.item = Item(name, price, quantity)
        self.assertEqual(self.item.name, name)
        self.assertEqual(self.item.price, price)
        self.assertEqual(self.item.quantity, quantity)


class VendingMachineTestCase(unittest.TestCase):

    def setUp(self):
        self.vendingMachine = VendingMachine(5)

    def tearDown(self):
        pass

    def test_add_items(self):
        pass

if __name__ == '__main__':
    unittest.main()
