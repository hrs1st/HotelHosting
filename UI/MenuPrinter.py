def printStartMenu():
    print()
    print('     !!! WELCOME TO THE SERVICE APP !!!     ')
    print()
    print('Please choose your position: ')
    print('Employee: enter 1')
    print('Guest: enter 2')


def printEmployeeMainMenu():
    print()
    print('Employee Hosting Service: COMING SOON!')
    print('enter 0 to get back')
    # print('enter 1 to add a guest')
    # print('enter 2 to view a guest\'s details')
    # print('enter 3 to view rooms list')


def printGuestMainMenu():
    print()
    print('enter 1 to see the rooms list')
    print('enter 2 to order a service')
    print('enter 3 to see your bill')


def printRoomsList(roomsList):
    print()
    for i in range(len(roomsList)):
        status = ''
        if roomsList[i].isOccupied:
            status = 'full'
        else:
            status = 'empty'

        print(f'{i + 1}) Room {roomsList[i].roomNum} --> status: {status}')

    print('\nenter index of a room for its options')
    print('enter 0 to go back')


def printGuestRoomOptions(roomsList, num):
    print()
    print(f'Room Number: {roomsList[num].roomNum}\n'
          f'Room Type: {roomsList[num].roomType}\n'
          f'Price for one night: {roomsList[num].roomPrice}$\n'
          f'is Room Occupied: {roomsList[num].isOccupied}\n')

    if not roomsList[num].isOccupied:
        print('enter 1 to book the room')
    else:
        print('<< the room is already booked >>')

    print('enter 0 to go back')
    print('enter 00 to go to the mainMenu')


def printEmployeeRoomOptions(roomsList, num):
    pass


def printGuestServicesMenu():
    print()
    print('enter 1 to order food Service')
    print('enter 2 to order room cleaning service')
    print('enter 3 to order laundry service')
    print()
    print('enter 0 to go back')


def printGuestBill(billInfo):
    print()
    print(f'your bill balance: {billInfo[0]}$')
    print(f'your bill is << {billInfo[1]} >>')
    print()
    print('enter 0 to go back')


def printSuccessfulOperation():
    print('\nsuccessful Operation!')

# build and print menus
