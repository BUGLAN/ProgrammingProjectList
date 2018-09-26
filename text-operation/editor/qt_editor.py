#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    editor.qt_editor
    ----------------

    text editor
    hope it do more
    :copyright: (c) 2018-09-26 by buglan
"""

import sys
from pathlib import Path

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QFontDialog,
                             QMainWindow, QMenu, QTextEdit, qApp)


class Editor(QMainWindow):

    def __init__(self):
        super().__init__()
        self.font = QFont("Monaco", 14)
        self.font.setFixedPitch(True)
        self.title = 'simple text editor'
        self.textEditor = QTextEdit()
        self.textEditor.setFont(self.font)
        self.menubar = self.menuBar()
        self.menubar.setFont(self.font)
        self.init_ui()

    def setFileMenu(self):
        # fileMenu setting
        fileMenu = self.menubar.addMenu('File')
        fileMenu.setFont(self.font)

        # action
        newAct = QAction('New', self)
        openAct = QAction('Open', self)
        autoSave = QAction('AutoSavle', self, checkable=True)
        settingAct = QAction('Setting', self)
        exitAct = QAction('Exit', self)

        # action detail
        openAct.triggered.connect(self.showFileDialog)

        # autoSave set default False
        autoSave.setChecked(False)

        # add action on fileMenu
        fileMenu.addAction(newAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(autoSave)
        fileMenu.addAction(settingAct)
        fileMenu.addAction(exitAct)

    def setSettingMenu(self):
        # settingMenu setting
        settingMenu = self.menubar.addMenu('Setting')
        settingMenu.setFont(self.font)

        # action
        fontAct = QAction('Font', self)

        # action detail
        settingMenu.addAction(fontAct)

        # add action on settingMenu
        fontAct.triggered.connect(self.showFontDialog)

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            #  QApplication.setFont(font)
            print(self.textEditor.font)
            self.font = font
            print("Display Fonts: ", font)

    def init_ui(self):
        self.setFileMenu()
        self.setSettingMenu()
        self.setCentralWidget(self.textEditor)

        # setting window
        self.setGeometry(500, 300, 800, 600)
        self.setWindowTitle(self.title)
        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == newAct:
            pass

        if action == quitAct:
            qApp.quit()

        if action == openAct:
            pass

    def showFileDialog(self):
        # get current use main home full path as string
        main_home = Path.home().absolute().as_posix()
        fname = QFileDialog.getOpenFileName(self, 'Open File', main_home)
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                content = f.read()
                self.textEditor.setText(content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = Editor()
    sys.exit(app.exec_())
