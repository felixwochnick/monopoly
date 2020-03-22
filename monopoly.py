'''
Monopoly game classes
by Felix Wochnick (2019)
'''

import random
import colour

def getHcolor(colorHEX):
    color = colour.Color(colorHEX)
    return color.get_hsl()[2]


class Player():
    """Player class"""

    def __init__(self, name: str, color: str, playerID: int, asset: int = 2000):
        self.name = name
        self.color = color
        self.playerID = playerID
        self.asset = asset
        self.property = []
        self.position: int = 0
        self.rolled = False
        self.haveDoublets = False
        self.rolledInt = 0
        self.intoPrison = False

    def move(self):
        cube1 = random.randint(1, 6)
        cube2 = random.randint(1, 6)
        event: str = None

        if self.position + cube1 + cube2 <= 39:
            self.position += cube1 + cube2
        elif self.position + cube1 + cube2 == 40:
            self.position = 0
            self.goONstart()
            event = 'goONstart'
        else:
            self.position += cube1 + cube2 - 40
            self.goOVERstart()
            event = 'goOVERstart'

        self.rolledInt = cube1 + cube2

        return [cube1, cube2, event]

    def moveTo(self, position: int, direct: bool = False):
        if direct is False and position < self.position:
            self.goOVERstart()
        elif position == 0:
            self.goONstart()

        self.position = position

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
            street.updateGroup()

    def sellStreet(self, street):
        if street in self.property:
            self.property.remove(street)
            self.asset += street.costs
            return True
        else:
            return False

    def getMonney(self, monney: int):
        self.asset += monney

    def loseMonney(self, monney: int):
        if self.asset < monney:
            self.asset -= monney
        else:
            self.asset -= monney

    def goINTOprison(self):
        self.moveTo(10, True)
        self.intoPrison = True

    def becomeFree(self):
        self.intoPrison = False
        self.loseMonney(50)


class Field():
    """Field class"""

    def __init__(self, name: str):
        self.name = name
        self.function = 'Field'


class FieldGroup():
    """FieldGroup"""

    def __init__(self, color: str, lenght: int = 3):
        self.color = color
        self.owners = lenght * [None]

    def haveSameOwners(self) -> bool:
        if len(self.owners) == 3:
            return self.owners[0] == self.owners[1] and self.owners[0] == self.owners[2]
        elif len(self.owners) == 4:
            return self.owners[0] == self.owners[1] and self.owners[0] == self.owners[2] and self.owners[0] == self.owners[3]
        else:
            return self.owners[0] == self.owners[1]

    def howMannySameOwner(self, owner: Player) -> int:
        x = 0

        for person in self.owners:
            if person == owner:
                x += 1

        return x


class Street(Field):
    """Street class"""

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
        self.stageOFexpension: int = 0  # 0: less than 2*/3 streets; 1: 2*/3 streets; 2: 1 house; 3: 2 houses; 4: 3 houses; 5: 4 houses; 6: 1 hotel;   ||  *: 1st/last street group & Factorys

        self.mortgage = mortgage

        self.streetGroup = streetGroup
        self.GroupPosition = GroupPosition

        self.isBought: bool = False
        self.owner: Player = None

    def upgrade(self):
        if self.streetGroup.haveSameOwners() and self.stageOFexpension <= 6:
            self.stageOFexpension += 1

    def downgrade(self):
        if (self.streetGroup.haveSameOwners() and self.stageOFexpension == 1) or self.stageOFexpension == 0:
            pass
        else:
            self.stageOFexpension -= 1

    def updateRent(self):
        if self.streetGroup.haveSameOwners() and self.stageOFexpension == 0:
            self.upgrade()

        if self.stageOFexpension == 0:
            self.currentRent = self.rent
        elif self.stageOFexpension == 1:
            self.currentRent = self.rent * 2
        # elif self.stageOFexpension == 3:
        #     self.currentRent = self.rentW1H
        # elif self.stageOFexpension == 4:
        #     self.currentRent = self.rentW2H
        # elif self.stageOFexpension == 5:
        #     self.currentRent = self.rentW3H
        # elif self.stageOFexpension == 6:
        #     self.currentRent = self.rentW4H
        # elif self.stageOFexpension == 3:
        #     self.currentRent = self.rentWH

    def updateGroup(self):
        self.streetGroup.owners[self.GroupPosition] = self.owner

    def payRent(self, player: Player):
        self.updateRent()
        self.owner.getMonney(self.currentRent)
        player.loseMonney(self.currentRent)


class TrainStation(Field):
    """Train Station class"""

    def __init__(self, name: str, trainStationGroup: FieldGroup, GroupPosition: int):
        super().__init__(name)
        self.function = 'AbleToBuyField'

        self.costs: int = 200
        self.rent1: int = 25
        self.rent2: int = 50
        self.rent3: int = 100
        self.rent4: int = 200

        self.currentRent = self.rent1

        self.mortgage = 100

        self.streetGroup = trainStationGroup
        self.GroupPosition = GroupPosition

        self.isBought: bool = False
        self.owner: Player = None

    def updateRent(self):
        numberOFtrainstations = self.streetGroup.howMannySameOwner(self.owner)

        if numberOFtrainstations == 1:
            self.currentRent = self.rent1
        elif numberOFtrainstations == 2:
            self.currentRent = self.rent2
        elif numberOFtrainstations == 3:
            self.currentRent = self.rent3
        elif numberOFtrainstations == 4:
            self.currentRent = self.rent4

    def updateGroup(self):
        self.streetGroup.owners[self.GroupPosition] = self.owner

    def payRent(self, player: Player):
        self.updateRent()
        self.owner.getMonney(self.currentRent)
        player.loseMonney(self.currentRent)


class Factory(Field):
    def __init__(self, name: str, factoryGroup: FieldGroup, GroupPosition: int):
        super().__init__(name)
        self.function = 'AbleToBuyField'

        self.costs: int = 150

        self.mortgage = 75

        self.streetGroup = factoryGroup
        self.GroupPosition = GroupPosition

        self.isBought: bool = False
        self.owner: Player = None

    def updateGroup(self):
        pass
        # self.streetGroup.owners[self.GroupPosition] = self.owner

    def payRent(self, player: Player):
        rent = player.rolledInt * 4
        self.owner.getMonney(rent)
        player.loseMonney(rent)
        return rent


class MonneyActionField(Field):
    """MonneyField."""
    def __init__(self, name: str, getMonney: int, loseMonney: int):
        super().__init__(name)
        self.function = 'ActionField'

        self.getMonney = getMonney
        self.loseMonney = loseMonney

    def action(self, player: Player):
        player.getMonney(self.getMonney)
        player.loseMonney(self.loseMonney)

class EventField(Field):
    def __init__(self):
        super().__init__('Ereignisfeld')
        self.function = 'ActionField'

    def action(player: Player):
        pass


class CommunityField(Field)
    def __init__(self):
        super().__init__('Gemeinschaftsfeld')
        self.function = 'ActionField'

    def action(player):
        pass
