import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QFileDialog
from PyQt5.QtGui import QIcon





class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.data = None

    def initUI(self):

        openAct = QAction(QIcon('open.png'), '&Open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open file dialog')
        openAct.triggered.connect(self.openFile)

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)


        self.statusBar()


        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAct)
        fileMenu.addSeparator()

        fileMenu.addAction(exitAct)
        fileMenu.addSeparator()


        fileMenu = menubar.addMenu('&Edit')


        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Data View')
        self.show()


    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "All Files (*);;Excel Files (*xlsx);;" 
                                                  "CSV Files (*csv);; Text Files(*txt)", options=options)

        if fileName:
            fichier = open(fileName, 'r')
            self.data = [i.split(";") for i in fichier.read().split("\n")]
            print(self.data)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
