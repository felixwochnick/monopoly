from PyQt5.QtWidgets import QLabel, QGridLayout, QGroupBox, QWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from monopoly import getHcolor
import monopoly


class QPlayerGroupBox(QGroupBox):
    """docstring for QPlayerGroupBox."""

    def __init__(self, title: str, color: str):
        super().__init__(title)

        self.layout = QGridLayout()

        self.lblName = QLabel('Name:')
        self.lblNameV = QLabel("")
        self.lblNameV.setStyleSheet('background-color: {}; color: {};'.format(color, 'white' if not color == '#f7d41a' else 'black'))
        self.lblNameV.setAlignment(Qt.AlignCenter)

        self.lblPosition = QLabel('Position:')
        self.lblPositionV = QLabel("")
        self.lblAsset = QLabel('Kapital:')
        self.lblAssetV = QLabel()
        # self.lblProperty = QLabel('Besitz:')
        # self.lblPropertyV = QLabel()
        self.lblPrison = QLabel('Im Gefängnis:')
        self.lblPrisonV = QLabel('Nein')

        self.layout.addWidget(self.lblName, 0, 0)
        self.layout.addWidget(self.lblNameV, 0, 1)
        self.layout.addWidget(self.lblPosition, 1, 0)
        self.layout.addWidget(self.lblPositionV, 1, 1)
        self.layout.addWidget(self.lblAsset, 2, 0)
        self.layout.addWidget(self.lblAssetV, 2, 1)
        # self.layout.addWidget(self.lblProperty, 3, 0)
        # self.layout.addWidget(self.lblPropertyV, 3, 1)
        self.layout.addWidget(self.lblPrison, 3, 0)
        self.layout.addWidget(self.lblPrisonV, 3, 1)

        self.setLayout(self.layout)

class Matchfield(QGroupBox):
    def __init__(self, game):
        super().__init__('Spielfeld')

        self.game = game
        self.matchfield = []

        self.fieldCards = 40 * [None]

        self.initUI()

    def initUI(self):
        self.layout = QGridLayout()

        x = 0
        y = 1
        z = 0
        for field in self.game.map:
            if x > 9:
                x = 0
                y += 1

            if field.function == 'AbleToBuyField':
                self.matchfield.append(Matchfield_SubField(field.name, field.streetGroup.color))
                self.fieldCards[z] = FieldCard(field)
                self.matchfield[z].btnField.clicked.connect(self.fieldCards[z].show)
            else:
                self.matchfield.append(Matchfield_SubField(field.name))


            self.layout.addWidget(self.matchfield[z], x, y)
            z += 1
            x += 1

        self.setLayout(self.layout)

    def refreshMatchfield(self):
        for i in self.matchfield:
            i.clearlblPlayer()

        for player in self.game.players:
            self.matchfield[player.position].changelblPlayer(player)

class Matchfield_SubField(QWidget):
    def __init__(self, name, color=''):
        super().__init__()
        self.lblStyle = 'background-color: {}; height: 3px; width: 100%; min-height: 3px; max-height: 3px;'
        self.initUI(name, color)

    def initUI(self, name, color):
        self.layout = QGridLayout()

        self.btnField = QPushButton(name, self)
        self.btnField.setStyleSheet('background-color: {}; border 0; color: {}; border-radius: 3px; padding: 3px;'.format('grey' if color == '' else color, 'white' if getHcolor(color) < 0.45 else 'black'))
        self.lblOwner = QLabel()
        self.lblOwner.setStyleSheet(self.lblStyle.format('white'))
        self.lblPlayer = QLabel()
        self.lblPlayer.setStyleSheet(self.lblStyle.format('white'))

        self.layout.addWidget(self.btnField, 1, 1)
        self.layout.addWidget(self.lblOwner, 2, 1)
        self.layout.addWidget(self.lblPlayer, 3, 1)

        self.setLayout(self.layout)

    def changelblOwner(self, owner):
        self.lblOwner.setStyleSheet(self.lblStyle.format(owner.color))

    def changelblPlayer(self, player):
        self.lblPlayer.setStyleSheet(self.lblStyle.format(player.color))

    def clearlblPlayer(self):
        self.lblPlayer.setStyleSheet(self.lblStyle.format('white'))

class FieldCard(QWidget):
    def __init__(self, field):
        super().__init__()
        self.field: monopoly.Field = field
        self.buildUI()

    def buildUI(self):
        self.setGeometry(100, 100, 250, 450)
        self.setWindowTitle(self.field.name)

        self.layout = QGridLayout()

        if type(self.field) == monopoly.Street:
            self.lblName = QLabel(self.field.name)
            self.lblName.setStyleSheet('background-color: {}; color: {};'.format(self.field.streetGroup.color, 'white' if getHcolor(self.field.streetGroup.color) < 0.45 else 'black'))
            self.lblName.setAlignment(Qt.AlignCenter)
            self.lblCosts = QLabel('Kaufpreis')
            self.lblCostsV = QLabel('¢ {}'.format(self.field.costs))
            self.lblCostsV.setAlignment(Qt.AlignRight)
            self.lblRent = QLabel('Miete')
            self.lblRentV = QLabel('¢ {}'.format(self.field.rent))
            self.lblRentV.setAlignment(Qt.AlignRight)
            self.lblRentW1H = QLabel('Mit 1 Haus')
            self.lblRentW1HV = QLabel('¢ {}'.format(self.field.rentW1H))
            self.lblRentW1HV.setAlignment(Qt.AlignRight)
            self.lblRentW2H = QLabel('Mit 2 Häusern')
            self.lblRentW2HV = QLabel('¢ {}'.format(self.field.rentW2H))
            self.lblRentW2HV.setAlignment(Qt.AlignRight)
            self.lblRentW3H = QLabel('Mit 3 Häusern')
            self.lblRentW3HV = QLabel('¢ {}'.format(self.field.rentW3H))
            self.lblRentW3HV.setAlignment(Qt.AlignRight)
            self.lblRentW4H = QLabel('Mit 4 Häusern')
            self.lblRentW4HV = QLabel('¢ {}'.format(self.field.rentW4H))
            self.lblRentW4HV.setAlignment(Qt.AlignRight)
            self.lblRentWH = QLabel('Mit Hotel')
            self.lblRentWHV = QLabel('¢ {}'.format(self.field.rentWH))
            self.lblRentWHV.setAlignment(Qt.AlignRight)
            self.lblMortgage = QLabel('Hypothekenwert')
            self.lblMortgageV = QLabel('¢ {}'.format(self.field.mortgage))
            self.lblMortgageV.setAlignment(Qt.AlignRight)
            self.lblCostsTObuild = QLabel('1 Haus kostet ¢ {}\n1 Hotel kostet ¢ {} plus 4 Häuser'.format(self.field.costsTObuild, self.field.costsTObuild))
            self.lblCostsTObuild.setAlignment(Qt.AlignCenter)
            self.lblRentInfo = QLabel('Wenn ein Spieler alle Grundstücke einer Farbgruppe besitzt, so ist die Miete auf dem unbebauten Grundstücken dieser Farbgruppe doppelt so hoch.')
            self.lblRentInfo.setAlignment(Qt.AlignCenter)
            self.lblRentInfo.setStyleSheet('max-width: 230px;')
            self.lblRentInfo.setWordWrap(True)

            self.layout.addWidget(self.lblName, 1, 1, 1, 2)
            self.layout.addWidget(self.lblCosts, 2, 1)
            self.layout.addWidget(self.lblCostsV, 2, 2)
            self.layout.addWidget(self.lblRent, 3, 1)
            self.layout.addWidget(self.lblRentV, 3, 2)
            self.layout.addWidget(self.lblRentW1H, 4, 1)
            self.layout.addWidget(self.lblRentW1HV, 4, 2)
            self.layout.addWidget(self.lblRentW2H, 5, 1)
            self.layout.addWidget(self.lblRentW2HV, 5, 2)
            self.layout.addWidget(self.lblRentW3H, 6, 1)
            self.layout.addWidget(self.lblRentW3HV, 6, 2)
            self.layout.addWidget(self.lblRentW4H, 7, 1)
            self.layout.addWidget(self.lblRentW4HV, 7, 2)
            self.layout.addWidget(self.lblRentWH, 8, 1)
            self.layout.addWidget(self.lblRentWHV, 8, 2)
            self.layout.addWidget(self.lblMortgage, 9, 1)
            self.layout.addWidget(self.lblMortgageV, 9, 2)
            self.layout.addWidget(self.lblCostsTObuild, 10, 1, 1, 2)
            self.layout.addWidget(self.lblRentInfo, 11, 1, 1, 2)

        elif type(self.field) == monopoly.TrainStation:
            self.icoTrain = QLabel()
            self.srcIconTrain = QPixmap("resources/icons/train.svg")
            self.srcIconTrain = self.srcIconTrain.scaledToWidth(60)
            self.srcIconTrain = self.srcIconTrain.scaledToHeight(60)
            self.icoTrain.setPixmap(self.srcIconTrain)
            self.icoTrain.setAlignment(Qt.AlignCenter)
            self.lblName = QLabel(self.field.name)
            self.lblName.setAlignment(Qt.AlignCenter)
            self.lblCosts = QLabel('Kaufpreis')
            self.lblCostsV = QLabel('¢ {}'.format(self.field.costs))
            self.lblCostsV.setAlignment(Qt.AlignRight)
            self.lblRent = QLabel('Miete')
            self.lblRentV = QLabel('¢ {}'.format(self.field.rent1))
            self.lblRentV.setAlignment(Qt.AlignRight)
            self.lblRent2 = QLabel('Wenn man 2 Bahnhöfe besitzt')
            self.lblRent2V = QLabel('¢ {}'.format(self.field.rent2))
            self.lblRent2V.setAlignment(Qt.AlignRight)
            self.lblRent3 = QLabel('Wenn man 3 Bahnhöfe besitzt')
            self.lblRent3V = QLabel('¢ {}'.format(self.field.rent3))
            self.lblRent3V.setAlignment(Qt.AlignRight)
            self.lblRent4 = QLabel('Wenn man 4 Bahnhöfe besitzt')
            self.lblRent4V = QLabel('¢ {}'.format(self.field.rent4))
            self.lblRent4V.setAlignment(Qt.AlignRight)
            self.lblMortgage = QLabel('Hypothekenwert')
            self.lblMortgageV = QLabel('¢ {}'.format(self.field.mortgage))
            self.lblMortgageV.setAlignment(Qt.AlignRight)
            self.lblRentInfo = QLabel('Mit Bahnhöfen verdoppeln sich die Mieten.')
            self.lblRentInfo.setAlignment(Qt.AlignCenter)
            self.lblRentInfo.setStyleSheet('max-width: 230px;')
            self.lblRentInfo.setWordWrap(True)

            self.layout.addWidget(self.icoTrain, 1, 1, 1, 2)
            self.layout.addWidget(self.lblName, 2, 1, 1, 2)
            self.layout.addWidget(self.lblCosts, 3, 1)
            self.layout.addWidget(self.lblCostsV, 3, 2)
            self.layout.addWidget(self.lblRent, 4, 1)
            self.layout.addWidget(self.lblRentV, 4, 2)
            self.layout.addWidget(self.lblRent2, 5, 1)
            self.layout.addWidget(self.lblRent2V, 5, 2)
            self.layout.addWidget(self.lblRent3, 6, 1)
            self.layout.addWidget(self.lblRent3V, 6, 2)
            self.layout.addWidget(self.lblRent4, 7, 1)
            self.layout.addWidget(self.lblRent4V, 7, 2)
            self.layout.addWidget(self.lblMortgage, 8, 1)
            self.layout.addWidget(self.lblMortgageV, 8, 2)
            self.layout.addWidget(self.lblRentInfo, 9, 1, 1, 2)

        elif type(self.field) == monopoly.Factory:
            self.icoFactory = QLabel()
            self.srcIconFactory = QPixmap("resources/icons/bulb.svg") if self.field.name == 'Elektrizitätswerk' else QPixmap("resources/icons/water_tap.svg") # Icon made by monkik from www.flaticon.com
            self.srcIconFactory = self.srcIconFactory.scaledToWidth(60)
            self.srcIconFactory = self.srcIconFactory.scaledToHeight(60)
            self.icoFactory.setPixmap(self.srcIconFactory)
            self.icoFactory.setAlignment(Qt.AlignCenter)
            self.lblName = QLabel(self.field.name)
            self.lblName.setAlignment(Qt.AlignCenter)
            self.lblCosts = QLabel('Kaufpreis')
            self.lblCostsV = QLabel('¢ {}'.format(self.field.costs))
            self.lblCostsV.setAlignment(Qt.AlignRight)
            self.lblRentInfo = QLabel('Wenn man Besitzer des Elektrizitätswerk ist, so ist die Miete 4-mal so hoch, wie die Augen auf den Würfeln sind.\n\nWenn man zwei Versorgungswerke besitzt, so ist die Miete 10-mal so hoch.') if self.field.name == 'Elektrizitätswerk' else QLabel('Wenn man Besitzer des Wasserwerks ist, so ist die Miete 4-mal so hoch, wie die Augen auf den Würfeln sind.\n\nWenn man zwei Versorgungswerke besitzt, so ist die Miete 10-mal so hoch.')
            self.lblRentInfo.setAlignment(Qt.AlignCenter)
            self.lblRentInfo.setStyleSheet('max-width: 230px;')
            self.lblRentInfo.setWordWrap(True)
            self.lblMortgage = QLabel('Hypothekenwert')
            self.lblMortgageV = QLabel('¢ {}'.format(self.field.mortgage))
            self.lblMortgageV.setAlignment(Qt.AlignRight)

            self.layout.addWidget(self.icoFactory, 1, 1, 1, 2)
            self.layout.addWidget(self.lblName, 2, 1, 1, 2)
            self.layout.addWidget(self.lblCosts, 3, 1)
            self.layout.addWidget(self.lblCostsV, 3, 2)
            self.layout.addWidget(self.lblRentInfo, 4, 1, 1, 2)
            self.layout.addWidget(self.lblMortgage, 5, 1)
            self.layout.addWidget(self.lblMortgageV, 5, 2)

        self.setLayout(self.layout)
