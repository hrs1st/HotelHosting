class Room:

    def __init__(self, roomType):
        self.roomType = roomType
        self.roomNum = 0
        self.roomPrice = self.calculateRoomPrice()
        self.isOccupied = False

    def calculateRoomPrice(self):

        if self.roomType == 'ordinary':
            return 100

        elif self.roomType == 'highClass':
            return 200

        elif self.roomType == 'VIP':
            return 300

