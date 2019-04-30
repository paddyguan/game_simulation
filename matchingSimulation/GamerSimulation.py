import numpy


# gamer base class, contain some static init method
class GamerBase:

    fightCapacityRange = [1, 100]
    count = 0
    distributionType = 0

    def __init__(self):
        self.fightCapacity = 0
        GamerBase.count += 1
        self.id = GamerBase.count

    def fix_fight_capacity(self):
        pass

    @staticmethod
    def init_gamers_capacity(gamersList):
        # Gaussian distribution
        if GamerBase.distributionType == 0:
            tmpRandom = numpy.random.normal(50, 30, GamerBase.count)

            for i in range(1, GamerBase.count+1):
                # tmpFightCapacity = tmpRandom[i] * GamerBase.fightCapacityRange[1]
                gamersList[i].fightCapacity = int(tmpRandom[i])


# define game property
class GamePropertyBase:
    propertyList = list()

    def __init__(self):
        self.attack = 0


if __name__ == '__main__':

    gamers = []

    for i in range(100):
        gamers[i] = GamerBase()

    GamerBase.init_gamers_capacity(gamers)

    for i in gamers:
        print(i.fightCapacity)

