from PyQt5 import QtCore, QtWidgets


class CompletedTasksUi():
    def start_ui(self, CompletedWindow):
        CompletedWindow.resize(1050, 610)
        CompletedWindow.setStyleSheet("MainWindow{\n"
                                      "    background-color: rgb(33, 38, 45);\n"
                                      "}")
        self.c_centralwidget = QtWidgets.QWidget(CompletedWindow)
        self.c_centralwidget.setStyleSheet("background-color: rgb(33, 38, 45);\n")
        self.c_gridLayout = QtWidgets.QGridLayout(self.c_centralwidget)
        CompletedWindow.setWindowTitle("Completed Tasks")

        # Table Widget -------------------------------------------------------------------------------------------------
        self.c_tableWidget = QtWidgets.QTableWidget(self.c_centralwidget)
        self.c_tableWidget.setMaximumSize(QtCore.QSize(1280, 720))
        self.c_tableWidget.setStyleSheet("QTableWidget{\n"
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
        self.c_tableWidget.setColumnCount(3)
        self.c_tableWidget.setRowCount(0)
        self.c_tableWidget.setColumnWidth(0, 150)
        self.c_tableWidget.setColumnWidth(1, 430)
        self.c_tableWidget.setColumnWidth(2, 130)
        self.c_tableWidget.setHorizontalHeaderLabels(["Name", "Description", "Date"])
        self.c_gridLayout.addWidget(self.c_tableWidget, 0, 0, 1, 1)

        # Calender Widget ----------------------------------------------------------------------------------------------
        self.calenderLayout = QtWidgets.QVBoxLayout()
        self.calenderLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.calenderLayout.setContentsMargins(-1, -1, -1, 90)
        self.c_calendarWidget = QtWidgets.QCalendarWidget(self.c_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_calendarWidget.sizePolicy().hasHeightForWidth())
        self.c_calendarWidget.setSizePolicy(sizePolicy)
        self.c_calendarWidget.setMinimumSize(QtCore.QSize(300, 260))
        self.c_calendarWidget.setMaximumSize(QtCore.QSize(300, 260))
        self.c_calendarWidget.setAutoFillBackground(False)
        self.c_calendarWidget.setStyleSheet("background-color: rgb(22, 27, 34);\n"
                                            "alternate-background-color: rgb(13, 17, 23);\n"
                                            "border-color: rgb(33, 38, 45);\n"
                                            "font: 10pt \"Mongolian Baiti\";\n"
                                            "color: rgb(198, 205, 213);\n"
                                            "selection-background-color: rgb(198, 205, 213);\n"
                                            "selection-color: rgb(22, 27, 34);")
        self.c_calendarWidget.setGridVisible(False)
        self.calenderLayout.addWidget(self.c_calendarWidget)
        self.c_emptyLabel_1 = QtWidgets.QLabel(self.c_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_emptyLabel_1.sizePolicy().hasHeightForWidth())
        self.c_emptyLabel_1.setSizePolicy(sizePolicy)
        self.c_emptyLabel_1.setMaximumSize(QtCore.QSize(10, 720))
        self.c_emptyLabel_1.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), "
            "stop:1 rgba(255, 255, 255, 255));")
        self.c_emptyLabel_1.setText("")
        self.calenderLayout.addWidget(self.c_emptyLabel_1)
        self.c_gridLayout.addLayout(self.calenderLayout, 0, 1, 1, 1)

        # Delete All ---------------------------------------------------------------------------------------------------
        self.c_verticalLayout = QtWidgets.QVBoxLayout()
        self.c_verticalLayout.setObjectName("verticalLayout")
        self.c_deleteAllButton = QtWidgets.QPushButton(self.c_centralwidget)
        self.c_deleteAllButton.setMinimumSize(QtCore.QSize(220, 30))
        self.c_deleteAllButton.setStyleSheet("QPushButton{\n"
                                             "    background-color: rgb(22, 27, 34);\n"
                                             "    font: 14pt \"Mongolian Baiti\";\n"
                                             "    color: rgb(198, 205, 213);\n"
                                             "    border-radius: 10px;\n"
                                             "}\n"
                                             "QPushButton::hover{\n"
                                             "    color: rgb(22, 27, 34);\n"
                                             "    background-color: rgb(198, 205, 213);\n"
                                             "}\n"
                                             "QPushButton::pressed{\n"
                                             "    border: 2px solid;\n"
                                             "    border-color: rgb(13, 17, 23);\n"
                                             "    padding-top: 3px;\n"
                                             "}")
        self.c_deleteAllButton.setText("Delete All")
        self.c_verticalLayout.addWidget(self.c_deleteAllButton)

        self.c_emptyLabel_2 = QtWidgets.QLabel(self.c_centralwidget)
        sizePolicy.setHeightForWidth(self.c_emptyLabel_2.sizePolicy().hasHeightForWidth())
        self.c_emptyLabel_2.setSizePolicy(sizePolicy)
        self.c_emptyLabel_2.setMaximumSize(QtCore.QSize(10, 20))
        self.c_emptyLabel_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), "
            "stop:1 rgba(255, 255, 255, 255));")
        self.c_emptyLabel_2.setText("")
        self.c_verticalLayout.addWidget(self.c_emptyLabel_2)

        # Delete -------------------------------------------------------------------------------------------------------
        self.c_deleteButton = QtWidgets.QPushButton(self.c_centralwidget)
        self.c_deleteButton.setMinimumSize(QtCore.QSize(220, 30))
        self.c_deleteButton.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(22, 27, 34);\n"
                                          "    font: 14pt \"Mongolian Baiti\";\n"
                                          "    color: rgb(198, 205, 213);\n"
                                          "    border-radius: 10px;\n"
                                          "}\n"
                                          "QPushButton::hover{\n"
                                          "    color: rgb(22, 27, 34);\n"
                                          "    background-color: rgb(198, 205, 213);\n"
                                          "}\n"
                                          "QPushButton::pressed{\n"
                                          "    border: 2px solid;\n"
                                          "    border-color: rgb(13, 17, 23);\n"
                                          "    padding-top: 3px;\n"
                                          "}")
        self.c_deleteButton.setText("Delete")
        self.c_verticalLayout.addWidget(self.c_deleteButton)

        # Save to File -------------------------------------------------------------------------------------------------
        self.c_emptyLabel_3 = QtWidgets.QLabel(self.c_centralwidget)
        sizePolicy.setHeightForWidth(self.c_emptyLabel_3.sizePolicy().hasHeightForWidth())
        self.c_emptyLabel_3.setSizePolicy(sizePolicy)
        self.c_emptyLabel_3.setMaximumSize(QtCore.QSize(10, 20))
        self.c_emptyLabel_3.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), "
            "stop:1 rgba(255, 255, 255, 255));")
        self.c_emptyLabel_3.setText("")
        self.c_emptyLabel_3.setObjectName("emptyLabel_4")
        self.c_verticalLayout.addWidget(self.c_emptyLabel_3)
        self.c_saveToFileButton = QtWidgets.QPushButton(self.c_centralwidget)
        self.c_saveToFileButton.setMinimumSize(QtCore.QSize(220, 30))
        self.c_saveToFileButton.setStyleSheet("QPushButton{\n"
                                              "    background-color: rgb(22, 27, 34);\n"
                                              "    font: 14pt \"Mongolian Baiti\";\n"
                                              "    color: rgb(198, 205, 213);\n"
                                              "    border-radius: 10px;\n"
                                              "}\n"
                                              "QPushButton::hover{\n"
                                              "    color: rgb(22, 27, 34);\n"
                                              "    background-color: rgb(198, 205, 213);\n"
                                              "}\n"
                                              "QPushButton::pressed{\n"
                                              "    border: 2px solid;\n"
                                              "    border-color: rgb(13, 17, 23);\n"
                                              "    padding-top: 3px;\n"
                                              "}")
        self.c_saveToFileButton.setText("Save to File")
        self.c_verticalLayout.addWidget(self.c_saveToFileButton)

        # Load From File -----------------------------------------------------------------------------------------------
        self.c_emptyLabel_4 = QtWidgets.QLabel(self.c_centralwidget)
        sizePolicy.setHeightForWidth(self.c_emptyLabel_4.sizePolicy().hasHeightForWidth())
        self.c_emptyLabel_4.setSizePolicy(sizePolicy)
        self.c_emptyLabel_4.setMaximumSize(QtCore.QSize(10, 20))
        self.c_emptyLabel_4.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), "
            "stop:1 rgba(255, 255, 255, 255));")
        self.c_emptyLabel_4.setText("")
        self.c_verticalLayout.addWidget(self.c_emptyLabel_4)
        self.c_loadFromFileButton = QtWidgets.QPushButton(self.c_centralwidget)
        self.c_loadFromFileButton.setMinimumSize(QtCore.QSize(220, 30))
        self.c_loadFromFileButton.setStyleSheet("QPushButton{\n"
                                                "    background-color: rgb(22, 27, 34);\n"
                                                "    font: 14pt \"Mongolian Baiti\";\n"
                                                "    color: rgb(198, 205, 213);\n"
                                                "    border-radius: 10px;\n"
                                                "}\n"
                                                "QPushButton::hover{\n"
                                                "    color: rgb(22, 27, 34);\n"
                                                "    background-color: rgb(198, 205, 213);\n"
                                                "}\n"
                                                "QPushButton::pressed{\n"
                                                "    border: 2px solid;\n"
                                                "    border-color: rgb(13, 17, 23);\n"
                                                "    padding-top: 3px;\n"
                                                "}")
        self.c_loadFromFileButton.setText("Load From File")
        self.c_verticalLayout.addWidget(self.c_loadFromFileButton)
        self.c_emptyLabel_5 = QtWidgets.QLabel(self.c_centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_emptyLabel_5.sizePolicy().hasHeightForWidth())
        self.c_emptyLabel_5.setSizePolicy(sizePolicy)
        self.c_emptyLabel_5.setMaximumSize(QtCore.QSize(10, 200))
        self.c_emptyLabel_5.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), "
            "stop:1 rgba(255, 255, 255, 255));")
        self.c_emptyLabel_5.setText("")
        self.c_verticalLayout.addWidget(self.c_emptyLabel_5)
        self.c_gridLayout.addLayout(self.c_verticalLayout, 1, 0, 1, 2)
        CompletedWindow.setCentralWidget(self.c_centralwidget)
