from Model.Bill import Bill


class Guest:

    def __init__(self, guestName, guestId):
        self.guestName = guestName
        self.guestId = guestId
        self.guestRoomNum = 0
        self.guestBill = Bill()
