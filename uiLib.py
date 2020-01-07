from PyQt5.QtWidgets import QLabel, QGridLayout, QGroupBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


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

        self.layout.addWidget(self.lblName, 0, 0)
        self.layout.addWidget(self.lblNameV, 0, 1)
        self.layout.addWidget(self.lblPosition, 1, 0)
        self.layout.addWidget(self.lblPositionV, 1, 1)
        self.layout.addWidget(self.lblAsset, 2, 0)
        self.layout.addWidget(self.lblAssetV, 2, 1)
        self.layout.addWidget(self.lblProperty, 3, 0)
        self.layout.addWidget(self.lblPropertyV, 3, 1)

        self.setLayout(self.layout)
