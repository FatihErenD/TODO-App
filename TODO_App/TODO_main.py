from PyQt5.QtWidgets import QMainWindow, QWidget, QCheckBox, QTableWidgetItem, QMessageBox, QApplication
from first_ui import TODOAppUi
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from datetime import datetime
import json


class TODOApp(QMainWindow, QWidget):
    tasks = {}
    completed_tasks = {}
    checkBox = []
    row = 1
    completed_task_number = 1

    def __init__(self):
        super().__init__()
        self.ui = TODOAppUi()
        self.ui.start_ui(self)
        self.setWindowTitle("TODOApp")

        self.ui.tableWidget.setColumnWidth(0, 5)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 350)
        self.ui.tableWidget.setColumnWidth(3, 110)

        self.highlight_date = QTextCharFormat()
        self.highlight_date.setBackground(QColor(49, 78, 130))
        self.normal_date = QTextCharFormat()
        self.normal_date.setBackground(QColor(22, 27, 34))

        self.ui.addToListButton.clicked.connect(self.add_to_list)
        self.ui.deleteAllButton.clicked.connect(lambda: self.delete_all(1))
        self.ui.deleteButton.clicked.connect(self.delete_row)
        self.ui.upButton.clicked.connect(self.up_row)
        self.ui.downButton.clicked.connect(self.down_row)
        self.ui.completedTaskButton.clicked.connect(self.show_completed_tasks)
        self.ui.saveToFileButton.clicked.connect(self.save_to_file)
        self.ui.loadFromFileButton.clicked.connect(self.load_from_file)
        self.ui.tableWidget.itemChanged.connect(self.edit_task)

    def remove_from_dict(self, remove_index: int):
        for i in range(remove_index, len(self.tasks)):
            self.tasks[i] = self.tasks[i + 1]
        self.tasks.pop(len(self.tasks))

    def remove_from_calender(self, date):
        count = 0
        for x in self.tasks:
            if date == self.tasks[x]["date"]:
                count += 1
        if count == 0:
            date = QtCore.QDate.fromString(date, "dd.MM.yyyy")
            self.ui.calendarWidget.setDateTextFormat(date, self.normal_date)

    def status_show_message(self, style_type, message, ms):
        if style_type == "error":
            self.ui.statusbar.setStyleSheet("background-color: rgb(33, 38, 45);\n"
                                            "font: 12pt \"Mongolian Baiti\";"
                                            "color: rgb(250, 121, 112)")
        elif style_type == "success":
            self.ui.statusbar.setStyleSheet("background-color: rgb(33, 38, 45);\n"
                                            "font: 12pt \"Mongolian Baiti\";"
                                            "color: rgb(124, 227, 139)")
        self.ui.statusbar.showMessage(message, ms)

    def add_to_list(self):
        scan_name = self.ui.nameLineEdit.text()
        scan_description = self.ui.descriptionLineEdit.text()
        selected_date = self.ui.calendarWidget.selectedDate().toPyDate().strftime("%d.%m.%Y")
        if scan_name != "":
            self.ui.tableWidget.setRowCount(self.row)
            self.tasks[self.row] = {}
            self.tasks[self.row]["name"] = scan_name
            self.tasks[self.row]["description"] = scan_description
            self.tasks[self.row]["date"] = selected_date
            self.ui.tableWidget.setItem(self.row - 1, 1, QtWidgets.QTableWidgetItem(scan_name))
            self.ui.tableWidget.setItem(self.row - 1, 2, QtWidgets.QTableWidgetItem(scan_description))
            self.ui.tableWidget.setItem(self.row - 1, 3, QtWidgets.QTableWidgetItem(str(selected_date)))
            self.checkBox.append(QCheckBox())
            self.checkBox[self.row - 1].setStyleSheet("background-color: rgb(22, 27, 34);")
            self.checkBox[self.row - 1].setObjectName(str(self.row - 1))
            self.ui.tableWidget.setCellWidget(self.row - 1, 0, self.checkBox[self.row - 1])
            self.checkBox[self.row - 1].clicked.connect(self.checked_task)
            self.ui.tableWidget.setStyleSheet("QTableWidget{\n"
                                              "    font: 12pt \"Mongolian Baiti\";\n"
                                              "    color: rgb(198, 205, 213);\n"
                                              "    background-color: rgb(22, 27, 34);\n"
                                              "    border-radius: 25px;\n"
                                              "    selection-background-color: rgb(198, 205, 213);\n"
                                              "    selection-color: rgb(22, 27, 34);\n"
                                              "    alternate-background-color: rgb(255, 255, 255);\n"
                                              "}\n"
                                              "QHeaderView, QHeaderView::section {\n"
                                              "    background-color: rgb(13, 17, 23);\n"
                                              "    color: rgb(198, 205, 213);\n"
                                              "}\n"
                                              "QTableView QTableCornerButton::section{\n"
                                              "    border: 1px solid;\n"
                                              "    border-color: rgba(33, 38, 45, 255);\n"
                                              "    background-color: rgba(33, 38, 45, 255);\n"
                                              "}")
            self.ui.calendarWidget.setDateTextFormat(self.ui.calendarWidget.selectedDate(), self.highlight_date)
            self.status_show_message("success", "Successfully Added", 1000)
            self.row += 1
        else:
            self.status_show_message("error", "Can't Save Please Give Your Task a Name", 1200)
        self.ui.nameLineEdit.clear()
        self.ui.descriptionLineEdit.clear()

    def edit_task(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != -1:
            print(self.tasks)
            if self.tasks[selected_row + 1]["name"] != self.ui.tableWidget.item(selected_row, 1).text() \
                    or self.tasks[selected_row + 1]["description"] != self.ui.tableWidget.item(selected_row, 2).text() \
                    or self.tasks[selected_row + 1]["date"] != self.ui.tableWidget.item(selected_row, 3).text():
                try:
                    is_date = bool(datetime.strptime(self.ui.tableWidget.item(selected_row, 3).text(), "%d.%m.%Y"))
                except ValueError:
                    is_date = False
                if is_date:
                    changed_date = self.tasks[selected_row + 1]["date"]
                    self.tasks[selected_row + 1]["name"] = self.ui.tableWidget.item(selected_row, 1).text()
                    self.tasks[selected_row + 1]["description"] = self.ui.tableWidget.item(selected_row, 2).text()
                    self.tasks[selected_row + 1]["date"] = self.ui.tableWidget.item(selected_row, 3).text()
                    date = QtCore.QDate.fromString(self.tasks[selected_row + 1]["date"], "dd.MM.yyyy")
                    self.remove_from_calender(changed_date)
                    self.ui.calendarWidget.setDateTextFormat(date, self.highlight_date)
                    self.status_show_message("success", "Successfully Changed", 1000)
                else:
                    self.ui.tableWidget.setItem(selected_row, 3, QTableWidgetItem(self.tasks[selected_row + 1]["date"]))
                    self.status_show_message("error",
                                             "Incorrect Date Format. Format Should be dd.mm.yyyy", 2000)

            print(self.tasks)

    def checked_task(self):
        signal = self.sender()
        signal_number = int(signal.objectName())
        if signal.checkState() == Qt.Checked:
            self.ui.tableWidget.removeRow(signal_number)
            self.checkBox.pop(signal_number)
            date = self.tasks[signal_number + 1]["date"]
            self.completed_tasks[self.completed_task_number] = self.tasks[signal_number + 1]
            self.completed_task_number += 1
            self.remove_from_dict(signal_number + 1)
            self.remove_from_calender(date)
            for o in self.checkBox:
                number = int(o.objectName())
                if signal_number < number:
                    o.setObjectName(str(number - 1))
            self.row -= 1

    def delete_all(self, select: int):
        if len(self.tasks) > 0:
            if select == -1:
                for x in self.tasks:
                    date = QtCore.QDate.fromString(self.tasks[x]["date"], "dd.MM.yyyy")
                    self.ui.calendarWidget.setDateTextFormat(date, self.normal_date)
                self.ui.tableWidget.setRowCount(0)
                self.row = 1
                self.tasks = {}
                self.checkBox = []
                self.status_show_message("success", "Successfully Deleted", 1000)
            elif select == 1:
                answer = QMessageBox.question(self, "Are You Sure", "Do you want delete all tasks?",
                                              QMessageBox.Yes | QMessageBox.No)
                if answer == QMessageBox.Yes:
                    for x in self.tasks:
                        date = QtCore.QDate.fromString(self.tasks[x]["date"], "dd.MM.yyyy")
                        self.ui.calendarWidget.setDateTextFormat(date, self.normal_date)
                    self.ui.tableWidget.setRowCount(0)
                    self.row = 1
                    self.tasks = {}
                    self.checkBox = []
                    self.status_show_message("success", "Successfully Deleted", 1000)
        elif select == 1:
            QMessageBox.warning(self, "Warning", "There is nothing to delete.")

    def delete_row(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            self.status_show_message("error", "Please Select a Task to Remove", 1200)
        else:
            date = self.tasks[selected_row + 1]["date"]
            self.ui.tableWidget.removeRow(selected_row)
            self.row -= 1
            self.remove_from_dict(selected_row + 1)
            self.remove_from_calender(date)
            self.status_show_message("success", "Successfully Removed", 1000)

    def show_completed_tasks(self):
        QMessageBox.information(self, "Show Completed Tasks", "Under Maintenance")

    def save_to_file(self):
        answer = QMessageBox.question(self, "Are You Sure",
                                      "Existing file will be deleted. Do you want to continue?",
                                      QMessageBox.Yes | QMessageBox.No)
        if answer == QMessageBox.Yes:
            folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
            if folder != "":
                json_file = json.dumps(self.tasks, indent=2)
                file = open(folder + "/todoapp_tasks.json", "w")
                file.write(json_file)
                file.close()
                self.status_show_message("success", "Successfully Saved To: " + folder, 1200)
            else:
                self.status_show_message("error", "Folder Not Selected", 1000)
        else:
            self.status_show_message("error", "Cant Save", 1000)

    def load_from_file(self):
        answer = QMessageBox.question(self, "Are You Sure",
                                      "Existing tasks will be deleted. Do you want to continue?",
                                      QMessageBox.Yes | QMessageBox.No)
        if answer == QMessageBox.Yes:
            json_file = QtWidgets.QFileDialog.getOpenFileName(self, "Select File", "", "JSON Files (*.json)")
            if json_file != ("", ""):
                file = open(json_file[0])
                readed_dict = json.load(file)
                self.delete_all(-1)
                self.tasks = {}
                self.checkBox = []
                for x in readed_dict:
                    self.tasks[int(x)] = readed_dict[x]
                file.close()
                self.row = 1
                for x in self.tasks:
                    self.ui.tableWidget.setRowCount(self.row)
                    name = self.tasks[x]["name"]
                    description = self.tasks[x]["description"]
                    date = self.tasks[x]["date"]
                    self.ui.tableWidget.setItem(self.row - 1, 1, QtWidgets.QTableWidgetItem(name))
                    self.ui.tableWidget.setItem(self.row - 1, 2, QtWidgets.QTableWidgetItem(description))
                    self.ui.tableWidget.setItem(self.row - 1, 3, QtWidgets.QTableWidgetItem(str(date)))
                    self.checkBox.append(QCheckBox(''))
                    self.checkBox[self.row - 1].setStyleSheet("background-color: rgb(22, 27, 34);")
                    self.checkBox[self.row - 1].setObjectName(str(self.row - 1))
                    self.ui.tableWidget.setCellWidget(self.row - 1, 0, self.checkBox[self.row - 1])
                    self.checkBox[self.row - 1].clicked.connect(self.checked_task)
                    self.ui.tableWidget.setStyleSheet("QTableWidget{\n"
                                                      "    font: 12pt \"Mongolian Baiti\";\n"
                                                      "    color: rgb(198, 205, 213);\n"
                                                      "    background-color: rgb(22, 27, 34);\n"
                                                      "    border-radius: 25px;\n"
                                                      "    selection-background-color: rgb(198, 205, 213);\n"
                                                      "    selection-color: rgb(22, 27, 34);\n"
                                                      "    alternate-background-color: rgb(255, 255, 255);\n"
                                                      "}\n"
                                                      "QHeaderView, QHeaderView::section {\n"
                                                      "    background-color: rgb(13, 17, 23);\n"
                                                      "    color: rgb(198, 205, 213);\n"
                                                      "}\n"
                                                      "QTableView QTableCornerButton::section{\n"
                                                      "    border: 1px solid;\n"
                                                      "    border-color: rgba(33, 38, 45, 255);\n"
                                                      "    background-color: rgba(33, 38, 45, 255);\n"
                                                      "}")
                    date = QtCore.QDate.fromString(date, "dd.MM.yyyy")
                    self.ui.calendarWidget.setDateTextFormat(date, self.highlight_date)
                    self.row += 1
                self.status_show_message("success", "Successfully Loaded", 1000)

    def up_row(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != 0:
            if selected_row == len(self.tasks) - 1:
                self.ui.tableWidget.setRowCount(selected_row + 2)
            else:
                self.ui.tableWidget.insertRow(selected_row + 1)
            temp = self.tasks[selected_row]
            self.tasks[selected_row] = self.tasks[selected_row + 1]
            self.tasks[selected_row + 1] = temp
            temp = self.checkBox[selected_row - 1]
            self.checkBox[selected_row - 1] = self.checkBox[selected_row]
            self.checkBox[selected_row] = temp
            self.checkBox[selected_row].setObjectName(str(int(self.checkBox[selected_row].objectName()) + 1))
            self.checkBox[selected_row - 1].setObjectName(str(int(self.checkBox[selected_row - 1].objectName()) - 1))
            self.ui.tableWidget.setCellWidget(selected_row + 1, 0, self.checkBox[selected_row])
            self.ui.tableWidget.setItem(selected_row + 1, 1, QTableWidgetItem(self.tasks[selected_row + 1]["name"]))
            self.ui.tableWidget.setItem(selected_row + 1, 2,
                                        QTableWidgetItem(self.tasks[selected_row + 1]["description"]))
            self.ui.tableWidget.setItem(selected_row + 1, 3, QTableWidgetItem(self.tasks[selected_row + 1]["date"]))
            self.ui.tableWidget.removeRow(selected_row - 1)
        else:
            self.status_show_message("error", "Already at the Top", 1200)

    def down_row(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row < len(self.tasks) - 1:
            self.ui.tableWidget.insertRow(selected_row)
            temp = self.checkBox[selected_row]
            self.checkBox[selected_row] = self.checkBox[selected_row + 1]
            self.checkBox[selected_row + 1] = temp
            self.checkBox[selected_row].setObjectName(str(int(self.checkBox[selected_row].objectName()) - 1))
            self.checkBox[selected_row + 1].setObjectName(str(int(self.checkBox[selected_row + 1].objectName()) + 1))
            self.ui.tableWidget.setCellWidget(selected_row, 0, self.checkBox[selected_row])
            self.ui.tableWidget.setItem(selected_row, 1,
                                        QTableWidgetItem(self.tasks[selected_row + 2]["name"]))
            self.ui.tableWidget.setItem(selected_row, 2,
                                        QTableWidgetItem(self.tasks[selected_row + 2]["description"]))
            self.ui.tableWidget.setItem(selected_row, 3,
                                        QTableWidgetItem(self.tasks[selected_row + 2]["date"]))
            self.ui.tableWidget.removeRow(selected_row + 2)
            temp = self.tasks[selected_row + 1]
            self.tasks[selected_row + 1] = self.tasks[selected_row + 2]
            self.tasks[selected_row + 2] = temp
        else:
            self.status_show_message("error", "Already at the Bottom", 1200)


uygulama = QApplication([])
pencere = TODOApp()
pencere.show()
uygulama.exec()
