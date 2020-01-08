'''
Monopoly game classes
by Felix Wochnick (2019)
'''

import random


class Player():
    """Player for monopoly"""

    def __init__(self, name: str, playerID: int, asset: int = 2000):
        self.name = name
        self.playerID = playerID
        self.asset = asset
        self.property = []
        self.position: int = 0
        self.rolled = False
        self.rolledInt = 0

    def move(self):
        cube1 = random.randint(1, 6)
        cube2 = random.randint(1, 6)

        if self.position + cube1 + cube2 <= 51:
            self.position += cube1 + cube2
        elif self.position + cube1 + cube2 == 52:
            self.position = 0
            self.goONstart()
        else:
            self.position += cube1 + cube2 - 52
            self.goOVERstart()

        self.rolledInt = cube1 + cube2

        return [cube1, cube2]

    def moveTo(self, position: int, direct: bool = False):
        self.position = position

        if direct is True:
            self.goOVERstart()
        elif direct is True and position == 0:
            self.goONstart()

        return True

    def goOVERstart(self):
        self.asset += 200

    def goONstart(self):
        self.asset += 400

    def buyStreet(self, street):
        if self.asset > street.costs and street.owner is None:
            self.asset -= street.costs
            self.property.append(street)
            street.isBought = True
            street.owner = self
            return True
        else:
            return False

    def sellStreet(self, street):
        if street in self.property:
            self.property.remove(street)
            self.asset += street.costs
            return True
        else:
            return False

    def getMonney(self, monney: int):
        self.asset += monney
        return True

    def loseMonney(self, monney: int):
        if self.asset < monney:
            self.asset -= monney
            return False
        else:
            self.asset -= monney
            return True


class Field():
    """Field class for Monopoly"""

    def __init__(self, name: str):
        self.name = name
        self.function = 'Field'

    def getSelf(self):
        return self


class FieldGroup():
    """FieldGroup"""

    def __init__(self, color: str, lenght: int = 4):
        self.color = color
        self.owners = lenght * [None]


class Street(Field):
    """Street class for Monopoly"""

    def __init__(self, name: str, streetGroup: FieldGroup, GroupPosition: int, costs: int, rent: int, rentW1H: int, rentW2H: int, rentW3H: int, rentW4H: int, rentWH: int, costsTObuild: int, mortgage: int):
        super().__init__(name)
        self.function = 'AbleToBuyField'

        self.costs = costs

        self.rent = rent
        self.rentW1H = rentW1H
        self.rentW2H = rentW2H
        self.rentW3H = rentW3H
        self.rentW4H = rentW4H
        self.rentWH = rentWH

        self.currentRent = self.rent

        self.costsTObuild = costsTObuild
        self.stageOFexpension: int = 0  # 0: less than 2*/3 streets; 1: 2*/3 streets; 2: 3*/4 streets; 3: 1 house; 4: 2 houses; 5: 3 houses; 6: 4 houses; 7: 1 hotel;   ||  *: 1st/last street group

        self.mortgage = mortgage

        self.streetGroup = streetGroup
        self.GroupPosition = GroupPosition

        self.isBought: bool = False
        self.owner: Player = None

    def upgrade(self):
        self.stageOFexpension += 1

    def downgrade(self):
        self.stageOFexpension -= 1

    def updateRent(self):
        if self.stageOFexpension == 1:
            self.currentRent = self.rent * 2
        elif self.stageOFexpension == 2:
            self.currentRent = self.rent * 3
        elif self.stageOFexpension == 3:
            self.currentRent = self.rentW1H
        elif self.stageOFexpension == 4:
            self.currentRent = self.rentW2H
        elif self.stageOFexpension == 5:
            self.currentRent = self.rentW3H
        elif self.stageOFexpension == 6:
            self.currentRent = self.rentW4H
        elif self.stageOFexpension == 3:
            self.currentRent = self.rentWH

    def payRent(self, player: Player):
        self.updateRent()
        self.owner.getMonney(self.currentRent)
        player.loseMonney(self.currentRent)


class TrainStation(Field):
    """docstring for Train Station."""

    def __init__(self, name: str, trainStationGroup: FieldGroup, GroupPosition: int):
        super().__init__(name)
        self.function = 'AbleToBuyField'

        self.costs: int = 200
        self.rent1: int = 25
        self.rent2: int = 50
        self.rent3: int = 100
        self.rent4: int = 200

        self.currentRent = self.rent1

        self.trainStationGroup = trainStationGroup
        self.GroupPosition = GroupPosition

        self.isBought: bool = False
        self.owner: Player = None

    def updateRent(self):
        return ''

        if self.stageOFexpension == 1:
            self.currentRent = self.rent * 2
        elif self.stageOFexpension == 2:
            self.currentRent = self.rent * 3
        elif self.stageOFexpension == 3:
            self.currentRent = self.rentW1H
        elif self.stageOFexpension == 4:
            self.currentRent = self.rentW2H
        elif self.stageOFexpension == 5:
            self.currentRent = self.rentW3H
        elif self.stageOFexpension == 6:
            self.currentRent = self.rentW4H
        elif self.stageOFexpension == 3:
            self.currentRent = self.rentWH

    def payRent(self, player: Player):
        self.updateRent()
        self.owner.getMonney(self.currentRent)
        player.loseMonney(self.currentRent)


class Factory(Field):
    def __init__(self, name: str, factoryGroup: FieldGroup, GroupPosition: int):
        super().__init__(name)
        self.function = 'AbleToBuyField'

        self.costs: int = 150

        self.factoryGroup = factoryGroup
        self.GroupPosition = GroupPosition

        self.isBought: bool = False
        self.owner: Player = None

    def payRent(self, player: Player):
        rent = player.rolledInt * 4
        self.owner.getMonney(rent)
        player.loseMonney(rent)


class MonneyActionField(Field):
    """docstring for MonneyField."""

    def __init__(self, name: str, getMonney: int, loseMonney: int):
        super().__init__(name)
        self.function = 'ActionField'

        self.getMonney = getMonney
        self.loseMonney = loseMonney

    def action(self, player):
        player.getMonney(self.getMonney)
        player.loseMonney(self.loseMonney)
