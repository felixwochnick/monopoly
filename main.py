#!/usr/bin/env python3


"""
    Mainfile 'MONOPOLY.GAME'
"""

import sys
import game as gameLib

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

uiStart: gameLib.UIstart
uiMain: gameLib.UImain
game: gameLib.Game


app = QApplication(sys.argv)
app.setAttribute(Qt.AA_UseHighDpiPixmaps)

uiStart = gameLib.UIstart()

sys.exit(app.exec_())
