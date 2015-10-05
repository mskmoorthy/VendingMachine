class Item(object):

    """Item is a simple class used in the vending machine"""

    def __init__(self, name=None, price=None, quantity=None):
        super(Item, self).__init__()
        self.name = name
        self.price = price
        self.quantity = int(quantity)

    def __str__(self):
        return "%s: \n\t%d at $%.2f" % (self.name, self.quantity, self.price)
    
    def __eq__(self, other):
        return self.name == other.name  and self.price == other.price

    def purchase(self):
        self.quantity -= 1 ## instead of -=1 error introduced by msk


class VendingMachine():

    """docstring for VendingMachine"""

    def __init__(self, itemCount):
        self.itemCount = itemCount
        self.pendingBalance = 0
        self.balance = 0
        self.items = [None] * itemCount

    def __str__(self):
        return "Vending Machine: \n\titemCount: %d \n\tBalance: $%.2f \n\tPending Balance: $%.2f " % (self.itemCount, self.balance, self.pendingBalance)

    def addItem(self, item, location):
        '''add an item to a location in the vending machine. If it was unsuccessful returns false'''
        if (abs(location) < self.itemCount) and self.items[location] == None:
            self.items[location] = item
            return True
        return False

    def checkItem(self, location):
        '''Returns the item that is in the given location'''
        if (abs(location) < self.itemCount):
            return self.items[location]
        return None

    def coinReturn(self):
        '''Returns the change that hasn't been used for a purchase'''
        returnBalance = self.pendingBalance
        self.pendingBalance = 0
        return returnBalance

    def addMoney(self, moneyInput):
        self.pendingBalance += moneyInput

    def purchase(self, location):
        item = self.items[location]

        if (self.pendingBalance >= item.price):
            item.purchase()
            self.balance += item.price
            self.pendingBalance -= item.price
            return item
        else:
            return None

if __name__ == '__main__':
    chips = Item("Chips", 1.95, 5)
    cookies = Item("Cookies", 1.75, 10)

    machine_1 = VendingMachine(4)
    machine_1.addItem(chips, 0)
    machine_1.addItem(cookies, 1)
    machine_1.addMoney(2)
    item = machine_1.purchase(1)
    print item
    print machine_1
    print machine_1.checkItem(1)
