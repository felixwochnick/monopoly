import sys
import monopoly
import uiLib
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QGridLayout, QLineEdit, QMessageBox, QTextEdit, QListWidget
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt



class DisplayPlayer(monopoly.Player):
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
        self.ActivePlayer: monopoly.Player

        while len(self.players) < numberOFplayers:
            self.players.append(DisplayPlayer(nameOFplayers[len(self.players)], len(self.players)))

        self.ActivePlayer = self.players[0]

        gruppeBraun = monopoly.FieldGroup('#65250d', 2)
        gruppeGrau = monopoly.FieldGroup('#728bbb')
        gruppePink = monopoly.FieldGroup('#ea00fb')
        gruppeOrange = monopoly.FieldGroup('#f37c05')
        gruppeRot = monopoly.FieldGroup('#ea0d0d')
        gruppeGelb = monopoly.FieldGroup('#d9dc0b')
        gruppeGrün = monopoly.FieldGroup('#0bc508')
        gruppeBlau = monopoly.FieldGroup('#0878e8', 2)

        gruppeWerk = monopoly.FieldGroup('#6b6b6b', 2)
        gruppeBahnhof = monopoly.FieldGroup('#bfbebe', 4)

        self.map = [
            monopoly.Field('Los'),                                                                               # Los Feld

            monopoly.Street('Badstrasse', gruppeBraun, 0, 60, 2, 10, 30, 90, 160, 250, 50, 30),                  # Badstrasse
            monopoly.Field('Gemeinschaftsfeld'),                                                                 # Gemeinschaftsfeld
            monopoly.Street('Turmstrasse', gruppeBraun, 1, 60, 4, 20, 60, 180, 320, 450, 50, 30),                # Turmstrasse
            # monopoly.Street('Stadionstrasse', gruppeBraun, 2, 80, 5, 30, 80, 240, 360, 500, 50, 40),             # Stadionstrasse
            monopoly.MonneyActionField('Einkommenssteuer Feld', 0, 200),                                         # Einkommenssteuer Feld

            monopoly.TrainStation('Südbahnhof', gruppeBahnhof, 0),                                               # Südbahnhof

            monopoly.Street('Chausseestrasse', gruppeGrau, 0, 100, 6, 30, 90, 270, 400, 550, 50, 50),            # Chausseestrasse
            monopoly.Field('Ereignisfeld'),                                                                      # Ereignisfeld
            monopoly.Street('Elisenstrasse', gruppeGrau, 1, 100, 6, 30, 90, 270, 400, 550, 50, 50),              # Elisenstrasse
            # monopoly.Factory('Gaswerk', gruppeWerk, 0),                                                          # Gaswerk
            monopoly.Street('Poststrasse', gruppeGrau, 2, 100, 6, 30, 90, 270, 400, 550, 50, 50),                # Poststrasse
            # monopoly.Street('Tiergartenstrasse', gruppeGrau, 3, 120, 8, 40, 100, 300, 450, 600, 50, 60),         # Tiergartenstrasse

            monopoly.Field('Nur zu Besuch'),                                                                     # Nur zu Besuch

            # monopoly.Field('Auktion'),                                                                           # Aktion
            monopoly.Street('Seestrasse', gruppePink, 0, 140, 10, 50, 150, 450, 625, 750, 100, 70),              # Seestrasse
            monopoly.Factory('Elektrizitätswerk', gruppeWerk, 0),                                                # Elektrizitätswerk
            monopoly.Street('Hafenstrasse', gruppePink, 1, 140, 10, 50, 150, 450, 625, 750, 100, 70),            # Hafenstrasse
            monopoly.Street('Neue Strasse', gruppePink, 2, 140, 10, 50, 150, 450, 625, 750, 100, 70),            # Neue Strasse
            # monopoly.Street('Marktplatz', gruppePink, 3, 160, 12, 60, 180, 500, 700, 900, 100, 80),              # Marktplatz

            monopoly.TrainStation('Westbahnhof', gruppeBahnhof, 1),                                              # Westbahnhof

            monopoly.Street('Münchner Strasse', gruppeOrange, 0, 180, 14, 70, 200, 550, 750, 950, 100, 90),      # Münchner Strasse
            monopoly.Field('Gemeinschaftsfeld'),                                                                 # Gemeinschaftsfeld
            monopoly.Street('Wiener Strasse', gruppeOrange, 1, 180, 14, 70, 200, 550, 750, 950, 100, 90),        # Wiener Strasse
            monopoly.Street('Berliner Strasse', gruppeOrange, 2, 200, 16, 80, 220, 600, 800, 1000, 100, 100),    # Berliner Strasse
            # monopoly.Street('Hamburger Strasse', gruppeOrange, 3, 200, 16, 80, 220, 600, 800, 1000, 100, 100),   # Hamburger Strasse

            monopoly.Field('Frei Parken'),                                                                       # Frei Parken

            monopoly.Street('Theaterstrasse', gruppeRot, 0, 220, 18, 90, 250, 700, 875, 1050, 150, 100),         # Theaterstrasse
            monopoly.Field('Ereignisfeld'),                                                                      # Ereignisfeld
            monopoly.Street('Museumstrasse', gruppeRot, 1, 220, 18, 90, 250, 700, 875, 1050, 150, 100),          # Museumstrasse
            monopoly.Street('Opernplatz', gruppeRot, 2, 240, 20, 100, 300, 750, 925, 1100, 150, 120),            # Opernplatz
            # monopoly.Street('Konzerthausstrasse', gruppeRot, 3, 240, 20, 100, 300, 750, 925, 1100, 150, 120),    # Konzerthausstrasse

            # monopoly.Field('Bus'),                                                                               # Bus
            monopoly.TrainStation('Nordbahnhof', gruppeBahnhof, 2),                                              # Nordbahnhof

            monopoly.Street('Lessingstrasse', gruppeGelb, 0, 260, 22, 110, 330, 800, 975, 1150, 150, 130),       # Lessingstrasse
            monopoly.Street('Schillerstrasse', gruppeGelb, 1, 260, 22, 110, 330, 800, 975, 1150, 150, 130),      # Schillerstrasse
            monopoly.Factory('Wasserwerk', gruppeWerk, 1),                                                       # Wasserwerk
            monopoly.Street('Goethestrasse', gruppeGelb, 2, 280, 24, 120, 360, 850, 1025, 1200, 150, 140),       # Goethestrasse
            # monopoly.Street('Rilkestrasse', gruppeGelb, 3, 280, 24, 120, 360, 850, 1025, 1200, 150, 140),        # Rilkestrasse

            monopoly.Field('Gefängnis'),                                                                         # Gefängnis

            monopoly.Street('Rathausplatz', gruppeGrün, 0, 300, 26, 130, 390, 900, 1100, 1275, 200, 150),        # Rathausplatz
            monopoly.Street('Hauptstrasse', gruppeGrün, 1, 300, 26, 130, 390, 900, 1100, 1275, 200, 150),        # Hauptstrasse
            # monopoly.Street('Börsenplatz', gruppeGrün, 2, 300, 26, 130, 390, 900, 1100, 1275, 200, 150),         # Börsenplatz
            monopoly.Field('Gemeinschaftsfeld'),                                                                 # Gemeinschaftsfeld
            monopoly.Street('Bahnhofstraße', gruppeGrün, 2, 320, 28, 150, 450, 1000, 1200, 1400, 200, 160),      # Bahnhofstraße

            monopoly.TrainStation('Hauptbahnhof', gruppeBahnhof, 3),                                             # Hauptbahnhof
            monopoly.Field('Ereignisfeld'),                                                                      # Ereignisfeld

            # monopoly.MonneyActionField('Geburtstaggeschenk', 100, 0),                                            # Geburtstaggeschenk
            # monopoly.Street('Domplatz', gruppeBlau, 0, 350, 35, 175, 500, 1100, 1300, 1500, 200, 175),           # Domplatz
            monopoly.Street('Parkstrasse', gruppeBlau, 0, 350, 35, 175, 500, 1100, 1300, 1500, 200, 175),        # Parkstrasse
            monopoly.MonneyActionField('Zusatzsteuer', 0, 75),                                                   # Zusatzsteuer
            monopoly.Street('Schlossallee', gruppeBlau, 1, 400, 50, 200, 600, 1400, 1700, 2000, 200, 200),       # Schlossallee
        ]

    def mainLoop(self):
        for player in self.players:
            player.move()
            if type(self.map[player.position]) == monopoly.Street or type(self.map[player.position]) == monopoly.TrainStation:
                if self.map[player.position].isBought is False:
                    if input(self.map[player.position].name + ' kaufen? ') == 'Y':
                        player.buyStreet(self.map[player.position])

                elif self.map[player.position].isBought is True:
                    self.map[player.position].payRent(player)

            elif type(self.map[player.position]) == monopoly.MonneyActionField:
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

    def __init__(self, styleText: str):
        super().__init__()

        self.buildUI()
        self.initUI()
        self.changePlayerNumber()

        self.setStyleSheet(styleText)
        self.show()

    def buildUI(self):
        self.setGeometry(100, 100, 400, 600)
        self.setWindowTitle('Monopoly starten')

        self.lblHeader = QLabel('Monopoly (Alpha)', self)
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

        self.ActivePlayer: monopoly.Player = game.getActivePlayer()
        self.gbPlayers[self.ActivePlayer.playerID].setStyleSheet('QGroupBox:title { background-color: #cacccc; }')

    def buildUI(self):
        self.setGeometry(100, 100, 1280, 720)
        self.setWindowTitle('Monopoly')

        # layoutAction

        self.layoutAction = QGridLayout()

        self.btnRoll = QPushButton('Würfeln', self)
        self.btnRoll.setStyleSheet('QPushButton { background-color: black; color: white; }')
        self.btnBuy = QPushButton('Kaufen', self)
        self.btnBuy.setStyleSheet('QPushButton { background-color: green; color: white; }')
        self.btnBecomeFree = QPushButton('Freikaufen', self)
        self.btnBecomeFree.setStyleSheet('QPushButton { background-color: grey; color: white; }')
        self.btnBuild = QPushButton('Baumenu', self)
        self.btnTrade = QPushButton('Handeln', self)
        self.btnTrade.setStyleSheet('QPushButton { background-color: orange; }')
        self.btnEnd = QPushButton('Zug beenden', self)
        self.btnEnd.setStyleSheet('QPushButton { background-color: darkred; color: white; }')
        self.teLogger = QTextEdit(self)
        self.teLogger.setReadOnly(True)
        self.teLogger.setStyleSheet('QTextEdit { max-width: 300px; max-height: 400px }')
        # self.teLogger.setText(str(len(game.map)))

        self.layoutAction.addWidget(self.btnRoll, 0, 0)
        self.layoutAction.addWidget(self.btnBuy, 1, 0)
        self.layoutAction.addWidget(self.btnBecomeFree, 2, 0)
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

        y += 1

        self.matchfield = uiLib.Matchfield(game)

        self.layout.addWidget(self.matchfield, 0, y, 2, 1)

        self.setLayout(self.layout)

    def initUI(self):
        self.btnRoll.clicked.connect(self.actionRoll)
        self.btnBuy.clicked.connect(self.actionBuy)
        self.btnBecomeFree.clicked.connect(self.actionBecomeFree)
        self.btnTrade.clicked.connect(self.actionTrade)
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
        """Player rolls and goes to the rolled Field"""
        if not self.ActivePlayer.intoPrison:
            if not self.ActivePlayer.rolled:
                cube1, cube2, event = self.ActivePlayer.move()
                if event == 'goONstart':
                    self.teLogger.setText("'{}' würfelt {} und bekommt $400, weil er auf Los gekommen ist\n{}".format(self.ActivePlayer.name, str(cube1 + cube2), self.teLogger.toPlainText()))
                elif event == 'goOVERstart':
                    self.teLogger.setText("'{}' würfelt {} und bekommt $200, weil er über Los gekommen ist\n{}".format(self.ActivePlayer.name, str(cube1 + cube2), self.teLogger.toPlainText()))
                else:
                    self.teLogger.setText("'{}' würfelt {} \n{}".format(self.ActivePlayer.name, str(cube1 + cube2), self.teLogger.toPlainText()))
                # if not cube1 == cube2: # TODO: Pasch programieren
                self.ActivePlayer.rolled = True

                # pay rent
                if game.map[self.ActivePlayer.position].function == 'AbleToBuyField':
                    if game.map[self.ActivePlayer.position].isBought:
                        if game.map[self.ActivePlayer.position].owner != self.ActivePlayer:
                            game.map[self.ActivePlayer.position].payRent(self.ActivePlayer)
                            self.teLogger.setText("'{}' zahlt an '{}' ${} Miete\n{}".format(self.ActivePlayer.name, game.map[self.ActivePlayer.position].owner.name, str(game.map[self.ActivePlayer.position].currentRent), self.teLogger.toPlainText()))

                # get/lose monney
                elif game.map[self.ActivePlayer.position].function == 'ActionField':
                    game.map[self.ActivePlayer.position].action(self.ActivePlayer)
                    if game.map[self.ActivePlayer.position].getMonney > 0:
                        self.teLogger.setText("'{}' bekommt von der Bank ${} ({})\n{}".format(self.ActivePlayer.name, game.map[self.ActivePlayer.position].getMonney, game.map[self.ActivePlayer.position].name, self.teLogger.toPlainText()))
                    else:
                        self.teLogger.setText("'{}' zahlt an die Bank ${} ({})\n{}".format(self.ActivePlayer.name, game.map[self.ActivePlayer.position].loseMonney, game.map[self.ActivePlayer.position].name, self.teLogger.toPlainText()))

                # go into prison
                elif self.ActivePlayer.position == 30:
                    self.ActivePlayer.goINTOprison()
                    self.gbPlayers[self.ActivePlayer.playerID].lblPrisonV.setText('Ja')
                    self.teLogger.setText("'{}' geht in das Gefängnis \n{}".format(self.ActivePlayer.name, self.teLogger.toPlainText()))

        self.updateUI()

    def actionBuy(self):
        """Player buys a new Field"""
        if self.ActivePlayer.rolled:
            if game.map[self.ActivePlayer.position].function == 'AbleToBuyField':
                if not game.map[self.ActivePlayer.position].isBought:
                    self.ActivePlayer.buyStreet(game.map[self.ActivePlayer.position])
                    self.teLogger.setText("'{}' kauft {} für ${} \n{}".format(self.ActivePlayer.name, game.map[self.ActivePlayer.position].name, game.map[self.ActivePlayer.position].costs, self.teLogger.toPlainText()))

        self.updateUI()

    def actionBecomeFree(self):
        if self.ActivePlayer.intoPrison:
            self.ActivePlayer.becomeFree()
            self.gbPlayers[self.ActivePlayer.playerID].lblPrisonV.setText('Nein')
            self.teLogger.setText("'{}' ist wieder frei \n{}".format(self.ActivePlayer.name, self.teLogger.toPlainText()))

        self.updateUI()

    def actionTrade(self):
        self.uitrade = UItrade(self.ActivePlayer)

    def actionEnd(self):
        """Player's move ends"""
        if self.ActivePlayer.rolled or self.ActivePlayer.intoPrison:
            self.ActivePlayer.rolled = False
            self.teLogger.setText("'{}' beendet den Zug\n{}".format(self.ActivePlayer.name, self.teLogger.toPlainText()))
            game.changeActivePlayer()
            self.ActivePlayer = game.getActivePlayer()
            for gb in self.gbPlayers:
                gb.setStyleSheet('QGroupBox:tile { background-color: transparent; }')

        self.gbPlayers[self.ActivePlayer.playerID].setStyleSheet('QGroupBox:title { background-color: #cacccc; }')

        self.updateUI()


class UItrade(QWidget):
    def __init__(self, ActivePlayer):
        super().__init__()
        self.ActivePlayer: monopoly.Player = ActivePlayer

        self.playerList: list = []
        for player in game.players:
            self.playerList.append(player)
        self.playerList.pop(self.ActivePlayer.playerID)

        self.listPlayerLeft = [game.map[5], Monney(400)]
        self.listPlayerRight = [game.map[11]]

        self.buildUI()
        self.initUI()
        self.show()

    def buildUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Handelsmenü')

        # layout

        self.lblActivePlayer = QLabel(self.ActivePlayer.name)

        self.icoTrade = QLabel()
        self.srcIconTrade = QPixmap("resources/icons/arrow.svg")
        self.srcIconTrade = self.srcIconTrade.scaledToWidth(20)
        self.srcIconTrade = self.srcIconTrade.scaledToHeight(20)
        self.icoTrade.setPixmap(self.srcIconTrade)  # Icon made by Pixel perfect from www.flaticon.com


        self.cboxSelectPlayer = QComboBox(self)
        for player in self.playerList:
            self.cboxSelectPlayer.addItem(player.name)

        self.btnPlayerLeftAdd = QPushButton('+', self)
        self.btnPlayerLeftRemove = QPushButton('-', self)

        self.btnPlayerRightAdd = QPushButton('+', self)
        self.btnPlayerRightRemove = QPushButton('-', self)

        self.lwPlayerLeft = QListWidget()
        self.lwPlayerRight = QListWidget()

        self.btnTrade = QPushButton('Handeln', self)
        self.btnCancel = QPushButton('Abbrechen', self)

        self.layout = QGridLayout()
        self.layout.addWidget(self.lblActivePlayer, 0, 0, 1, 2)

        self.layout.addWidget(self.icoTrade, 0, 2, 1, 1,)

        self.layout.addWidget(self.cboxSelectPlayer, 0, 3, 1, 2)

        self.layout.addWidget(self.btnPlayerLeftAdd, 1, 0, 1, 1)
        self.layout.addWidget(self.btnPlayerLeftRemove, 1, 1, 1, 1)

        self.layout.addWidget(self.btnPlayerRightAdd, 1, 3, 1, 1)
        self.layout.addWidget(self.btnPlayerRightRemove, 1, 4, 1, 1)

        self.layout.addWidget(self.lwPlayerLeft, 2, 0, 1, 2)
        self.layout.addWidget(self.lwPlayerRight, 2, 3, 1, 2)

        self.layout.addWidget(self.btnTrade, 3, 0, 1, 2)
        self.layout.addWidget(self.btnCancel, 3, 3, 1, 2)

        self.setLayout(self.layout)

    def initUI(self):
        self.btnPlayerLeftAdd.clicked.connect(self.actionPlayerLeftAdd)
        self.btnPlayerRightAdd.clicked.connect(self.actionPlayerRightAdd)
        self.btnPlayerLeftRemove.clicked.connect(self.actionPlayerLeftRemove)
        self.btnPlayerRightRemove.clicked.connect(self.actionPlayerRightRemove)

        self.btnTrade.clicked.connect(self.actionTrade)
        self.btnCancel.clicked.connect(self.actionCancel)


        self.lwPlayerLeft.addItems(self.getNames(self.listPlayerLeft))
        self.lwPlayerRight.addItems(self.getNames(self.listPlayerRight))

    def actionPlayerLeftAdd(self):
        pass

    def actionPlayerLeftRemove(self):
        self.listPlayerLeft = self.removeFromList(self.listPlayerLeft, self.lwPlayerLeft.currentItem().text())
        self.lwPlayerLeft.clear()
        self.lwPlayerLeft.addItems(self.getNames(self.listPlayerLeft))

    def actionPlayerRightAdd(self):
        pass

    def actionPlayerRightRemove(self):
        self.listPlayerRight = self.removeFromList(self.listPlayerRight, self.lwPlayerRight.currentItem().text())
        self.lwPlayerRight.clear()
        self.lwPlayerRight.addItems(self.getNames(self.listPlayerRight))

    def actionTrade(self):
        self.hide()

    def actionCancel(self):
        self.hide()

    def getNames(self, list: list):
        rList = []
        for item in list:
            rList.append(item.name)

        return rList

    def removeFromList(self, list: list, name: str):
        x = 0
        for item in list:
            if item.name == name:
                break
            x += 1
        list.pop(x)

        return list

class Monney():
    def __init__(self, value):
        self.name: str = '$ {}'.format(str(value))
        self.value: int = value
