

class GamerBase:

    count = 0
    distribution = 0

    def __init__(self):
        self.fightCapacity = 0
        GamerBase.count += 1
        self.id = GamerBase.count

    def setFightCapacity(self, value):
        self.fightCapacity = value

    def initGamersCapacity(self, gamersList):
        return



