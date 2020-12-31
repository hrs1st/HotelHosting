class Bill:

    def __init__(self):
        self.cost = 0
        self.isPaid = False

    def addToBill(self, price=0):
        self.cost += price

    def omitFromBill(self, price=0):
        self.cost -= price

    def makeBillPaid(self):
        self.isPaid = True
