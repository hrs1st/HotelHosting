from UI.MenuPrinter import *


class UserInterface:

    def __init__(self, hostingService):
        self.hostingService = hostingService
        self.roomsList = self.hostingService.roomsList

    def start(self):
        printStartMenu()

        while True:
            command = int(input())
            if command == 1:
                return self.employeeMainMenu()
            elif command == 2:
                return self.guestMainMenu()
            else:
                print('WRONG INPUT!')

    def employeeMainMenu(self):
        printEmployeeMainMenu()

        while True:
            command = int(input())
            if command == 0:
                return self.start()
            else:
                print('WRONG INPUT!')

    def guestMainMenu(self):
        printGuestMainMenu()

        while True:
            command = int(input())
            if command == 1:
                return self.showRoomsList()
            elif command == 2:
                return self.orderServices()
            elif command == 3:
                return self.showBill()
            else:
                print('WRONG INPUT!')

    def showRoomsList(self):
        printRoomsList(self.roomsList)

        while True:
            command = int(input())
            if command == 0:
                return self.guestMainMenu()

            for i in range(len(self.roomsList)+1):
                if command == i:
                    return self.roomOptions(i-1)

            print('WRONG INPUT!')

    def roomOptions(self, index):
        printGuestRoomOptions(self.roomsList, index)

        while True:
            command = int(input())
            if command == 1:
                return self.bookARoom(index+1)
            elif command == 0:
                return self.showRoomsList()
            elif command == 00:
                return self.guestMainMenu()

    def bookARoom(self, roomNum):
        self.hostingService.bookARoom(roomNum)
        printSuccessfulOperation()
        self.guestMainMenu()

    def orderServices(self):
        if self.hostingService.guest.guestName != '':
            printGuestServicesMenu()

            while True:
                command = int(input())
                if command == 1:
                    return self.orderFoodService()
                elif command == 2:
                    return self.orderRoomCleaning()
                elif command == 3:
                    return self.orderLaundry()
                elif command == 0:
                    return self.guestMainMenu()
                else:
                    print('WRONG INPUT!')
        else:
            print('<< you need to book a room first >>')
            self.guestMainMenu()

    def orderFoodService(self):
        self.hostingService.orderService('foodService')
        printSuccessfulOperation()
        self.guestMainMenu()

    def orderRoomCleaning(self):
        self.hostingService.orderService('roomCleaning')
        printSuccessfulOperation()
        self.guestMainMenu()

    def orderLaundry(self):
        self.hostingService.orderService('laundry')
        printSuccessfulOperation()
        self.guestMainMenu()

    def showBill(self):
        if self.hostingService.guest.guestName != '':
            billInfo = self.hostingService.generateGuestBill()
            printGuestBill(billInfo)

            while True:
                command = int(input())
                if command == 0:
                    self.guestMainMenu()
                else:
                    print('WRONG INPUT!')
        else:
            print('<< you need to book a room first >>')
            self.guestMainMenu()

# relations between hostingService & Menus
