from PyQt5 import QtCore, QtGui, QtWidgets


class FirstWindow(object):

    def start_ui(self, MainWindow):
        MainWindow.setWindowTitle("TODO")
        MainWindow.resize(1000, 650)
        MainWindow.setStyleSheet("MainWindow{\n"
                                 "    background-color: rgb(33, 38, 45);\n"
                                 "}")
        # --------------------------------------------------------------------------------------------------------------
        self.page = QtWidgets.QWidget(MainWindow)
        self.page.setStyleSheet("QWidget{\n"
                                "    background-color: rgb(33, 38, 45);\n"
                                "}")
        # --------------------------------------------------------------------------------------------------------------
        self.widget = QtWidgets.QWidget(self.page)
        self.widget.setGeometry(QtCore.QRect(20, 20, 15, 23))
        MainWindow.setCentralWidget(self.page)
        # --------------------------------------------------------------------------------------------------------------
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: rgb(33, 38, 45);\n"
                                     "font: 12pt \"Mongolian Baiti\";"
                                     "color: rgb(124, 227, 139)")
        MainWindow.setStatusBar(self.statusbar)
        # --------------------------------------------------------------------------------------------------------------
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 625, 310))
        self.tableWidget.setStyleSheet("QTableWidget{\n"
                                       "    font: 12pt \"Mongolian Baiti\";\n"
                                       "    color: rgb(198, 205, 213);\n"
                                       "    background-color: rgb(22, 27, 34);\n"
                                       "    border-radius: 15px;\n"
                                       "    selection-background-color: rgb(198, 205, 213);\n"
                                       "    selection-color: rgb(22, 27, 34);\n"
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
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Name"))
        self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Description"))
        self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Date"))
        # --------------------------------------------------------------------------------------------------------------
        self.calendarWidget = QtWidgets.QCalendarWidget(self.page)
        self.calendarWidget.setGeometry(QtCore.QRect(660, 20, 320, 240))
        self.calendarWidget.setStyleSheet("background-color: rgb(22, 27, 34);\n"
                                          "alternate-background-color: rgb(13, 17, 23);\n"
                                          "border-color: rgb(33, 38, 45);\n"
                                          "font: 10pt \"Mongolian Baiti\";\n"
                                          "color: rgb(198, 205, 213);\n"
                                          "selection-background-color: rgb(198, 205, 213);\n"
                                          "selection-color: rgb(22, 27, 34);")
        self.labelName = QtWidgets.QLabel(self.page)
        self.labelName.setGeometry(QtCore.QRect(40, 350, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.labelName.setFont(font)
        self.labelName.setStyleSheet("color: rgb(198, 205, 213);\n"
                                     "background-color: rgba(255, 255, 255, 0);")
        self.labelName.setText("Name")
        # --------------------------------------------------------------------------------------------------------------
        self.lineEditName = QtWidgets.QLineEdit(self.page)
        self.lineEditName.setGeometry(QtCore.QRect(30, 370, 240, 30))
        self.lineEditName.setStyleSheet("QLineEdit{\n"
                                        "    background-color: rgb(22, 27, 34);\n"
                                        "    border: none;\n"
                                        "    border-radius: 10px;\n"
                                        "    font: 12pt \"Mongolian Baiti\";\n"
                                        "    color: rgb(198, 205, 213);\n"
                                        "}\n"
                                        "QLineEdit::focus{\n"
                                        "    border: 2px solid;\n"
                                        "    border-color: rgb(22, 27, 34);\n"
                                        "    background-color: rgb(33, 38, 45)\n"
                                        "}")
        # --------------------------------------------------------------------------------------------------------------
        self.labelDescription = QtWidgets.QLabel(self.page)
        self.labelDescription.setGeometry(QtCore.QRect(40, 410, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.labelDescription.setFont(font)
        self.labelDescription.setStyleSheet("color: rgb(198, 205, 213);\n"
                                            "background-color: rgba(255, 255, 255, 0);")
        self.labelDescription.setText("Description")
        # --------------------------------------------------------------------------------------------------------------
        self.lineEditDescription = QtWidgets.QLineEdit(self.page)
        self.lineEditDescription.setGeometry(QtCore.QRect(30, 430, 450, 30))
        self.lineEditDescription.setStyleSheet("QLineEdit{\n"
                                               "    background-color: rgb(22, 27, 34);\n"
                                               "    border: none;\n"
                                               "    border-radius: 10px;\n"
                                               "    font: 12pt \"Mongolian Baiti\";\n"
                                               "    color: rgb(198, 205, 213);\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit::focus{\n"
                                               "    border: 2px solid;\n"
                                               "    border-color: rgb(22, 27, 34);\n"
                                               "    background-color: rgb(33, 38, 45)\n"
                                               "}")
        # --------------------------------------------------------------------------------------------------------------
        self.pushButton_addToList = QtWidgets.QPushButton(self.page)
        self.pushButton_addToList.setGeometry(QtCore.QRect(40, 480, 150, 30))
        self.pushButton_addToList.setStyleSheet("QPushButton{\n"
                                                "    background-color: rgb(22, 27, 34);\n"
                                                "    font: 14pt \"Mongolian Baiti\";\n"
                                                "    color: rgb(198, 205, 213);\n"
                                                "    border-radius: 10px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton::hover{\n"
                                                "    color: rgb(22, 27, 34);\n"
                                                "    background-color: rgb(198, 205, 213);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton::pressed{\n"
                                                "    border: 2px solid;\n"
                                                "    border-color: rgb(13, 17, 23);\n"
                                                "    padding-top: 3px;\n"
                                                "}\n"
                                                "")
        self.pushButton_addToList.setText("Add to List")
        # --------------------------------------------------------------------------------------------------------------
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
