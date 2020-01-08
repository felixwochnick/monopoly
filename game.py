import sys
import monpoly
import uiLib
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QGridLayout, QLineEdit, QMessageBox, QTextEdit
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

    def checkPlayerHaveNames(self):
        if self.cboxPlayerNumber.currentText() == '2':
            if self.lePlayerName0.text() == '' or self.lePlayerName1.text() == '':
                return False

        elif self.cboxPlayerNumber.currentText() == '3':
            if self.lePlayerName0.text() == '' or self.lePlayerName1.text() == '' or self.lePlayerName2.text() == '':
                return False

        elif self.cboxPlayerNumber.currentText() == '4':
            if self.lePlayerName0.text() == '' or self.lePlayerName1.text() == '' or self.lePlayerName2.text() == '' or self.lePlayerName3.text() == '':
                return False

        return True

    def startGame(self):
        if not self.checkPlayerHaveNames():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Bitte geben sie die Namen für alle Spieler an!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return ''
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
        self.updateUI()

        self.ActivePlayer: monpoly.Player = game.getActivePlayer()
        self.gbPlayers[self.ActivePlayer.playerID].setStyleSheet('QGroupBox:title { background-color: #cacccc; }')

    def buildUI(self):
        self.setGeometry(100, 100, 1280, 720)
        self.setWindowTitle('Monpoly')

        # layoutAction

        self.layoutAction = QGridLayout()

        self.btnRoll = QPushButton('Würfeln', self)
        self.btnRoll.setStyleSheet('QPushButton { background-color: black; color: white; }')
        self.btnBuy = QPushButton('Kaufen', self)
        self.btnBuy.setStyleSheet('QPushButton { background-color: green; color: white; }')
        self.btnSell = QPushButton('Verkaufen', self)
        self.btnSell.setStyleSheet('QPushButton { background-color: red; color: white; }')
        self.btnBuild = QPushButton('Baumenu', self)
        self.btnTrade = QPushButton('Handen', self)
        self.btnTrade.setStyleSheet('QPushButton { background-color: orange; }')
        self.btnEnd = QPushButton('Zug beenden', self)
        self.btnEnd.setStyleSheet('QPushButton { background-color: darkred; color: white; }')
        self.teLogger = QTextEdit(self)
        self.teLogger.setReadOnly(True)
        self.teLogger.setStyleSheet('QTextEdit { max-width: 300px; max-height: 400px }')

        self.layoutAction.addWidget(self.btnRoll, 0, 0)
        self.layoutAction.addWidget(self.btnBuy, 1, 0)
        self.layoutAction.addWidget(self.btnSell, 2, 0)
        self.layoutAction.addWidget(self.btnBuild, 3, 0)
        self.layoutAction.addWidget(self.btnTrade, 4, 0)
        self.layoutAction.addWidget(self.btnEnd, 5, 0)
        self.layoutAction.addWidget(self.teLogger, 6, 0)

        # layout

        self.layout = QGridLayout()

        self.layout.addLayout(self.layoutAction, 0, 0, 2, 1)

        self.gbPlayers = []

        x = 0
        y = 1
        z = 0
        for player in game.players:
            if x > 1:
                x = 0
                y += 1
            self.gbPlayers.append(uiLib.QPlayerGroupBox(game.players[z].name))
            self.layout.addWidget(self.gbPlayers[z], x, y)
            z += 1
            x += 1

        self.setLayout(self.layout)

    def initUI(self):
        self.btnRoll.clicked.connect(self.actionRoll)
        self.btnBuy.clicked.connect(self.actionBuy)
        self.btnEnd.clicked.connect(self.actionEnd)


    def updateUI(self):
        for player in game.players:
            gbPlayerActive = self.gbPlayers[player.playerID]
            gbPlayerActive.lblNameV.setText(player.name)
            gbPlayerActive.lblPositionV.setText(player.getPOSITION())
            gbPlayerActive.lblAssetV.setText(str(player.asset))
            propertyStr = ''
            for property in player.property:
                propertyStr += property.name + ', '
            gbPlayerActive.lblPropertyV.setText(propertyStr)
        # self.gbPlayers[0].lblNameV.setText(str(type(game.map[0])))


    def actionRoll(self):
        if not self.ActivePlayer.rolled:
            cube1, cube2 = self.ActivePlayer.move()
            # if not cube1 == cube2: # TODO: Pasch programieren
            self.ActivePlayer.rolled = True
            if game.map[self.ActivePlayer.position].function == 'AbleToBuyField':
                if game.map[self.ActivePlayer.position].isBought:
                    game.map[self.ActivePlayer.position].payRent(self.ActivePlayer)
                    self.teLogger.setText(self.teLogger.toPlainText() + "\n'{}' zahlt an '{}' ${} Miete".format(self.ActivePlayer.name, game.map[self.ActivePlayer.position].owner.name, str(game.map[self.ActivePlayer.position].currentRent)))
        self.updateUI()

    def actionBuy(self):
        if self.ActivePlayer.rolled:
            if game.map[self.ActivePlayer.position].function == 'AbleToBuyField':
                if not game.map[self.ActivePlayer.position].isBought:
                    self.ActivePlayer.buyStreet(game.map[self.ActivePlayer.position])
                    self.teLogger.setText(self.teLogger.toPlainText() + "\n'{}' kauft {} für ${}".format(self.ActivePlayer.name, game.map[self.ActivePlayer.position].name, game.map[self.ActivePlayer.position].costs))

        self.updateUI()

    def actionEnd(self):
        if self.ActivePlayer.rolled:
            self.ActivePlayer.rolled = False
            game.changeActivePlayer()
            self.ActivePlayer = game.getActivePlayer()
            for gb in self.gbPlayers:
                gb.setStyleSheet('QGroupBox:tile { background-color: transparent; }')

        self.gbPlayers[self.ActivePlayer.playerID].setStyleSheet('QGroupBox:title { background-color: #cacccc; }')

        self.updateUI()
