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
        name = "Gum"
        price = .75
        quantity = 20
        gum = Item(name, price, quantity)
        
        location = 0
        self.vendingMachine.addItem(gum,location)
        self.assertEqual(gum, self.vendingMachine.checkItem(location)) 

    def test_add_money(self):
        '''Tests how the machine handles adding money'''
        #add one dollar to the empty vending machine and the balance should be one.
        self.vendingMachine.addMoney(1)

        self.assertEqual(self.vendingMachine.pendingBalance, 1)

        #add one more dollar and pending balance should be 2
        self.vendingMachine.addMoney(1)
        
        self.assertEqual(self.vendingMachine.pendingBalance, 2)

if __name__ == '__main__':
    unittest.main()
