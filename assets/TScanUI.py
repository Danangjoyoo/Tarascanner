# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 640)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 640))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 640))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 180, 1061, 401))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.scannerTab = QtWidgets.QWidget()
        self.scannerTab.setObjectName("scannerTab")
        self.groupBox_main = QtWidgets.QGroupBox(self.scannerTab)
        self.groupBox_main.setGeometry(QtCore.QRect(20, 20, 291, 161))
        self.groupBox_main.setStyleSheet("b")
        self.groupBox_main.setObjectName("groupBox_main")
        self.pushButton_startScanner = QtWidgets.QPushButton(self.groupBox_main)
        self.pushButton_startScanner.setGeometry(QtCore.QRect(70, 105, 131, 41))
        self.pushButton_startScanner.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_startScanner.setObjectName("pushButton_startScanner")
        self.checkBox_connectDbase = QtWidgets.QCheckBox(self.groupBox_main)
        self.checkBox_connectDbase.setGeometry(QtCore.QRect(70, 70, 131, 20))
        self.checkBox_connectDbase.setObjectName("checkBox_connectDbase")
        self.comboBox_camID = QtWidgets.QComboBox(self.groupBox_main)
        self.comboBox_camID.setGeometry(QtCore.QRect(140, 30, 61, 22))
        self.comboBox_camID.setObjectName("comboBox_camID")
        self.comboBox_camID.addItem("")
        self.comboBox_camID.addItem("")
        self.comboBox_camID.addItem("")
        self.label_camID = QtWidgets.QLabel(self.groupBox_main)
        self.label_camID.setGeometry(QtCore.QRect(70, 32, 71, 16))
        self.label_camID.setObjectName("label_camID")
        self.tableView_dbase = QtWidgets.QTableView(self.scannerTab)
        self.tableView_dbase.setGeometry(QtCore.QRect(330, 30, 721, 331))
        self.tableView_dbase.setObjectName("tableView_dbase")
        self.label_dbMonitor = QtWidgets.QLabel(self.scannerTab)
        self.label_dbMonitor.setGeometry(QtCore.QRect(330, 10, 221, 16))
        self.label_dbMonitor.setObjectName("label_dbMonitor")
        self.groupBox_dbControl = QtWidgets.QGroupBox(self.scannerTab)
        self.groupBox_dbControl.setGeometry(QtCore.QRect(20, 190, 291, 171))
        self.groupBox_dbControl.setObjectName("groupBox_dbControl")
        self.comboBox_dbaseKeys = QtWidgets.QComboBox(self.groupBox_dbControl)
        self.comboBox_dbaseKeys.setGeometry(QtCore.QRect(100, 60, 171, 22))
        self.comboBox_dbaseKeys.setObjectName("comboBox_dbaseKeys")
        self.label_columnRef = QtWidgets.QLabel(self.groupBox_dbControl)
        self.label_columnRef.setGeometry(QtCore.QRect(40, 60, 51, 16))
        self.label_columnRef.setObjectName("label_columnRef")
        self.label_rowRef = QtWidgets.QLabel(self.groupBox_dbControl)
        self.label_rowRef.setGeometry(QtCore.QRect(40, 30, 61, 16))
        self.label_rowRef.setObjectName("label_rowRef")
        self.pushButton_insert = QtWidgets.QPushButton(self.groupBox_dbControl)
        self.pushButton_insert.setGeometry(QtCore.QRect(20, 130, 51, 31))
        self.pushButton_insert.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_insert.setObjectName("pushButton_insert")
        self.lineEdit_inputMod = QtWidgets.QLineEdit(self.groupBox_dbControl)
        self.lineEdit_inputMod.setGeometry(QtCore.QRect(100, 90, 171, 22))
        self.lineEdit_inputMod.setObjectName("lineEdit_inputMod")
        self.label_valueRef = QtWidgets.QLabel(self.groupBox_dbControl)
        self.label_valueRef.setGeometry(QtCore.QRect(40, 90, 41, 16))
        self.label_valueRef.setObjectName("label_valueRef")
        self.pushButton_insertTime = QtWidgets.QPushButton(self.groupBox_dbControl)
        self.pushButton_insertTime.setGeometry(QtCore.QRect(80, 130, 121, 31))
        self.pushButton_insertTime.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_insertTime.setObjectName("pushButton_insertTime")
        self.comboBox_dbaseRows = QtWidgets.QComboBox(self.groupBox_dbControl)
        self.comboBox_dbaseRows.setGeometry(QtCore.QRect(100, 30, 171, 22))
        self.comboBox_dbaseRows.setObjectName("comboBox_dbaseRows")
        self.pushButton_reset = QtWidgets.QPushButton(self.groupBox_dbControl)
        self.pushButton_reset.setGeometry(QtCore.QRect(210, 130, 61, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_reset.setFont(font)
        self.pushButton_reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.tabWidget.addTab(self.scannerTab, "")
        self.generatorTab = QtWidgets.QWidget()
        self.generatorTab.setObjectName("generatorTab")
        self.groupBox_generateSingle = QtWidgets.QGroupBox(self.generatorTab)
        self.groupBox_generateSingle.setGeometry(QtCore.QRect(20, 20, 421, 341))
        self.groupBox_generateSingle.setObjectName("groupBox_generateSingle")
        self.pushButton_goEncode = QtWidgets.QPushButton(self.groupBox_generateSingle)
        self.pushButton_goEncode.setGeometry(QtCore.QRect(160, 100, 93, 28))
        self.pushButton_goEncode.setObjectName("pushButton_goEncode")
        self.lineEdit_inputTextEncode = QtWidgets.QLineEdit(self.groupBox_generateSingle)
        self.lineEdit_inputTextEncode.setGeometry(QtCore.QRect(20, 70, 391, 22))
        self.lineEdit_inputTextEncode.setObjectName("lineEdit_inputTextEncode")
        self.label_textToEncode = QtWidgets.QLabel(self.groupBox_generateSingle)
        self.label_textToEncode.setGeometry(QtCore.QRect(160, 40, 101, 16))
        self.label_textToEncode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_textToEncode.setObjectName("label_textToEncode")
        self.label_showGenerated = QtWidgets.QLabel(self.groupBox_generateSingle)
        self.label_showGenerated.setGeometry(QtCore.QRect(120, 140, 161, 151))
        self.label_showGenerated.setStyleSheet("border-radius:10")
        self.label_showGenerated.setText("")
        self.label_showGenerated.setPixmap(QtGui.QPixmap("E:/WHITE HAT/PHYTON/test6/MACHINE LEARNING/TARASERA/Tarascanner/andra_qrcode.png"))
        self.label_showGenerated.setScaledContents(True)
        self.label_showGenerated.setObjectName("label_showGenerated")
        self.label_checkGenerated1 = QtWidgets.QLabel(self.groupBox_generateSingle)
        self.label_checkGenerated1.setGeometry(QtCore.QRect(90, 300, 221, 31))
        self.label_checkGenerated1.setStyleSheet("background: white; border-radius: 10")
        self.label_checkGenerated1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_checkGenerated1.setObjectName("label_checkGenerated1")
        self.groupBox_generateMultiple = QtWidgets.QGroupBox(self.generatorTab)
        self.groupBox_generateMultiple.setGeometry(QtCore.QRect(450, 20, 591, 331))
        self.groupBox_generateMultiple.setObjectName("groupBox_generateMultiple")
        self.label_xlsxFile = QtWidgets.QLabel(self.groupBox_generateMultiple)
        self.label_xlsxFile.setGeometry(QtCore.QRect(20, 30, 551, 20))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        self.label_xlsxFile.setFont(font)
        self.label_xlsxFile.setStyleSheet("background: white; border-radius: 5")
        self.label_xlsxFile.setAlignment(QtCore.Qt.AlignCenter)
        self.label_xlsxFile.setObjectName("label_xlsxFile")
        self.label_csvFile = QtWidgets.QLabel(self.groupBox_generateMultiple)
        self.label_csvFile.setGeometry(QtCore.QRect(20, 120, 551, 20))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        self.label_csvFile.setFont(font)
        self.label_csvFile.setStyleSheet("background: white; border-radius: 5")
        self.label_csvFile.setAlignment(QtCore.Qt.AlignCenter)
        self.label_csvFile.setObjectName("label_csvFile")
        self.pushButton_generateByExcel = QtWidgets.QPushButton(self.groupBox_generateMultiple)
        self.pushButton_generateByExcel.setGeometry(QtCore.QRect(210, 60, 171, 28))
        self.pushButton_generateByExcel.setObjectName("pushButton_generateByExcel")
        self.pushButton_generateByCSV = QtWidgets.QPushButton(self.groupBox_generateMultiple)
        self.pushButton_generateByCSV.setGeometry(QtCore.QRect(210, 150, 171, 28))
        self.pushButton_generateByCSV.setObjectName("pushButton_generateByCSV")
        self.label_totalGeneratedRef = QtWidgets.QLabel(self.groupBox_generateMultiple)
        self.label_totalGeneratedRef.setGeometry(QtCore.QRect(200, 219, 111, 20))
        self.label_totalGeneratedRef.setAlignment(QtCore.Qt.AlignCenter)
        self.label_totalGeneratedRef.setObjectName("label_totalGeneratedRef")
        self.label_check2 = QtWidgets.QLabel(self.groupBox_generateMultiple)
        self.label_check2.setGeometry(QtCore.QRect(140, 250, 311, 31))
        self.label_check2.setStyleSheet("background: white; border-radius: 10")
        self.label_check2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_check2.setObjectName("label_check2")
        self.label_totalGeneratedValue = QtWidgets.QLabel(self.groupBox_generateMultiple)
        self.label_totalGeneratedValue.setGeometry(QtCore.QRect(320, 220, 55, 16))
        self.label_totalGeneratedValue.setObjectName("label_totalGeneratedValue")
        self.tabWidget.addTab(self.generatorTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_main.setTitle(_translate("MainWindow", "Main"))
        self.pushButton_startScanner.setText(_translate("MainWindow", "START SCANNER"))
        self.checkBox_connectDbase.setText(_translate("MainWindow", "Connect Database"))
        self.comboBox_camID.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_camID.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_camID.setItemText(2, _translate("MainWindow", "2"))
        self.label_camID.setText(_translate("MainWindow", "Camera ID"))
        self.label_dbMonitor.setText(_translate("MainWindow", "Database Monitor: localDatabase.csv"))
        self.groupBox_dbControl.setTitle(_translate("MainWindow", "Database Control"))
        self.label_columnRef.setText(_translate("MainWindow", "Column"))
        self.label_rowRef.setText(_translate("MainWindow", "Row"))
        self.pushButton_insert.setText(_translate("MainWindow", "Insert"))
        self.label_valueRef.setText(_translate("MainWindow", "Value"))
        self.pushButton_insertTime.setText(_translate("MainWindow", "Insert Time Stamp"))
        self.pushButton_reset.setWhatsThis(_translate("MainWindow", "Reset The Whole timestamp"))
        self.pushButton_reset.setText(_translate("MainWindow", "RESET"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scannerTab), _translate("MainWindow", "Scanner"))
        self.groupBox_generateSingle.setTitle(_translate("MainWindow", "Generate Single Code"))
        self.pushButton_goEncode.setText(_translate("MainWindow", "ENCODE"))
        self.label_textToEncode.setText(_translate("MainWindow", "Text to Encode"))
        self.label_checkGenerated1.setText(_translate("MainWindow", "Check at \'GeneratedCode\' Folder"))
        self.groupBox_generateMultiple.setTitle(_translate("MainWindow", "Generate Multiple Code"))
        self.label_xlsxFile.setText(_translate("MainWindow", "No .xlsx File Chosen"))
        self.label_csvFile.setText(_translate("MainWindow", "No .csv File Chosen"))
        self.pushButton_generateByExcel.setText(_translate("MainWindow", "Generate From Excel List"))
        self.pushButton_generateByCSV.setText(_translate("MainWindow", "Generate From CSV List"))
        self.label_totalGeneratedRef.setText(_translate("MainWindow", "Total Generated :"))
        self.label_check2.setText(_translate("MainWindow", "Check at the new folder in \'GeneratedCode\' Folder"))
        self.label_totalGeneratedValue.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generatorTab), _translate("MainWindow", "QR Generator"))


    def __injectFunction(self,*args):
        args = list(args)
        if len(args) == 1:
            func = args.pop(0); func()
        else:
            func = args.pop(0); func(*args)

    # Push Button Function Injector
    def startScanner(self):
        self.setStartScannerText()
        if self.scannerState:
            self.setCamID(self.getCamID())
            self.injected_runScanner()
        else:
            self.injected_stopScanner()

    def modify(self):
        df = pd.read_csv('localDatabase.csv')
        keys = [key for key in df.keys()]
        for i in len(df):
            datas = [df[key][i] for key in df.keys()]
        
    def insertTime(self, *args): 
        self.__injectFunction(*args)

    def encode(self, *args): 
        self.__injectFunction(*args)

    def generateByExcel(self, *args): 
        self.__injectFunction(*args)

    def generateByCSV(self, *args): 
        self.__injectFunction(*args)

    # Get CheckBox State
    def getCheckBoxConnectDatabase(self):
        return self.checkBox_connectDbase.checkState()

    # Get Camera ID
    def getCamID(self):
        return int(self.comboBox_camID.currentText())

    # Get column keys
    def getDbaseColumnKeys(self):
        return str(self.comboBox_dbaseKeys.currentText())

    # Set column keys
    def setDbaseColumnKeys(self):
        df = pd.read_csv('localDatabase.csv')
        keys = [key for key in df.keys()]
        for key in keys: self.comboBox_dbaseKeys.addItem(key)
        self.comboBox_dbaseKeys.SelectedIndex = self.FindStringExact('TimeStamp')

    # Get Row Keys
    def getDbaseRowKeys(self):
        return int(self.comboBox_dbaseRows.currentText())

    # Set Row Keys
    def setDbaseRowKeys(self):
        df = pd.read_csv('localDatabase.csv')
        for i in range(len(df)): self.comboBox_dbaseKeys.addItem(str(i))

    # Get Line Edit
    def getInputMod(self):
        return self.lineEdit_inputMod.text()

    def getInputEncode(self):
        return self.lineEdit_inputTextEncode.text()

    # Set Label
    def setStartScannerText(self):
        self.scannerState = True if not self.scannerState else False
        if self.scannerState:           
            self.pushButton_startScanner.setText("STOP SCANNER")
        else:
            self.pushButton_startScanner.setText("START SCANNER")

    def setExcelTitle(self,val):
        self.label_xlsxFile.setText(str(val))

    def setCSVTitle(self,val):
        self.label_csvFile.setText(str(val))

    def setTotal(self, val):
        self.label_totalGeneratedValue(str(val))

    # Set Barcode Picture
    def showBarcode(self, pic):
        self.label_showGenerated.setPixmap(QtGui.QPixmap(pic))
        self.label_showGenerated.setScaledContents(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
