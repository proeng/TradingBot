# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1153, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Filed_Orders_lbx = QtWidgets.QListView(self.centralwidget)
        self.Filed_Orders_lbx.setGeometry(QtCore.QRect(530, 30, 291, 211))
        self.Filed_Orders_lbx.setObjectName("Filed_Orders_lbx")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 10, 101, 16))
        self.label_5.setObjectName("label_5")
        self.Pending_Orders_lbx = QtWidgets.QListView(self.centralwidget)
        self.Pending_Orders_lbx.setGeometry(QtCore.QRect(530, 270, 291, 211))
        self.Pending_Orders_lbx.setObjectName("Pending_Orders_lbx")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 250, 111, 16))
        self.label_6.setObjectName("label_6")
        self.Login_gbx = QtWidgets.QGroupBox(self.centralwidget)
        self.Login_gbx.setGeometry(QtCore.QRect(10, 10, 471, 141))
        self.Login_gbx.setObjectName("Login_gbx")
        self.Api_Key_tbx = QtWidgets.QLineEdit(self.Login_gbx)
        self.Api_Key_tbx.setGeometry(QtCore.QRect(90, 30, 351, 20))
        self.Api_Key_tbx.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Api_Key_tbx.setObjectName("Api_Key_tbx")
        self.Api_Signature_tbx = QtWidgets.QLineEdit(self.Login_gbx)
        self.Api_Signature_tbx.setGeometry(QtCore.QRect(90, 70, 351, 20))
        self.Api_Signature_tbx.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Api_Signature_tbx.setObjectName("Api_Signature_tbx")
        self.Login_Status_Display_lbl = QtWidgets.QLabel(self.Login_gbx)
        self.Login_Status_Display_lbl.setGeometry(QtCore.QRect(10, 120, 141, 16))
        self.Login_Status_Display_lbl.setObjectName("Login_Status_Display_lbl")
        self.Login_Connect_btn = QtWidgets.QPushButton(self.Login_gbx)
        self.Login_Connect_btn.setGeometry(QtCore.QRect(380, 110, 75, 23))
        self.Login_Connect_btn.setObjectName("Login_Connect_btn")
        self.label_2 = QtWidgets.QLabel(self.Login_gbx)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.Login_gbx)
        self.label.setGeometry(QtCore.QRect(10, 30, 51, 16))
        self.label.setObjectName("label")
        self.Transaction_gbx = QtWidgets.QGroupBox(self.centralwidget)
        self.Transaction_gbx.setGeometry(QtCore.QRect(10, 330, 471, 171))
        self.Transaction_gbx.setObjectName("Transaction_gbx")
        self.label_4 = QtWidgets.QLabel(self.Transaction_gbx)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 61, 16))
        self.label_4.setObjectName("label_4")
        self.Transaction_Symbol_cbx = QtWidgets.QComboBox(self.Transaction_gbx)
        self.Transaction_Symbol_cbx.setGeometry(QtCore.QRect(380, 100, 71, 22))
        self.Transaction_Symbol_cbx.setObjectName("Transaction_Symbol_cbx")
        self.Transaction_Execute_btn = QtWidgets.QPushButton(self.Transaction_gbx)
        self.Transaction_Execute_btn.setGeometry(QtCore.QRect(380, 140, 75, 23))
        self.Transaction_Execute_btn.setObjectName("Transaction_Execute_btn")
        self.label_10 = QtWidgets.QLabel(self.Transaction_gbx)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Transaction_gbx)
        self.label_11.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.Transaction_gbx)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_13.setObjectName("label_13")
        self.Transaction_Amount_Procent_Display_hsr = QtWidgets.QSlider(self.Transaction_gbx)
        self.Transaction_Amount_Procent_Display_hsr.setGeometry(QtCore.QRect(90, 20, 131, 22))
        self.Transaction_Amount_Procent_Display_hsr.setMaximum(100)
        self.Transaction_Amount_Procent_Display_hsr.setOrientation(QtCore.Qt.Horizontal)
        self.Transaction_Amount_Procent_Display_hsr.setObjectName("Transaction_Amount_Procent_Display_hsr")
        self.Transaction_Amount_Procent_Display_lbl = QtWidgets.QLabel(self.Transaction_gbx)
        self.Transaction_Amount_Procent_Display_lbl.setGeometry(QtCore.QRect(230, 20, 61, 16))
        self.Transaction_Amount_Procent_Display_lbl.setObjectName("Transaction_Amount_Procent_Display_lbl")
        self.label_15 = QtWidgets.QLabel(self.Transaction_gbx)
        self.label_15.setGeometry(QtCore.QRect(310, 100, 41, 20))
        self.label_15.setObjectName("label_15")
        self.Transaction_Status_Display_lbl = QtWidgets.QLabel(self.Transaction_gbx)
        self.Transaction_Status_Display_lbl.setGeometry(QtCore.QRect(10, 150, 321, 16))
        self.Transaction_Status_Display_lbl.setObjectName("Transaction_Status_Display_lbl")
        self.Transaction_Buy_in_tbx = QtWidgets.QLineEdit(self.Transaction_gbx)
        self.Transaction_Buy_in_tbx.setGeometry(QtCore.QRect(90, 50, 131, 20))
        self.Transaction_Buy_in_tbx.setObjectName("Transaction_Buy_in_tbx")
        self.Transaction_Target_tbx = QtWidgets.QLineEdit(self.Transaction_gbx)
        self.Transaction_Target_tbx.setGeometry(QtCore.QRect(90, 80, 131, 20))
        self.Transaction_Target_tbx.setObjectName("Transaction_Target_tbx")
        self.Transaction_Stop_Limit_tbx = QtWidgets.QLineEdit(self.Transaction_gbx)
        self.Transaction_Stop_Limit_tbx.setGeometry(QtCore.QRect(90, 110, 131, 20))
        self.Transaction_Stop_Limit_tbx.setObjectName("Transaction_Stop_Limit_tbx")
        self.Transaction_Currency_cbx = QtWidgets.QComboBox(self.Transaction_gbx)
        self.Transaction_Currency_cbx.setGeometry(QtCore.QRect(380, 70, 71, 22))
        self.Transaction_Currency_cbx.setEditable(False)
        self.Transaction_Currency_cbx.setObjectName("Transaction_Currency_cbx")
        self.label_16 = QtWidgets.QLabel(self.Transaction_gbx)
        self.label_16.setGeometry(QtCore.QRect(310, 70, 51, 20))
        self.label_16.setObjectName("label_16")
        self.Transaction_Account_Balance_Display_lbl = QtWidgets.QLabel(self.Transaction_gbx)
        self.Transaction_Account_Balance_Display_lbl.setGeometry(QtCore.QRect(310, 20, 151, 20))
        self.Transaction_Account_Balance_Display_lbl.setObjectName("Transaction_Account_Balance_Display_lbl")
        self.Transaction_Current_Price_Display_lbl = QtWidgets.QLabel(self.Transaction_gbx)
        self.Transaction_Current_Price_Display_lbl.setGeometry(QtCore.QRect(310, 40, 151, 20))
        self.Transaction_Current_Price_Display_lbl.setObjectName("Transaction_Current_Price_Display_lbl")
        self.Clear_Pending_Orders_btn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Clear_Pending_Orders_btn.setGeometry(QtCore.QRect(620, 490, 191, 41))
        self.Clear_Pending_Orders_btn.setObjectName("Clear_Pending_Orders_btn")
        self.Force_Sell_btn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Force_Sell_btn.setGeometry(QtCore.QRect(1020, 490, 191, 41))
        self.Force_Sell_btn.setObjectName("Force_Sell_btn")
        self.Strategy_gbx = QtWidgets.QGroupBox(self.centralwidget)
        self.Strategy_gbx.setGeometry(QtCore.QRect(10, 180, 471, 141))
        self.Strategy_gbx.setObjectName("Strategy_gbx")
        self.Strategy_Target_Procent_Display_lbl = QtWidgets.QLabel(self.Strategy_gbx)
        self.Strategy_Target_Procent_Display_lbl.setGeometry(QtCore.QRect(230, 70, 61, 16))
        self.Strategy_Target_Procent_Display_lbl.setObjectName("Strategy_Target_Procent_Display_lbl")
        self.Strategy_Target_Procent_hsr = QtWidgets.QSlider(self.Strategy_gbx)
        self.Strategy_Target_Procent_hsr.setGeometry(QtCore.QRect(90, 70, 131, 22))
        self.Strategy_Target_Procent_hsr.setMaximum(100)
        self.Strategy_Target_Procent_hsr.setProperty("value", 0)
        self.Strategy_Target_Procent_hsr.setOrientation(QtCore.Qt.Horizontal)
        self.Strategy_Target_Procent_hsr.setObjectName("Strategy_Target_Procent_hsr")
        self.Strategy_Stop_Limit_Procent_hsr = QtWidgets.QSlider(self.Strategy_gbx)
        self.Strategy_Stop_Limit_Procent_hsr.setGeometry(QtCore.QRect(90, 100, 131, 22))
        self.Strategy_Stop_Limit_Procent_hsr.setMaximum(100)
        self.Strategy_Stop_Limit_Procent_hsr.setOrientation(QtCore.Qt.Horizontal)
        self.Strategy_Stop_Limit_Procent_hsr.setObjectName("Strategy_Stop_Limit_Procent_hsr")
        self.Strategy_Stop_Limit_Procent_Display_lbl = QtWidgets.QLabel(self.Strategy_gbx)
        self.Strategy_Stop_Limit_Procent_Display_lbl.setGeometry(QtCore.QRect(230, 100, 61, 16))
        self.Strategy_Stop_Limit_Procent_Display_lbl.setObjectName("Strategy_Stop_Limit_Procent_Display_lbl")
        self.label_18 = QtWidgets.QLabel(self.Strategy_gbx)
        self.label_18.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.Strategy_gbx)
        self.label_19.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.Strategy_gbx)
        self.label_20.setGeometry(QtCore.QRect(10, 30, 61, 16))
        self.label_20.setObjectName("label_20")
        self.Strategy_Ratio_High_sbx = QtWidgets.QSpinBox(self.Strategy_gbx)
        self.Strategy_Ratio_High_sbx.setGeometry(QtCore.QRect(90, 30, 51, 22))
        self.Strategy_Ratio_High_sbx.setObjectName("Strategy_Ratio_High_sbx")
        self.Strategy_Ratio_Low_sbx = QtWidgets.QSpinBox(self.Strategy_gbx)
        self.Strategy_Ratio_Low_sbx.setGeometry(QtCore.QRect(160, 30, 51, 22))
        self.Strategy_Ratio_Low_sbx.setObjectName("Strategy_Ratio_Low_sbx")
        self.label_21 = QtWidgets.QLabel(self.Strategy_gbx)
        self.label_21.setGeometry(QtCore.QRect(150, 30, 16, 16))
        self.label_21.setObjectName("label_21")
        self.Strategy_Apply_btn = QtWidgets.QPushButton(self.Strategy_gbx)
        self.Strategy_Apply_btn.setGeometry(QtCore.QRect(380, 110, 75, 23))
        self.Strategy_Apply_btn.setObjectName("Strategy_Apply_btn")
        self.Market_Buy_chbx = QtWidgets.QCheckBox(self.Strategy_gbx)
        self.Market_Buy_chbx.setGeometry(QtCore.QRect(380, 80, 101, 17))
        self.Market_Buy_chbx.setObjectName("Market_Buy_chbx")
        self.Paper_trade_chbx = QtWidgets.QCheckBox(self.centralwidget)
        self.Paper_trade_chbx.setGeometry(QtCore.QRect(400, 160, 101, 17))
        self.Paper_trade_chbx.setObjectName("Paper_trade_chbx")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(840, 10, 111, 16))
        self.label_7.setObjectName("label_7")
        self.Closed_Orders_lbx = QtWidgets.QListView(self.centralwidget)
        self.Closed_Orders_lbx.setGeometry(QtCore.QRect(840, 30, 291, 451))
        self.Closed_Orders_lbx.setObjectName("Closed_Orders_lbx")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1153, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionView = QtWidgets.QAction(MainWindow)
        self.actionView.setObjectName("actionView")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trader Bot"))
        self.label_5.setText(_translate("MainWindow", "Active Transactions"))
        self.label_6.setText(_translate("MainWindow", "Pending Transactions"))
        self.Login_gbx.setTitle(_translate("MainWindow", "Login"))
        self.Login_Status_Display_lbl.setText(_translate("MainWindow", "Status:"))
        self.Login_Connect_btn.setText(_translate("MainWindow", "Connect"))
        self.label_2.setText(_translate("MainWindow", "Api_Signature:"))
        self.label.setText(_translate("MainWindow", "Api_Key:"))
        self.Transaction_gbx.setTitle(_translate("MainWindow", "Transaction"))
        self.label_4.setText(_translate("MainWindow", "Stop Loss:"))
        self.Transaction_Execute_btn.setText(_translate("MainWindow", "Execute"))
        self.label_10.setText(_translate("MainWindow", "Buy In:"))
        self.label_11.setText(_translate("MainWindow", "Target:"))
        self.label_13.setText(_translate("MainWindow", "Amount:"))
        self.Transaction_Amount_Procent_Display_lbl.setText(_translate("MainWindow", "0%"))
        self.label_15.setText(_translate("MainWindow", "Asset:"))
        self.Transaction_Status_Display_lbl.setText(_translate("MainWindow", "Status:"))
        self.label_16.setText(_translate("MainWindow", "Currency:"))
        self.Transaction_Account_Balance_Display_lbl.setText(_translate("MainWindow", "Balance:"))
        self.Transaction_Current_Price_Display_lbl.setText(_translate("MainWindow", "Asset Price:"))
        self.Clear_Pending_Orders_btn.setText(_translate("MainWindow", "Clear Pending Orders"))
        self.Force_Sell_btn.setText(_translate("MainWindow", "Force Sell"))
        self.Strategy_gbx.setTitle(_translate("MainWindow", "Strategy"))
        self.Strategy_Target_Procent_Display_lbl.setText(_translate("MainWindow", "0%"))
        self.Strategy_Stop_Limit_Procent_Display_lbl.setText(_translate("MainWindow", "0%"))
        self.label_18.setText(_translate("MainWindow", "Target:"))
        self.label_19.setText(_translate("MainWindow", "Stop Loss:"))
        self.label_20.setText(_translate("MainWindow", "Ratio:"))
        self.label_21.setText(_translate("MainWindow", ":"))
        self.Strategy_Apply_btn.setText(_translate("MainWindow", "Apply"))
        self.Market_Buy_chbx.setText(_translate("MainWindow", "Market Buy"))
        self.Paper_trade_chbx.setText(_translate("MainWindow", "Paper Trade"))
        self.label_7.setText(_translate("MainWindow", "Closed Transactions"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionView.setText(_translate("MainWindow", "View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

