import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class Editor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        newAct = QAction('New', self)
        settingAct = QAction('Setting', self)
        exitAct = QAction('Exit', self)
        fileMenu.addAction(newAct)
        fileMenu.addAction(settingAct)
        fileMenu.addAction(exitAct)
        self.setGeometry(500, 300, 800, 600)
        self.setWindowTitle('文本编辑器0.0.1')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = Editor()
    sys.exit(app.exec_())
