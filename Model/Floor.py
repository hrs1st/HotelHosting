from Model.Room import Room


class Floor:

    def __init__(self, floorNum):
        self.floorNum = floorNum
        self.room1 = Room('ordinary')
        self.room2 = Room('highClass')
        self.room3 = Room('VIP')
        self.rooms = [self.room1, self.room2, self.room3]
