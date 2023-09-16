# -*- coding: utf-8 -*-
r"""
Generator of mdp (Molecular dynamics parameters) file for Gromacs.

self.eijMenulLabel = QtWidgets.QLabel('Output list:')
self.eijMenulLabel.setStyleSheet("background-color: lightgreen")

layout.addWidget(QtWidgets.QLabel('Username:'), 0, 0, QtCore.Qt.AlignTop)
layout.addWidget(QtWidgets.QLineEdit(), 0, 1, QtCore.Qt.AlignTop)


# setting up background color and border
self.label_2 = QtWidgets.QLabel('Output list:')
self.label_2.setStyleSheet("background-color: yellow;\
                            border: 1px solid black;")

sex = QtWidgets.QHBoxLayout()
sex.addWidget(QtWidgets.QRadioButton("Male"))
sex.addWidget(QtWidgets.QRadioButton("Female"))
layout.addRow(QtWidgets.QLabel("Sex"),sex)
layout.addRow("Date of Birth",QtWidgets.QLineEdit())

layout = QtWidgets.QHBoxLayout()
layout.addWidget(QtWidgets.QLabel("subjects"))
layout.addWidget(QtWidgets.QCheckBox("Physics"))
layout.addWidget(QtWidgets.QCheckBox("Maths"))
tab_group.setTabText(2,"Education Details")
self.tab3.setLayout(layout)

Author: Rogério Ribeiro Macêdo
Date: September/2023
"""
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon


class graphMainWindow(QtWidgets.QMainWindow):
    """Class Window."""

    def __init__(self, parent=None):
        """
        Init function for the class that make a window.

        Parameters
        ----------
        parent : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        """
        super().__init__(parent)

        self.setWindowTitle("GenMDP")
        self.setWindowIcon(QIcon('icons/logo.png'))

        # Menu bar
        self.mainMenuBar()

        # Adding a toolbar
        self.mainToolBar()

        # Status bar
        self.status = QtWidgets.QStatusBar()
        self.setStatusBar(self.status)
        self.statusBar().showMessage('Are you ready?!')

        # Layout
        self.layoutWindow()

    def layoutWindow(self):
        """
        Define layout window.

        Returns
        -------
        None.

        """
        # Tabs
        tabGroups = QtWidgets.QTabWidget()

        self.tabPreprocessing = QtWidgets.QWidget()
        self.layoutPreprocessing(self.tabPreprocessing)

        self.tabRunControl = QtWidgets.QWidget()
        self.layoutRunControl(self.tabRunControl)

        tabGroups.addTab(self.tabPreprocessing, "Preprocessing")
        tabGroups.addTab(self.tabRunControl, "Run Control")

        # Layout window
        layout = QtWidgets.QGridLayout()
        layout.addWidget(tabGroups, 0, 0, 1, 1)

        # Main frame
        self.mainFrame = QtWidgets.QWidget()
        self.mainFrame.setLayout(layout)
        self.mainFrame.setSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                     QtWidgets.QSizePolicy.Minimum)

        # Adding main frame to CentralWidget
        self.setCentralWidget(self.mainFrame)
        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum,
                           QtWidgets.QSizePolicy.Minimum)

    def layoutPreprocessing(self, tab):
        """
        Widgets for Preprocessing.

        Returns
        -------
        None.

        """
        layout = QtWidgets.QGridLayout()
        tab.setLayout(layout)

    def layoutRunControl(self, tab):
        """
        Widgets for Run Control.

        Parameters
        ----------
        tab : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        listIntegrator = ["md", "md-vv", "md-vv-avek",
                          "sd", "bd", "steep", "cg",
                          "l-bfgs", "nm", "tpi", "tpic", "mimic"]
        layout = QtWidgets.QGridLayout()

        # Combobox with list on integrators
        layout.addWidget(QtWidgets.QLabel("Integrator"), 0, 0, 1, 1, QtCore.Qt.AlignTop)
        integrator = QtWidgets.QComboBox(self)
        integrator.activated[str].connect(self.onChanged)
        for i in listIntegrator:
            integrator.addItem(i)
        layout.addWidget(integrator, 0, 1, 1, 1, QtCore.Qt.AlignTop)
        layout.setColumnStretch(1, 1)

        tab.setLayout(layout)

    def onChanged(self, text):
        infoMessage = QtWidgets.QMessageBox()
        infoMessage.setWindowTitle("About")
        infoMessage.setText(text)
        infoMessage.setIcon(1)
        infoMessage.exec_()

    def mainToolBar(self):
        """
        Toolbar.

        Returns
        -------
        None.

        """
        exitAction = QtWidgets.QAction(QIcon('icons/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+E')
        exitAction.setStatusTip('Exit')
        exitAction.triggered.connect(QtWidgets.qApp.quit)
        toolbar = QtWidgets.QToolBar('Main toolbar')
        self.addToolBar(toolbar)
        toolbar.addAction(exitAction)

    def mainMenuBar(self):
        """
        Build the main menu.

        Returns
        -------
        None.

        """
        # Menu bar
        mainMenuBar = self.menuBar()

        # File menu
        fileMenu = mainMenuBar.addMenu('&File')

        # Exit option (File -> Exit)
        exitAction = QtWidgets.QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+E')
        exitAction.setStatusTip('Exit')
        exitAction.triggered.connect(QtWidgets.qApp.quit)
        fileMenu.addAction(exitAction)

        # About menu
        menuAbout = mainMenuBar.addMenu('&About')

        # Info option (About -> Info)
        infoAction = QtWidgets.QAction('&Info', self)
        infoAction.setShortcut('Ctrl+I')
        infoAction.setStatusTip('Info about the application')
        infoAction.triggered.connect(self.aboutWindow)
        menuAbout.addAction(infoAction)

    def aboutWindow(self):
        """
        Create a pop-up window with information about the interface.

        Returns
        -------
        None.

        """
        infoMessage = QtWidgets.QMessageBox()
        infoMessage.setWindowTitle("About")
        infoMessage.setText("Application written in Python<br/><br/>\
                      Author: Rogério Ribeiro Macêdo<br/>\
                      Institution: Chemistry and Physics Institute, University Federal of Itajubá<br/>\
                      Year: 2023 and 2024<br/> \
                      Last Modified data: September 11, 2023")
        infoMessage.setIcon(1)
        infoMessage.exec_()


def main():
    """
    Initialize and show the Window.

    Returns
    -------
    None.

    """
    application = QtWidgets.QApplication(sys.argv)
    mainWindow = graphMainWindow()
    mainWindow.showMaximized()

    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
