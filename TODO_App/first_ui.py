from PyQt5 import QtCore, QtWidgets


class TODOAppUi():
    def start_ui(self, FirstWindow):
        FirstWindow.resize(1050, 600)
        FirstWindow.setStyleSheet("MainWindow{\n"
                                  "    background-color: rgb(33, 38, 45);\n"
                                  "}")
        self.center = QtWidgets.QWidget(FirstWindow)
        self.center.setStyleSheet("QWidget{\n"
                                  "    background-color: rgb(33, 38, 45);\n"
                                  "}")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.center)
        FirstWindow.setWindowTitle("TODOApp")

        # Table Widget -------------------------------------------------------------------------------------------------
        self.tableWidget = QtWidgets.QTableWidget(self.center)
        self.tableWidget.setMinimumSize(QtCore.QSize(700, 360))
        self.tableWidget.setMaximumSize(QtCore.QSize(1280, 800))
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
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 5)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 350)
        self.tableWidget.setColumnWidth(3, 110)
        self.tableWidget.setHorizontalHeaderLabels(["", "Name", "Description", "Date"])
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        # Table Widget Control -----------------------------------------------------------------------------------------
        # Delete All ---------------------------------------------------------------------------------------------------
        self.tableControlLayout = QtWidgets.QHBoxLayout()
        self.tableControlLayout.setContentsMargins(-1, -1, -1, 10)
        self.deleteAllButton = QtWidgets.QPushButton(self.center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteAllButton.sizePolicy().hasHeightForWidth())
        self.deleteAllButton.setSizePolicy(sizePolicy)
        self.deleteAllButton.setMinimumSize(QtCore.QSize(0, 20))
        self.deleteAllButton.setMaximumSize(QtCore.QSize(70, 20))
        self.deleteAllButton.setStyleSheet("QPushButton{\n"
                                           "    background-color: rgb(22, 27, 34);\n"
                                           "    font: 11pt \"Mongolian Baiti\";\n"
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
        self.deleteAllButton.setText("Delete All")
        self.tableControlLayout.addWidget(self.deleteAllButton)
        # Delete -------------------------------------------------------------------------------------------------------
        self.deleteButton = QtWidgets.QPushButton(self.center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setMinimumSize(QtCore.QSize(0, 20))
        self.deleteButton.setMaximumSize(QtCore.QSize(70, 20))
        self.deleteButton.setStyleSheet("QPushButton{\n"
                                        "    background-color: rgb(22, 27, 34);\n"
                                        "    font: 11pt \"Mongolian Baiti\";\n"
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
        self.deleteButton.setText("Delete")
        self.tableControlLayout.addWidget(self.deleteButton)
        # Up -----------------------------------------------------------------------------------------------------------
        self.upButton = QtWidgets.QPushButton(self.center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upButton.sizePolicy().hasHeightForWidth())
        self.upButton.setSizePolicy(sizePolicy)
        self.upButton.setMinimumSize(QtCore.QSize(0, 20))
        self.upButton.setMaximumSize(QtCore.QSize(70, 20))
        self.upButton.setStyleSheet("QPushButton{\n"
                                    "    background-color: rgb(22, 27, 34);\n"
                                    "    font: 11pt \"Mongolian Baiti\";\n"
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
        self.upButton.setText("Up")
        self.tableControlLayout.addWidget(self.upButton)
        # Down ---------------------------------------------------------------------------------------------------------
        self.downButton = QtWidgets.QPushButton(self.center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downButton.sizePolicy().hasHeightForWidth())
        self.downButton.setSizePolicy(sizePolicy)
        self.downButton.setMinimumSize(QtCore.QSize(0, 20))
        self.downButton.setMaximumSize(QtCore.QSize(70, 20))
        self.downButton.setStyleSheet("QPushButton{\n"
                                      "    background-color: rgb(22, 27, 34);\n"
                                      "    font: 11pt \"Mongolian Baiti\";\n"
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
        self.downButton.setText("Down")
        self.tableControlLayout.addWidget(self.downButton)
        self.gridLayout.addLayout(self.tableControlLayout, 1, 0, 1, 1)

        # Calender Widget ----------------------------------------------------------------------------------------------
        self.calenderLayout = QtWidgets.QVBoxLayout()
        self.calenderLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.calenderLayout.setContentsMargins(-1, -1, -1, 90)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.center)
        self.calendarWidget.setMinimumSize(QtCore.QSize(300, 260))
        self.calendarWidget.setMaximumSize(QtCore.QSize(300, 260))
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setStyleSheet("background-color: rgb(22, 27, 34);\n"
                                          "alternate-background-color: rgb(13, 17, 23);\n"
                                          "border-color: rgb(33, 38, 45);\n"
                                          "font: 10pt \"Mongolian Baiti\";\n"
                                          "color: rgb(198, 205, 213);\n"
                                          "selection-background-color: rgb(198, 205, 213);\n"
                                          "selection-color: rgb(22, 27, 34);")
        self.calendarWidget.setGridVisible(False)
        self.calenderLayout.addWidget(self.calendarWidget)
        self.label = QtWidgets.QLabel(self.center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), "
            "stop:1 rgba(255, 255, 255, 255));")
        self.label.setText("")
        self.calenderLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.calenderLayout, 0, 1, 1, 1)

        # Name ---------------------------------------------------------------------------------------------------------
        self.nameLayout = QtWidgets.QVBoxLayout()
        self.nameLayout.setSpacing(0)
        self.nameLabel = QtWidgets.QLabel(self.center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        self.nameLabel.setStyleSheet("color: rgb(198, 205, 213);\n"
                                     "font: 12pt \"Mongolian Baiti\";\n"
                                     "background-color: rgba(255, 255, 255, 0);")
        self.nameLabel.setText("Name")
        self.nameLayout.addWidget(self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLineEdit.sizePolicy().hasHeightForWidth())
        self.nameLineEdit.setSizePolicy(sizePolicy)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(60, 25))
        self.nameLineEdit.setMaximumSize(QtCore.QSize(250, 25))
        self.nameLineEdit.setStyleSheet("QLineEdit{\n"
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
        self.nameLayout.addWidget(self.nameLineEdit)
        self.gridLayout.addLayout(self.nameLayout, 2, 0, 1, 1)
        # Description --------------------------------------------------------------------------------------------------
        self.descriptionLabel = QtWidgets.QLabel(self.center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descriptionLabel.sizePolicy().hasHeightForWidth())
        self.descriptionLabel.setSizePolicy(sizePolicy)
        self.descriptionLabel.setStyleSheet("color: rgb(198, 205, 213);\n"
                                            "background-color: rgba(255, 255, 255, 0);"
                                            "font: 14pt \"Mongolian Baiti\";\n")
        self.descriptionLabel.setText("Description")
        self.descriptionLineEdit = QtWidgets.QLineEdit(self.center)
        self.descriptionLineEdit.setMinimumSize(QtCore.QSize(250, 25))
        self.descriptionLineEdit.setStyleSheet("QLineEdit{\n"
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
        self.descriptionLayout = QtWidgets.QVBoxLayout()
        self.descriptionLayout.setSpacing(0)
        self.descriptionLayout.addWidget(self.descriptionLabel)
        self.descriptionLayout.addWidget(self.descriptionLineEdit)
        self.gridLayout.addLayout(self.descriptionLayout, 3, 0, 1, 1)
        # Add To List --------------------------------------------------------------------------------------------------
        self.addToListLayout = QtWidgets.QHBoxLayout()
        self.addToListLayout.setContentsMargins(20, -1, 500, -1)
        self.addToListLayout.setObjectName("horizontalLayout_2")
        self.addToListButton = QtWidgets.QPushButton(self.center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addToListButton.sizePolicy().hasHeightForWidth())
        self.addToListButton.setSizePolicy(sizePolicy)
        self.addToListButton.setMinimumSize(QtCore.QSize(0, 25))
        self.addToListButton.setMaximumSize(QtCore.QSize(120, 25))
        self.addToListButton.setStyleSheet("QPushButton{\n"
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
        self.addToListButton.setText("Add to List")
        self.addToListLayout.addWidget(self.addToListButton)
        self.gridLayout.addLayout(self.addToListLayout, 4, 0, 1, 1)

        # Completed Tasks ----------------------------------------------------------------------------------------------
        self.completedTaskLayout = QtWidgets.QHBoxLayout()
        self.completedTaskButton = QtWidgets.QPushButton(self.center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.completedTaskButton.sizePolicy().hasHeightForWidth())
        self.completedTaskButton.setSizePolicy(sizePolicy)
        self.completedTaskButton.setMinimumSize(QtCore.QSize(0, 25))
        self.completedTaskButton.setMaximumSize(QtCore.QSize(220, 25))
        self.completedTaskButton.setStyleSheet("QPushButton{\n"
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
        self.completedTaskButton.setText("Show Completed Tasks")
        self.completedTaskLayout.addWidget(self.completedTaskButton)
        self.gridLayout.addLayout(self.completedTaskLayout, 1, 1, 1, 1)
        # Load From File -----------------------------------------------------------------------------------------------
        self.loadFromFileLayout = QtWidgets.QHBoxLayout()
        self.loadFromFileLayout.setContentsMargins(-1, 10, -1, -1)
        self.loadFromFileButton = QtWidgets.QPushButton(self.center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadFromFileButton.sizePolicy().hasHeightForWidth())
        self.loadFromFileButton.setSizePolicy(sizePolicy)
        self.loadFromFileButton.setMinimumSize(QtCore.QSize(0, 25))
        self.loadFromFileButton.setMaximumSize(QtCore.QSize(220, 25))
        self.loadFromFileButton.setStyleSheet("QPushButton{\n"
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
        self.loadFromFileButton.setText("Load From File")
        self.loadFromFileLayout.addWidget(self.loadFromFileButton)
        self.gridLayout.addLayout(self.loadFromFileLayout, 2, 1, 1, 1)
        # Save To File -------------------------------------------------------------------------------------------------
        self.saveToFileButton = QtWidgets.QPushButton(self.center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveToFileButton.sizePolicy().hasHeightForWidth())
        self.saveToFileButton.setSizePolicy(sizePolicy)
        self.saveToFileButton.setMinimumSize(QtCore.QSize(0, 25))
        self.saveToFileButton.setMaximumSize(QtCore.QSize(220, 25))
        self.saveToFileButton.setStyleSheet("QPushButton{\n"
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
        self.saveToFileButton.setText("Save To File")
        self.saveToFileLayout = QtWidgets.QHBoxLayout()
        self.saveToFileLayout.addWidget(self.saveToFileButton)
        self.gridLayout.addLayout(self.saveToFileLayout, 3, 1, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        FirstWindow.setCentralWidget(self.center)
        self.statusbar = QtWidgets.QStatusBar(FirstWindow)
        self.statusbar.setStyleSheet("background-color: rgb(33, 38, 45);\n"
                                     "font: 12pt \"Mongolian Baiti\";")
        FirstWindow.setStatusBar(self.statusbar)
