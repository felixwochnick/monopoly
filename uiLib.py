from PyQt5.QtWidgets import QLabel, QGridLayout, QGroupBox, QWidget, QPushButton
import colour


class QPlayerGroupBox(QGroupBox):
    """docstring for QPlayerGroupBox."""

    def __init__(self, title: str):
        super().__init__(title)

        self.layout = QGridLayout()

        self.lblName = QLabel('Name:')
        self.lblNameV = QLabel("")

        self.lblPosition = QLabel('Position:')
        self.lblPositionV = QLabel("")
        self.lblAsset = QLabel('Kapital:')
        self.lblAssetV = QLabel()
        self.lblProperty = QLabel('Besitz:')
        self.lblPropertyV = QLabel()
        self.lblPrison = QLabel('Im Gefängnis:')
        self.lblPrisonV = QLabel('Nein')

        self.layout.addWidget(self.lblName, 0, 0)
        self.layout.addWidget(self.lblNameV, 0, 1)
        self.layout.addWidget(self.lblPosition, 1, 0)
        self.layout.addWidget(self.lblPositionV, 1, 1)
        self.layout.addWidget(self.lblAsset, 2, 0)
        self.layout.addWidget(self.lblAssetV, 2, 1)
        self.layout.addWidget(self.lblProperty, 3, 0)
        self.layout.addWidget(self.lblPropertyV, 3, 1)
        self.layout.addWidget(self.lblPrison, 4, 0)
        self.layout.addWidget(self.lblPrisonV, 4, 1)

        self.setLayout(self.layout)

class Matchfield(QGroupBox):
    def __init__(self, game):
        super().__init__('Spielfeld')

        self.game = game
        self.matchfield = []

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

            # self.matchfield.append(QPushButton(field.name, self))
            # if field.function == 'AbleToBuyField':
            #    self.matchfield[z].setStyleSheet('background-color: {};'.format(field.streetGroup.color))

            if field.function == 'AbleToBuyField':
                self.matchfield.append(Matchfield_SubField(field.name, field.streetGroup.color))
            else:
                self.matchfield.append(Matchfield_SubField(field.name))


            self.layout.addWidget(self.matchfield[z], x, y)
            z += 1
            x += 1

        self.setLayout(self.layout)

class Matchfield_SubField(QWidget):
    def __init__(self, name, color=''):
        super().__init__()
        self.initUI(name, color)

    def initUI(self, name, color):
        self.layout = QGridLayout()

        self.btnField = QPushButton(name, self)
        self.btnField.setStyleSheet('background-color: {}; border 0; color: {}; border-radius: 3px; padding: 3px;'.format('grey' if color == '' else color, 'white' if self.getHcolor(color) < 0.45 else 'black'))
        self.lblOwner = QLabel()
        self.lblOwner.setStyleSheet('background-color: blue; height: 3px; width: 100%; min-height: 3px; max-height: 3px;')
        self.lblPlayer = QLabel()
        self.lblPlayer.setStyleSheet('background-color: red; height: 3px; width: 100%; min-height: 3px; max-height: 3px;')

        self.layout.addWidget(self.btnField, 1, 1)
        self.layout.addWidget(self.lblOwner, 2, 1)
        self.layout.addWidget(self.lblPlayer, 3, 1)

        self.setLayout(self.layout)

    def getHcolor(self, colorHEX):
        color = colour.Color(colorHEX)
        return color.get_hsl()[2]

    def changelblOwner(self, owner):
        pass

    def changelblPlayer(self, player):
        pass
