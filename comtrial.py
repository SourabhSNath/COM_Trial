from PyQt6 import QtCore, QtWidgets
import csv
import os.path


class Ui_MainWindow(object):

    table_header = ("Port", "Baudrate", "Parity")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(self.table_header)

        # Expand the table to fill the full width of the window
        horizontal_header = self.tableWidget.horizontalHeader()
        horizontal_header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        horizontal_header.setSectionResizeMode(
            1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        horizontal_header.setSectionResizeMode(
            2, QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontal_input_container = QtWidgets.QHBoxLayout()
        self.horizontal_input_container.setObjectName(
            "horizontal_input_container")

        self.port_box = QtWidgets.QHBoxLayout()
        self.port_box.setObjectName("port_box")
        self.port_label = QtWidgets.QLabel(self.centralwidget)
        self.port_label.setObjectName("port_label")
        self.port_box.addWidget(self.port_label)
        self.port_input = QtWidgets.QLineEdit(self.centralwidget)
        self.port_input.setObjectName("port_input")
        self.port_box.addWidget(self.port_input)
        self.horizontal_input_container.addLayout(self.port_box)

        self.baudrate_box = QtWidgets.QHBoxLayout()
        self.baudrate_box.setObjectName("baudrate_box")
        self.baudrate_label = QtWidgets.QLabel(self.centralwidget)
        self.baudrate_label.setObjectName("baudrate_label")
        self.baudrate_box.addWidget(self.baudrate_label)
        self.baudrate_input = QtWidgets.QLineEdit(self.centralwidget)
        self.baudrate_input.setObjectName("baudrate_input")
        self.baudrate_box.addWidget(self.baudrate_input)
        self.horizontal_input_container.addLayout(self.baudrate_box)

        self.parity_box = QtWidgets.QHBoxLayout()
        self.parity_box.setObjectName("parity_box")
        self.parity_label = QtWidgets.QLabel(self.centralwidget)
        self.parity_label.setObjectName("parity_label")
        self.parity_box.addWidget(self.parity_label)
        self.parity_input = QtWidgets.QLineEdit(self.centralwidget)
        self.parity_input.setObjectName("parity_input")
        self.parity_box.addWidget(self.parity_input)
        self.horizontal_input_container.addLayout(self.parity_box)

        self.verticalLayout.addLayout(self.horizontal_input_container)

        self.enter_button = QtWidgets.QPushButton(self.centralwidget)
        self.enter_button.setObjectName("enter_button")
        self.verticalLayout.addWidget(
            self.enter_button, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.enter_button.clicked.connect(self.handleData)
        self.handleData()  # Load the previous data when the window is opened.

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.port_label.setText(_translate("MainWindow", "Port"))
        self.baudrate_label.setText(_translate("MainWindow", "Baudrate"))
        self.parity_label.setText(_translate("MainWindow", "Parity"))
        self.enter_button.setText(_translate("MainWindow", "Enter"))

    def handleData(self):
        self.getInput()

        if os.path.exists('com.csv'):
            with open('com.csv', newline='') as file:
                reader = csv.reader(file)
                data = list(reader)

            print(data)

            self.loadTableData(data)

    # Takes the input from the input fields and stores them into a csv file.

    def getInput(self):
        port = self.port_input.text()
        baudrate = self.baudrate_input.text()
        parity = self.parity_input.text()

        # Check if the values aren't empty
        if port and baudrate and parity:
            input = [[port,
                      baudrate,
                      parity]]

            print(input)
            with open('com.csv', 'a+') as file:
                writer = csv.writer(file)
                writer.writerows(input)

    def loadTableData(self, data: list):
        self.tableWidget.setColumnCount(3)

        if len(data) > 0:
            rows = len(data)
            self.tableWidget.setRowCount(rows)
            for i in range(len(data)):
                for j in range(len(data[i])):
                    self.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(data[i][j]))
        else:
            self.tableWidget.setRowCount(10)  # Set default row count


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
