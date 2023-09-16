# -*- coding: utf-8 -*-
"""
Generator of mdp (Molecular dynamics parameters) file for Gromacs.

Author: Rogério Ribeiro Macêdo
Date: September/2023
"""
# pylint: disable=invalid-name
# pylint: disable=import-error
import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class MainWindow(QtWidgets.QMainWindow):
    """Class main window."""

    fileName = ""

    def __init__(self,  *args, **kwargs):
        """
        Initialize function of class.

        Returns
        -------
        None.

        """
        # super(MainWindow, self).__init__(parent)
        super().__init__(*args, **kwargs)

        # Windows properties
        self.setWindowTitle("GenMDP")
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        # Setting Menu Bar
        self.mainMenuBar()

        # Adding a toolbar
        self.mainToolBar()

    def mainToolBar(self):
        """
        Toolbar.

        Returns
        -------
        None.
        """
        # Button open on toolbar
        openAction = QtWidgets.QAction(QtGui.QIcon('images/open.png'), 'Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open')
        openAction.triggered.connect(self.openFileMdp)

        # Button save on toolbar
        saveAction = QtWidgets.QAction(QtGui.QIcon('images/save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save')
        saveAction.triggered.connect(self.saveFileMdp)

        # Button exit on toolbar
        exitAction = QtWidgets.QAction(QtGui.QIcon('images/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+E')
        exitAction.setStatusTip('Exit')
        exitAction.triggered.connect(QtWidgets.qApp.quit)

        toolbar = QtWidgets.QToolBar('Main toolbar')
        self.addToolBar(toolbar)

        # Adding buttons in toolbar
        toolbar.addAction(openAction)
        toolbar.addAction(saveAction)
        toolbar.addSeparator()
        toolbar.addAction(exitAction)

    def mainMenuBar(self):
        """
        Build the main menu.

        Returns
        -------
        None.

        """
        # Menu Bar
        mainMenuBar = self.menuBar()

        # File menu
        fileMenu = mainMenuBar.addMenu('&File')

        # Open option (File -> Open)
        openAction = QtWidgets.QAction(QtGui.QIcon('images/open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open file.')
        openAction.triggered.connect(self.openFileMdp)
        fileMenu.addAction(openAction)

        # Save option (File -> Save)
        saveAction = QtWidgets.QAction(QtGui.QIcon('images/save.png'), '&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save file.')
        saveAction.triggered.connect(self.saveFileMdp)
        fileMenu.addAction(saveAction)

        # Separator
        fileMenu.addSeparator()

        # Exit option (File -> Exit)
        self.fileName = ""
        exitAction = QtWidgets.QAction(QtGui.QIcon('images/exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+E')
        exitAction.setStatusTip('Exit')
        exitAction.triggered.connect(QtWidgets.qApp.quit)
        fileMenu.addAction(exitAction)

        # About menu
        menuAbout = mainMenuBar.addMenu('&About')

        # Info option (About -> Info)
        infoAction = QtWidgets.QAction(QtGui.QIcon('images/info.png'), '&Info', self)
        infoAction.setShortcut('Ctrl+I')
        infoAction.setStatusTip('Info about the application')
        infoAction.triggered.connect(self.aboutWindow)
        menuAbout.addAction(infoAction)

    def saveFileMdp(self):
        """
        Save file.

        Returns
        -------
        None.

        """

    def openFileMdp(self):
        """
        Open file mdp.

        Returns
        -------
        None.

        """
        dialogOpen = QtWidgets.QFileDialog(self)
        dialogOpen.setDirectory(os.getcwd())
        dialogOpen.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        dialogOpen.setNameFilter("MDP (*.mdp)")
        dialogOpen.setViewMode(QtWidgets.QFileDialog.ViewMode.List)
        if dialogOpen.exec():
            self.fileName = dialogOpen.selectedFiles()

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


if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication(sys.argv)

    # Create and show the principal window
    window = MainWindow()
    window.showMaximized()
    window.show()

    # Run the main Qt Loop
    sys.exit(app.exec())
