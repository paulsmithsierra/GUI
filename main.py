import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QFileDialog, QHBoxLayout, QPushButton, \
    QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QIcon





class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.data = None

    def initUI(self):


        #Widgets
        widgetTable = QTableWidget()


            # Row count
        widgetTable.setRowCount(4)

            # Column count
        widgetTable.setColumnCount(7)

            # Table will fit the screen horizontally
        widgetTable.horizontalHeader().setStretchLastSection(True)
        widgetTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)


        widgetStats = QWidget()
        widgetDetails = QWidget()
        widgetStats.setStyleSheet('background-color: red;')
        widgetDetails.setStyleSheet('background-color: green;')

        #Layouts
        layoutHorizontal = QHBoxLayout()
        layoutVertical = QVBoxLayout()

        layoutVertical.addWidget(widgetStats, 1)
        layoutVertical.addWidget(widgetDetails, 1)

        layoutHorizontal.addWidget(widgetTable, 3)
        layoutHorizontal.addLayout(layoutVertical, 1)


        widget = QWidget()
        widget.setLayout(layoutHorizontal)
        self.setCentralWidget(widget)


        #Actions
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
