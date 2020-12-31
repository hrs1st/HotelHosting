from Model.Floor import Floor
from Model.Room import Room
from Model.Guest import Guest
from Model.Service import Service


class HostingService:

    def __init__(self):
        self.guest = Guest('', 0)
        self.roomsList = []
        self.floors = []
        for i in range(5):
            floor = Floor(i + 1)
            self.floors.append(floor)
        self.setRooms()

    def setRooms(self):
        for i in range(len(self.floors)):
            room1 = Room('ordinary')
            room2 = Room('highClass')
            room3 = Room('VIP')
            self.roomsList.append(room1)
            self.roomsList.append(room2)
            self.roomsList.append(room3)
        self.setRoomNums()

    def setRoomNums(self):
        for i in range(len(self.roomsList)):
            self.roomsList[i].roomNum = 100 + i

    def bookARoom(self, roomNum):
        guestInfo = self.getNameAndIDFromGuest()
        self.guest.guestName = guestInfo[0]
        self.guest.guestId = guestInfo[1]
        self.guest.guestRoomNum = roomNum

        roomPrice = self.roomsList[roomNum - 1].roomPrice
        self.guest.guestBill.addToBill(roomPrice)

        self.roomsList[roomNum - 1].isOccupied = True
        # TODO save info in system file

    def getNameAndIDFromGuest(self):
        guestName = input('please enter your Name: ')
        guestId = int(input('please enter your ID number: '))
        guestInfo = [guestName, guestId]
        return guestInfo

    def orderService(self, serviceName):
        service = Service(serviceName)
        serviceCost = service.serviceCost
        self.guest.guestBill.addToBill(serviceCost)

    def generateGuestBill(self):
        bill = self.guest.guestBill

        status = ''
        if bill.isPaid:
            status = 'Paid'
        else:
            status = 'Not Paid'

        billInfo = [bill.cost, status]

        return billInfo

# hostingService operations
