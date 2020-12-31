class Service:

    def __init__(self, serviceName):
        self.serviceName = serviceName
        self.serviceCost = self.calculateServiceCost()

    def calculateServiceCost(self):

        if self.serviceName == 'foodService':
            return 5

        elif self.serviceName == 'roomCleaning':
            return 10

        elif self.serviceName == 'laundry':
            return 7
