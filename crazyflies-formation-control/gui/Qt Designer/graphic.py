# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crazyflie_multiagent.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 393)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../media/uoa_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_yawrate = QtWidgets.QLabel(self.centralwidget)
        self.label_yawrate.setObjectName("label_yawrate")
        self.gridLayout.addWidget(self.label_yawrate, 2, 6, 1, 1)
        self.edit_yawrate = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_yawrate.setObjectName("edit_yawrate")
        self.gridLayout.addWidget(self.edit_yawrate, 2, 7, 1, 1)
        self.label_pitch = QtWidgets.QLabel(self.centralwidget)
        self.label_pitch.setObjectName("label_pitch")
        self.gridLayout.addWidget(self.label_pitch, 1, 6, 1, 1)
        self.label_thrust = QtWidgets.QLabel(self.centralwidget)
        self.label_thrust.setObjectName("label_thrust")
        self.gridLayout.addWidget(self.label_thrust, 3, 6, 1, 1)
        self.edit_thrust = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_thrust.setObjectName("edit_thrust")
        self.gridLayout.addWidget(self.edit_thrust, 3, 7, 1, 1)
        self.btn_connectall = QtWidgets.QPushButton(self.centralwidget)
        self.btn_connectall.setObjectName("btn_connectall")
        self.gridLayout.addWidget(self.btn_connectall, 1, 0, 1, 1)
        self.edit_pitch = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_pitch.setObjectName("edit_pitch")
        self.gridLayout.addWidget(self.edit_pitch, 1, 7, 1, 1)
        self.edit_roll = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_roll.setObjectName("edit_roll")
        self.gridLayout.addWidget(self.edit_roll, 0, 7, 1, 1)
        self.combobox_drone = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_drone.setObjectName("combobox_drone")
        self.gridLayout.addWidget(self.combobox_drone, 0, 1, 1, 1)
        self.btn_snd_cmd = QtWidgets.QPushButton(self.centralwidget)
        self.btn_snd_cmd.setObjectName("btn_snd_cmd")
        self.gridLayout.addWidget(self.btn_snd_cmd, 4, 5, 1, 3)
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setAutoFillBackground(False)
        self.btn_exit.setObjectName("btn_exit")
        self.gridLayout.addWidget(self.btn_exit, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(81, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(72, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 4, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(89, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 2)
        self.label_roll = QtWidgets.QLabel(self.centralwidget)
        self.label_roll.setObjectName("label_roll")
        self.gridLayout.addWidget(self.label_roll, 0, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(185, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(89, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(89, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 1, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 2, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(69, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 2, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(89, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 1, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(247, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 5, 4, 1, 4)
        spacerItem11 = QtWidgets.QSpacerItem(69, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 3, 4, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(69, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 4, 4, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(81, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 2, 0, 1, 1)
        self.btn_scan = QtWidgets.QPushButton(self.centralwidget)
        self.btn_scan.setObjectName("btn_scan")
        self.gridLayout.addWidget(self.btn_scan, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 488, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuInterface = QtWidgets.QMenu(self.menuBar)
        self.menuInterface.setObjectName("menuInterface")
        MainWindow.setMenuBar(self.menuBar)
        self.action3D_plotter = QtWidgets.QAction(MainWindow)
        self.action3D_plotter.setObjectName("action3D_plotter")
        self.action3D_visualiser = QtWidgets.QAction(MainWindow)
        self.action3D_visualiser.setObjectName("action3D_visualiser")
        self.menuInterface.addSeparator()
        self.menuInterface.addSeparator()
        self.menuInterface.addAction(self.action3D_plotter)
        self.menuInterface.addAction(self.action3D_visualiser)
        self.menuBar.addAction(self.menuInterface.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crazyflie Multiagent"))
        self.label_yawrate.setText(_translate("MainWindow", "Yaw rate"))
        self.label_pitch.setText(_translate("MainWindow", "Pitch"))
        self.label_thrust.setText(_translate("MainWindow", "Thrust"))
        self.btn_connectall.setText(_translate("MainWindow", "Connect all"))
        self.btn_snd_cmd.setText(_translate("MainWindow", "Send command"))
        self.btn_exit.setText(_translate("MainWindow", "EXIT"))
        self.label_roll.setText(_translate("MainWindow", "Roll"))
        self.btn_scan.setText(_translate("MainWindow", "Scan"))
        self.menuInterface.setTitle(_translate("MainWindow", "Interface"))
        self.action3D_plotter.setText(_translate("MainWindow", "Simple Communication"))
        self.action3D_visualiser.setText(_translate("MainWindow", "3D visualiser"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
