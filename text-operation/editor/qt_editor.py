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

from PyQt5.QtGui import QFont, QFontMetricsF
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QFontDialog,
                             QMainWindow, QMenu, qApp, QPlainTextEdit)


class Editor(QMainWindow):

    def __init__(self):
        super().__init__()
        self.currentpath = ''
        self.font = QFont("Monaco", 14)
        self.font.setFixedPitch(True)
        self.title = 'simple text editor'
        self.textEditor = QPlainTextEdit()
        self.textEditor.setFont(self.font)
        # set tab length 4 spaces
        self.textEditor.setTabStopDistance(
            QFontMetricsF(self.textEditor.font()).width(' ') * 4)
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
        exitAct = QAction('Exit', self)
        saveAct = QAction('Save', self)
        exitAct.triggered.connect(qApp.quit)

        newAct.setShortcut('Ctrl+N')
        openAct.setShortcut('Ctrl+O')
        exitAct.setShortcut('Ctrl+Q')
        saveAct.setShortcut('Ctrl+S')

        # action detail
        openAct.triggered.connect(self.openFile)
        newAct.triggered.connect(self.newFile)
        saveAct.triggered.connect(self.saveFile)

        # autoSave set default False
        autoSave.setChecked(False)

        # add action on fileMenu
        fileMenu.addAction(newAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(autoSave)
        fileMenu.addAction(exitAct)

    def newFile(self):
        fname = QFileDialog.getSaveFileName(self, 'Save file')
        context = self.textEditor.toPlainText()
        if fname[0]:
            with open(fname[0], 'w') as f:
                f.write(context)
            self.currentpath = fname[0]

    def saveFile(self):
        path = self.currentpath
        context = self.textEditor.toPlainText()
        if path:
            with open(path, 'w') as f:
                f.write(context)

    def setSettingMenu(self):
        # settingMenu setting
        settingMenu = self.menubar.addMenu('Setting')
        settingMenu.setFont(self.font)

        # action
        fontAct = QAction('Font', self)

        # action detail
        settingMenu.addAction(fontAct)

        # add action on settingMenu
        fontAct.triggered.connect(self.selectFont)

    def selectFont(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEditor.setFont(font)

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

    def openFile(self):
        # get current use main home full path as string
        main_home = Path.home().absolute().as_posix()
        fname = QFileDialog.getOpenFileName(self, 'Open File', main_home)
        if fname[0]:
            with open(fname[0], 'r') as f:
                content = f.read()
                self.textEditor.setPlainText(content)
                self.currentpath = fname[0]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = Editor()
    sys.exit(app.exec_())
