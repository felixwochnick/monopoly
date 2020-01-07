import sys
import monpoly
import uiLib
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QGridLayout, QLineEdit, QGroupBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



class DisplayPlayer(monpoly.Player):
    def __init__(self, name: str, playerID: int):
        super().__init__(name, playerID)

    def printPROPERTY(self):
        for item in self.property:
            print(item.name + ' // ', end='')

        if self.property is not []:
            print()

    def getPOSITION(self):
        return game.map[self.position].name


class Game():
    """Maingame"""

    def __init__(self, numberOFplayers: int, nameOFplayers: list):
        self.players = []
        self.ActivePlayer: monpoly.Player

        while len(self.players) < numberOFplayers:
            self.players.append(DisplayPlayer(nameOFplayers[len(self.players)], len(self.players)))

        self.ActivePlayer = self.players[0]

        gruppeBraun = monpoly.FieldGroup('braun', 3)
        gruppeGrau = monpoly.FieldGroup('grau')
        gruppePink = monpoly.FieldGroup('pink')
        gruppeOrange = monpoly.FieldGroup('orange')
        gruppeRot = monpoly.FieldGroup('rot')
        gruppeGelb = monpoly.FieldGroup('gelb')
        gruppeGrün = monpoly.FieldGroup('grün')
        gruppeBlau = monpoly.FieldGroup('blau', 3)

        gruppeWerk = monpoly.FieldGroup('weiß', 3)
        gruppeBahnhof = monpoly.FieldGroup('weiß')

        self.map = [
            monpoly.Field('Los'),                                                                               # Los Feld

            monpoly.Street('Badstrasse', gruppeBraun, 0, 60, 2, 10, 30, 90, 160, 250, 50, 30),                  # Badstrasse
            monpoly.Field('Gemeinschaftsfeld'),                                                                 # Gemeinschaftsfeld
            monpoly.Street('Turmstrasse', gruppeBraun, 1, 60, 4, 20, 60, 180, 320, 450, 50, 30),                # Turmstrasse
            monpoly.Street('Stadionstrasse', gruppeBraun, 2, 80, 5, 30, 80, 240, 360, 500, 50, 40),             # Stadionstrasse
            monpoly.MonneyActionField('Einkommenssteuer Feld', 0, 200),                                         # Einkommenssteuer Feld

            monpoly.TrainStation('Südbahnhof', gruppeBahnhof, 0),                                               # Südbahnhof

            monpoly.Street('Chausseestrasse', gruppeGrau, 0, 100, 6, 30, 90, 270, 400, 550, 50, 50),            # Chausseestrasse
            monpoly.Street('Elisenstrasse', gruppeGrau, 1, 100, 6, 30, 90, 270, 400, 550, 50, 50),              # Elisenstrasse
            monpoly.Field('Ereignisfeld'),                                                                      # Ereignisfeld
            monpoly.Factory('Gaswerk', gruppeWerk, 0),                                                          # Gaswerk
            monpoly.Street('Poststrasse', gruppeGrau, 2, 100, 6, 30, 90, 270, 400, 550, 50, 50),                # Poststrasse
            monpoly.Street('Tiergartenstrasse', gruppeGrau, 2, 120, 8, 40, 100, 300, 450, 600, 50, 60),         # Tiergartenstrasse

            monpoly.Field('Nur zu Besuch'),                                                                     # Nur zu Besuch

            monpoly.Field('Auktion'),                                                                           # Aktion
            monpoly.Street('Seestrasse', gruppePink, 0, 140, 10, 50, 150, 450, 625, 750, 100, 70),              # Seestrasse
            monpoly.Street('Hafenstrasse', gruppePink, 1, 140, 10, 50, 150, 450, 625, 750, 100, 70),            # Hafenstrasse
            monpoly.Factory('Elektrizitätswerk', gruppeWerk, 1),                                                # Elektrizitätswerk
            monpoly.Street('Neue Strasse', gruppePink, 2, 140, 10, 50, 150, 450, 625, 750, 100, 70),            # Neue Strasse
            monpoly.Street('Marktplatz', gruppePink, 3, 160, 12, 60, 180, 500, 700, 900, 100, 80),              # Marktplatz

            monpoly.TrainStation('Westbahnhof', gruppeBahnhof, 1),                                              # Westbahnhof

            monpoly.Street('Münchner Strasse', gruppeOrange, 0, 180, 14, 70, 200, 550, 750, 950, 100, 90),      # Münchner Strasse
            monpoly.Field('Gemeinschaftsfeld'),                                                                 # Gemeinschaftsfeld
            monpoly.Street('Wiener Strasse', gruppeOrange, 1, 180, 14, 70, 200, 550, 750, 950, 100, 90),        # Wiener Strasse
            monpoly.Street('Berliner Strasse', gruppeOrange, 2, 200, 16, 80, 220, 600, 800, 1000, 100, 100),    # Berliner Strasse
            monpoly.Street('Hamburger Strasse', gruppeOrange, 3, 200, 16, 80, 220, 600, 800, 1000, 100, 100),   # Hamburger Strasse

            monpoly.Field('Frei Parken'),                                                                       # Frei Parken

            monpoly.Street('Theaterstrasse', gruppeRot, 0, 220, 18, 90, 250, 700, 875, 1050, 150, 100),         # Theaterstrasse
            monpoly.Field('Ereignisfeld'),                                                                      # Ereignisfeld
            monpoly.Street('Museumstrasse', gruppeRot, 1, 220, 18, 90, 250, 700, 875, 1050, 150, 100),          # Museumstrasse
            monpoly.Street('Opernplatz', gruppeRot, 2, 240, 20, 100, 300, 750, 925, 1100, 150, 120),            # Opernplatz
            monpoly.Street('Konzerthausstrasse', gruppeRot, 3, 240, 20, 100, 300, 750, 925, 1100, 150, 120),    # Konzerthausstrasse

            monpoly.Field('Bus'),                                                                               # Bus
            monpoly.TrainStation('Nordbahnhof', gruppeBahnhof, 2),                                              # Nordbahnhof

            monpoly.Street('Lessingstrasse', gruppeGelb, 0, 260, 22, 110, 330, 800, 975, 1150, 150, 130),       # Lessingstrasse
            monpoly.Street('Schillerstrasse', gruppeGelb, 1, 260, 22, 110, 330, 800, 975, 1150, 150, 130),      # Schillerstrasse
            monpoly.Factory('Wasserwerk', gruppeWerk, 2),                                                       # Wasserwerk
            monpoly.Street('Goethestrasse', gruppeGelb, 2, 280, 24, 120, 360, 850, 1025, 1200, 150, 140),       # Goethestrasse
            monpoly.Street('Rilkestrasse', gruppeGelb, 3, 280, 24, 120, 360, 850, 1025, 1200, 150, 140),        # Rilkestrasse

            monpoly.Field('Gefängnis'),                                                                         # Gefängnis

            monpoly.Street('Rathausplatz', gruppeGrün, 0, 300, 26, 130, 390, 900, 1100, 1275, 200, 150),        # Rathausplatz
            monpoly.Street('Hauptstrasse', gruppeGrün, 1, 300, 26, 130, 390, 900, 1100, 1275, 200, 150),        # Hauptstrasse
            monpoly.Street('Börsenplatz', gruppeGrün, 2, 300, 26, 130, 390, 900, 1100, 1275, 200, 150),         # Börsenplatz
            monpoly.Field('Gemeinschaftsfeld'),                                                                 # Gemeinschaftsfeld
            monpoly.Street('Bahnhofstraße', gruppeGrün, 3, 320, 28, 150, 450, 1000, 1200, 1400, 200, 160),      # Bahnhofstraße

            monpoly.TrainStation('Hauptbahnhof', gruppeBahnhof, 3),                                             # Hauptbahnhof
            monpoly.Field('Ereignisfeld'),                                                                      # Ereignisfeld

            monpoly.MonneyActionField('Geburtstaggeschenk', 100, 0),                                            # Geburtstaggeschenk
            monpoly.Street('Domplatz', gruppeBlau, 0, 350, 35, 175, 500, 1100, 1300, 1500, 200, 175),           # Domplatz
            monpoly.Street('Parkstrasse', gruppeBlau, 1, 350, 35, 175, 500, 1100, 1300, 1500, 200, 175),        # Parkstrasse
            monpoly.MonneyActionField('Zusatzsteuer', 0, 75),                                                   # Zusatzsteuer
            monpoly.Street('Schlossallee', gruppeBlau, 2, 400, 50, 200, 600, 1400, 1700, 2000, 200, 200),       # Schlossallee
        ]

    def mainLoop(self):
        for player in self.players:
            player.move()
            if type(self.map[player.position]) == monpoly.Street or type(self.map[player.position]) == monpoly.TrainStation:
                if self.map[player.position].isBought is False:
                    if input(self.map[player.position].name + ' kaufen? ') == 'Y':
                        player.buyStreet(self.map[player.position])

                elif self.map[player.position].isBought is True:
                    self.map[player.position].payRent(player)

            elif type(self.map[player.position]) == monpoly.MonneyActionField:
                self.map[player.position].action(player)

            player.printPOSITION()
            player.printASSET()
            player.printPROPERTY()
            commad = input('> Game ~~ ' + player.name + ' >> ')

            if commad == 'exit':
                sys.exit()

            print('')

        self.mainLoop()

    def changeActivePlayer(self):
        if self.ActivePlayer.playerID + 1 >= len(self.players):
            self.ActivePlayer = self.players[0]
        else:
            self.ActivePlayer = self.players[self.ActivePlayer.playerID + 1]

    def getActivePlayer(self):
        return self.ActivePlayer


class UIstart(QWidget):

    def __init__(self):
        super().__init__()

        self.buildUI()
        self.initUI()
        self.changePlayerNumber()

        self.show()

    def buildUI(self):
        self.setGeometry(100, 100, 400, 600)
        self.setWindowTitle('Monpoly starten')

        self.lblHeader = QLabel('Monpoly (v 0.1 Alpha)', self)
        self.lblHeader.setFont(QFont('Arial', 16))
        self.lblHeader.setAlignment(Qt.AlignTop)

        self.lblPlayerNumber = QLabel('Anzahl der Spieler: ', self)

        self.cboxPlayerNumber = QComboBox(self)
        self.cboxPlayerNumber.addItems(['2', '3', '4'])

        self.lblPlayerName0 = QLabel('Name des 1. Spielers: ', self)
        self.lblPlayerName1 = QLabel('Name des 2. Spielers: ', self)
        self.lblPlayerName2 = QLabel('Name des 3. Spielers: ', self)
        self.lblPlayerName3 = QLabel('Name des 4. Spielers: ', self)

        self.lePlayerName0 = QLineEdit(self)
        self.lePlayerName1 = QLineEdit(self)
        self.lePlayerName2 = QLineEdit(self)
        self.lePlayerName3 = QLineEdit(self)

        self.btnStart = QPushButton('Starten', self)

        self.layout = QGridLayout()
        self.layout.addWidget(self.lblHeader, 0, 0, 1, 2, Qt.AlignHCenter)

        self.layout.addWidget(self.lblPlayerNumber, 1, 0, 1, 1, Qt.AlignTop)
        self.layout.addWidget(self.cboxPlayerNumber, 1, 1, 1, 1, Qt.AlignTop)

        self.layout.addWidget(self.lblPlayerName0, 2, 0, 1, 1, Qt.AlignTop)
        self.layout.addWidget(self.lePlayerName0, 2, 1, 1, 1, Qt.AlignTop)

        self.layout.addWidget(self.lblPlayerName1, 3, 0, 1, 1, Qt.AlignTop)
        self.layout.addWidget(self.lePlayerName1, 3, 1, 1, 1, Qt.AlignTop)

        self.layout.addWidget(self.lblPlayerName2, 4, 0, 1, 1, Qt.AlignTop)
        self.layout.addWidget(self.lePlayerName2, 4, 1, 1, 1, Qt.AlignTop)

        self.layout.addWidget(self.lblPlayerName3, 5, 0, 1, 1, Qt.AlignTop)
        self.layout.addWidget(self.lePlayerName3, 5, 1, 1, 1, Qt.AlignTop)

        self.layout.addWidget(self.btnStart, 6, 0, 1, 2)

        self.setLayout(self.layout)


    def initUI(self):
        self.cboxPlayerNumber.currentIndexChanged.connect(self.changePlayerNumber)
        self.btnStart.clicked.connect(self.startGame)

    def changePlayerNumber(self):
        self.lblPlayerName0.hide()
        self.lePlayerName0.hide()

        self.lblPlayerName1.hide()
        self.lePlayerName1.hide()

        self.lblPlayerName2.hide()
        self.lePlayerName2.hide()

        self.lblPlayerName3.hide()
        self.lePlayerName3.hide()

        if self.cboxPlayerNumber.currentText() == '2':
            self.lblPlayerName0.show()
            self.lePlayerName0.show()

            self.lblPlayerName1.show()
            self.lePlayerName1.show()

        elif self.cboxPlayerNumber.currentText() == '3':
            self.lblPlayerName0.show()
            self.lePlayerName0.show()

            self.lblPlayerName1.show()
            self.lePlayerName1.show()

            self.lblPlayerName2.show()
            self.lePlayerName2.show()

        elif self.cboxPlayerNumber.currentText() == '4':
            self.lblPlayerName0.show()
            self.lePlayerName0.show()

            self.lblPlayerName1.show()
            self.lePlayerName1.show()

            self.lblPlayerName2.show()
            self.lePlayerName2.show()

            self.lblPlayerName3.show()
            self.lePlayerName3.show()



    def startGame(self):
        global uiMain, game
        game = Game(int(self.cboxPlayerNumber.currentText()), [self.lePlayerName0.text(), self.lePlayerName1.text(), self.lePlayerName2.text(), self.lePlayerName3.text()])
        uiMain = UImain()
        self.hide()
        uiMain.show()


class UImain(QWidget):

    def __init__(self):
        super().__init__()
        self.buildUI()
        self.initUI()

        self.ActivePlayer: monpoly.Player = game.getActivePlayer()

    def buildUI(self):
        self.setGeometry(100, 100, 1280, 720)
        self.setWindowTitle('Monpoly')

        # layoutAction

        self.layoutAction = QGridLayout()

        self.btnRoll = QPushButton('Würfeln', self)
        self.btnBuy = QPushButton('Kaufen', self)
        self.btnSell = QPushButton('Verkaufen', self)
        self.btnBuild = QPushButton('Baumenu', self)
        self.btnTrade = QPushButton('Handen', self)
        self.btnEnd = QPushButton('Zug beenden', self)

        self.layoutAction.addWidget(self.btnRoll, 0, 0)
        self.layoutAction.addWidget(self.btnBuy, 1, 0)
        self.layoutAction.addWidget(self.btnSell, 2, 0)
        self.layoutAction.addWidget(self.btnBuild, 3, 0)
        self.layoutAction.addWidget(self.btnTrade, 4, 0)
        self.layoutAction.addWidget(self.btnEnd, 5, 0)

        # gbPlayer0

        self.gbPlayer0 = uiLib.QPlayerGroupBox('Player 0')

        # gbPlayer1

        self.gbPlayer1 = QGroupBox('Player 1')

        # gbPlayer2

        self.gbPlayer2 = QGroupBox('Player 2')

        # gbPlayer3

        self.gbPlayer3 = QGroupBox('Player 3')

        # layout

        self.layout = QGridLayout()

        self.layout.addLayout(self.layoutAction, 0, 0, 2, 1)
        self.layout.addWidget(self.gbPlayer0, 0, 1)
        self.layout.addWidget(self.gbPlayer1, 1, 1)
        self.layout.addWidget(self.gbPlayer2, 0, 2)
        self.layout.addWidget(self.gbPlayer3, 1, 2)

        self.setLayout(self.layout)

    def initUI(self):
        self.btnRoll.clicked.connect(self.actionRoll)
        self.btnEnd.clicked.connect(self.actionEnd)

    def actionRoll(self):
        self.ActivePlayer.move()
        self.gbPlayer0.lblPositionV.setText(self.ActivePlayer.getPOSITION())

    def actionEnd(self):
        game.changeActivePlayer()
        self.ActivePlayer = game.getActivePlayer()
