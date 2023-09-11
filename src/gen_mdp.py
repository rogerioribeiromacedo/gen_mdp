# -*- coding: utf-8 -*-
"""
Generator of mdp (Molecular dynamics parameters) file for Gromacs.

Author: Rogério Ribeiro Macêdo
Date: September/2023
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QStatusBar
from PyQt5.QtGui import QIcon


class graphMainWindow(QMainWindow):
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
        self.mainMenuBar()

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.statusBar().showMessage('Are you ready?!')

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
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+E')
        exitAction.setStatusTip('Exit')
        exitAction.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAction)

        # About menu
        menuAbout = mainMenuBar.addMenu('&About')

        # Info option (About -> Info)
        infoAction = QAction('&Info', self)
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
        infoMessage = QMessageBox()
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
    application = QApplication(sys.argv)
    mainWindow = graphMainWindow()
    mainWindow.showMaximized()

    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
