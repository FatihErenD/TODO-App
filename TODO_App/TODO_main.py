from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.QtWidgets import *
from first_ui import FirstWindow
from PyQt5 import QtWidgets


class TODOApp(QMainWindow):
    row = 1

    def __init__(self):
        super().__init__()
        self.ui = FirstWindow()
        self.ui.start_ui(self)
        self.ui.pushButton_addToList.clicked.connect(self.save_to_list)
        self.ui.tableWidget.setColumnWidth(0, 150)
        self.ui.tableWidget.setColumnWidth(1, 350)
        self.ui.tableWidget.setColumnWidth(2, 110)
        self.highlight_date = QTextCharFormat()
        self.highlight_date.setBackground(QColor(49, 78, 130))
        self.ui.statusbar.setStyleSheet("background-color: rgb(33, 38, 45);\n"
                                        "font: 12pt \"Mongolian Baiti\";"
                                        "color: rgb(124, 227, 139)")

    def save_to_list(self):
        scan_name = self.ui.lineEditName.text()
        scan_description = self.ui.lineEditDescription.text()
        selected_date = self.ui.calendarWidget.selectedDate().toPyDate().strftime("%d.%m.%Y")
        if scan_name != "":
            self.ui.tableWidget.setRowCount(self.row)
            self.ui.tableWidget.setItem(self.row - 1, 0, QtWidgets.QTableWidgetItem(scan_name))
            self.ui.tableWidget.setItem(self.row - 1, 1, QtWidgets.QTableWidgetItem(scan_description))
            self.ui.tableWidget.setItem(self.row - 1, 2, QtWidgets.QTableWidgetItem(str(selected_date)))
            self.ui.calendarWidget.setDateTextFormat(self.ui.calendarWidget.selectedDate(), self.highlight_date)
            self.ui.statusbar.setStyleSheet("background-color: rgb(33, 38, 45);\n"
                                            "font: 12pt \"Mongolian Baiti\";"
                                            "color: rgb(124, 227, 139)")
            self.ui.statusbar.showMessage("Succesfully Saved", 1000)
            self.row += 1
        else:
            self.ui.statusbar.setStyleSheet("background-color: rgb(33, 38, 45);\n"
                                            "font: 12pt \"Mongolian Baiti\";"
                                            "color: rgb(250, 121, 112)")
            self.ui.statusbar.showMessage("Can't Save Please Give Your Task a Name", 1200)
        self.ui.lineEditName.clear()
        self.ui.lineEditDescription.clear()


uygulama = QApplication([])
pencere = TODOApp()
pencere.show()
uygulama.exec()
