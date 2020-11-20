# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 565)
        MainWindow.setBaseSize(QtCore.QSize(1010, 582))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../收藏夹/iCloud Photos/Downloads/2019/IMG_0574.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#StudentBox{background-color: rgb(255, 255, 255)}")
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.Table = QtWidgets.QTabWidget(self.widget)
        self.Table.setGeometry(QtCore.QRect(10, 10, 951, 531))
        self.Table.setStatusTip("")
        self.Table.setTabPosition(QtWidgets.QTabWidget.North)
        self.Table.setObjectName("Table")
        self.X_table = QtWidgets.QWidget()
        self.X_table.setObjectName("X_table")
        self.actionEdit_1 = QtWidgets.QPushButton(self.X_table)
        self.actionEdit_1.setGeometry(QtCore.QRect(681, 461, 111, 31))
        self.actionEdit_1.setObjectName("actionEdit_1")
        self.SearchFrame_1 = QtWidgets.QFrame(self.X_table)
        self.SearchFrame_1.setGeometry(QtCore.QRect(1, 21, 671, 31))
        self.SearchFrame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SearchFrame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SearchFrame_1.setObjectName("SearchFrame_1")
        self.SearchEdit_1 = QtWidgets.QLineEdit(self.SearchFrame_1)
        self.SearchEdit_1.setGeometry(QtCore.QRect(3, 0, 471, 31))
        self.SearchEdit_1.setObjectName("SearchEdit_1")
        self.SearchBox_1 = QtWidgets.QComboBox(self.SearchFrame_1)
        self.SearchBox_1.setGeometry(QtCore.QRect(470, 0, 81, 31))
        self.SearchBox_1.setBaseSize(QtCore.QSize(0, 0))
        self.SearchBox_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SearchBox_1.setEditable(False)
        self.SearchBox_1.setObjectName("SearchBox_1")
        self.SearchBox_1.addItem("")
        self.SearchBox_1.addItem("")
        self.SearchBox_1.addItem("")
        self.SearchBox_1.addItem("")
        self.SearchBox_1.addItem("")
        self.SearchBox_1.addItem("")
        self.SearchBox_1.addItem("")
        self.SearchButton_1 = QtWidgets.QPushButton(self.SearchFrame_1)
        self.SearchButton_1.setGeometry(QtCore.QRect(564, 0, 101, 31))
        self.SearchButton_1.setObjectName("SearchButton_1")
        self.groupBox_1 = QtWidgets.QGroupBox(self.X_table)
        self.groupBox_1.setGeometry(QtCore.QRect(701, 91, 221, 311))
        self.groupBox_1.setStyleSheet("#groupBox_1{\n"
"background : rgb(237, 255, 254);\n"
"}")
        self.groupBox_1.setFlat(False)
        self.groupBox_1.setCheckable(False)
        self.groupBox_1.setObjectName("groupBox_1")
        self.SIDlable = QtWidgets.QLabel(self.groupBox_1)
        self.SIDlable.setGeometry(QtCore.QRect(10, 40, 60, 15))
        self.SIDlable.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SIDlable.setObjectName("SIDlable")
        self.Snamelabel = QtWidgets.QLabel(self.groupBox_1)
        self.Snamelabel.setGeometry(QtCore.QRect(10, 70, 60, 15))
        self.Snamelabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Snamelabel.setObjectName("Snamelabel")
        self.Ssexlabel = QtWidgets.QLabel(self.groupBox_1)
        self.Ssexlabel.setGeometry(QtCore.QRect(10, 100, 60, 15))
        self.Ssexlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Ssexlabel.setObjectName("Ssexlabel")
        self.Lnolabel = QtWidgets.QLabel(self.groupBox_1)
        self.Lnolabel.setGeometry(QtCore.QRect(10, 130, 60, 15))
        self.Lnolabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Lnolabel.setObjectName("Lnolabel")
        self.Snolabel = QtWidgets.QLabel(self.groupBox_1)
        self.Snolabel.setGeometry(QtCore.QRect(10, 160, 60, 15))
        self.Snolabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Snolabel.setObjectName("Snolabel")
        self.Mnamelabel = QtWidgets.QLabel(self.groupBox_1)
        self.Mnamelabel.setGeometry(QtCore.QRect(10, 190, 60, 15))
        self.Mnamelabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Mnamelabel.setObjectName("Mnamelabel")
        self.SID = QtWidgets.QLabel(self.groupBox_1)
        self.SID.setGeometry(QtCore.QRect(80, 40, 131, 16))
        self.SID.setTextFormat(QtCore.Qt.AutoText)
        self.SID.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SID.setObjectName("SID")
        self.Sname = QtWidgets.QLabel(self.groupBox_1)
        self.Sname.setGeometry(QtCore.QRect(80, 70, 131, 16))
        self.Sname.setTextFormat(QtCore.Qt.AutoText)
        self.Sname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Sname.setObjectName("Sname")
        self.Ssex = QtWidgets.QLabel(self.groupBox_1)
        self.Ssex.setGeometry(QtCore.QRect(80, 100, 131, 16))
        self.Ssex.setTextFormat(QtCore.Qt.AutoText)
        self.Ssex.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Ssex.setObjectName("Ssex")
        self.Lno = QtWidgets.QLabel(self.groupBox_1)
        self.Lno.setGeometry(QtCore.QRect(80, 130, 131, 16))
        self.Lno.setTextFormat(QtCore.Qt.AutoText)
        self.Lno.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Lno.setObjectName("Lno")
        self.Sno = QtWidgets.QLabel(self.groupBox_1)
        self.Sno.setGeometry(QtCore.QRect(80, 160, 131, 16))
        self.Sno.setTextFormat(QtCore.Qt.AutoText)
        self.Sno.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Sno.setObjectName("Sno")
        self.MID = QtWidgets.QLabel(self.groupBox_1)
        self.MID.setGeometry(QtCore.QRect(80, 190, 131, 16))
        self.MID.setTextFormat(QtCore.Qt.AutoText)
        self.MID.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MID.setObjectName("MID")
        self.editButton_1 = QtWidgets.QPushButton(self.groupBox_1)
        self.editButton_1.setGeometry(QtCore.QRect(10, 260, 93, 28))
        self.editButton_1.setObjectName("editButton_1")
        self.DeleteButton_1 = QtWidgets.QPushButton(self.groupBox_1)
        self.DeleteButton_1.setGeometry(QtCore.QRect(120, 260, 93, 28))
        self.DeleteButton_1.setObjectName("DeleteButton_1")
        self.Mname = QtWidgets.QLabel(self.groupBox_1)
        self.Mname.setGeometry(QtCore.QRect(80, 215, 131, 16))
        self.Mname.setTextFormat(QtCore.Qt.AutoText)
        self.Mname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Mname.setObjectName("Mname")
        self.Mnamelabel_3 = QtWidgets.QLabel(self.groupBox_1)
        self.Mnamelabel_3.setGeometry(QtCore.QRect(10, 215, 60, 15))
        self.Mnamelabel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Mnamelabel_3.setObjectName("Mnamelabel_3")
        self.TableFrame_1 = QtWidgets.QFrame(self.X_table)
        self.TableFrame_1.setGeometry(QtCore.QRect(0, 70, 671, 431))
        self.TableFrame_1.setStyleSheet("")
        self.TableFrame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TableFrame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TableFrame_1.setObjectName("TableFrame_1")
        self.studentTable = QtWidgets.QTreeWidget(self.TableFrame_1)
        self.studentTable.setGeometry(QtCore.QRect(3, 0, 667, 420))
        self.studentTable.setStyleSheet("#studentTable\n"
"{\n"
"    background : rgb(237, 255, 254);\n"
"    border:2px solid rgb(172, 172, 172)\n"
"}")
        self.studentTable.setObjectName("studentTable")
        self.Table.addTab(self.X_table, "")
        self.S_Table = QtWidgets.QWidget()
        self.S_Table.setObjectName("S_Table")
        self.SearchFrame_2 = QtWidgets.QFrame(self.S_Table)
        self.SearchFrame_2.setGeometry(QtCore.QRect(1, 21, 671, 31))
        self.SearchFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SearchFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SearchFrame_2.setObjectName("SearchFrame_2")
        self.SearchEdit_2 = QtWidgets.QLineEdit(self.SearchFrame_2)
        self.SearchEdit_2.setGeometry(QtCore.QRect(3, 0, 471, 31))
        self.SearchEdit_2.setObjectName("SearchEdit_2")
        self.SearchBox_2 = QtWidgets.QComboBox(self.SearchFrame_2)
        self.SearchBox_2.setGeometry(QtCore.QRect(470, 0, 81, 31))
        self.SearchBox_2.setBaseSize(QtCore.QSize(0, 0))
        self.SearchBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SearchBox_2.setEditable(False)
        self.SearchBox_2.setObjectName("SearchBox_2")
        self.SearchBox_2.addItem("")
        self.SearchBox_2.addItem("")
        self.SearchBox_2.addItem("")
        self.SearchBox_2.addItem("")
        self.SearchBox_2.addItem("")
        self.SearchBox_2.addItem("")
        self.SearchButton_2 = QtWidgets.QPushButton(self.SearchFrame_2)
        self.SearchButton_2.setGeometry(QtCore.QRect(564, 0, 101, 31))
        self.SearchButton_2.setObjectName("SearchButton_2")
        self.actionEdit_2 = QtWidgets.QPushButton(self.S_Table)
        self.actionEdit_2.setGeometry(QtCore.QRect(681, 461, 111, 31))
        self.actionEdit_2.setObjectName("actionEdit_2")
        self.TableFrame_2 = QtWidgets.QFrame(self.S_Table)
        self.TableFrame_2.setGeometry(QtCore.QRect(0, 70, 671, 431))
        self.TableFrame_2.setStyleSheet("")
        self.TableFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TableFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TableFrame_2.setObjectName("TableFrame_2")
        self.ShusheTable = QtWidgets.QTreeWidget(self.TableFrame_2)
        self.ShusheTable.setGeometry(QtCore.QRect(3, 0, 661, 421))
        self.ShusheTable.setAcceptDrops(False)
        self.ShusheTable.setStyleSheet("#ShusheTable\n"
"{\n"
"    background : rgb(237, 255, 254);\n"
"    border:2px solid rgb(172, 172, 172)\n"
"}")
        self.ShusheTable.setObjectName("ShusheTable")
        self.groupBox_2 = QtWidgets.QGroupBox(self.S_Table)
        self.groupBox_2.setGeometry(QtCore.QRect(701, 91, 221, 311))
        self.groupBox_2.setStyleSheet("#groupBox_2{\n"
"background : rgb(237, 255, 254);\n"
"}")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.Lnolabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.Lnolabel_2.setGeometry(QtCore.QRect(10, 40, 80, 15))
        self.Lnolabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Lnolabel_2.setObjectName("Lnolabel_2")
        self.Snolabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.Snolabel_2.setGeometry(QtCore.QRect(10, 70, 80, 15))
        self.Snolabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Snolabel_2.setObjectName("Snolabel_2")
        self.K_nlabel = QtWidgets.QLabel(self.groupBox_2)
        self.K_nlabel.setGeometry(QtCore.QRect(10, 100, 80, 16))
        self.K_nlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.K_nlabel.setObjectName("K_nlabel")
        self.L_nlabel = QtWidgets.QLabel(self.groupBox_2)
        self.L_nlabel.setGeometry(QtCore.QRect(10, 130, 80, 16))
        self.L_nlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.L_nlabel.setObjectName("L_nlabel")
        self.C_nlabel = QtWidgets.QLabel(self.groupBox_2)
        self.C_nlabel.setGeometry(QtCore.QRect(10, 160, 80, 15))
        self.C_nlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.C_nlabel.setObjectName("C_nlabel")
        self.Locationlabel = QtWidgets.QLabel(self.groupBox_2)
        self.Locationlabel.setGeometry(QtCore.QRect(10, 190, 80, 15))
        self.Locationlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Locationlabel.setObjectName("Locationlabel")
        self.Lno_2 = QtWidgets.QLabel(self.groupBox_2)
        self.Lno_2.setGeometry(QtCore.QRect(100, 40, 100, 16))
        self.Lno_2.setTextFormat(QtCore.Qt.AutoText)
        self.Lno_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Lno_2.setObjectName("Lno_2")
        self.Sno_2 = QtWidgets.QLabel(self.groupBox_2)
        self.Sno_2.setGeometry(QtCore.QRect(100, 70, 100, 16))
        self.Sno_2.setTextFormat(QtCore.Qt.AutoText)
        self.Sno_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Sno_2.setObjectName("Sno_2")
        self.K_n = QtWidgets.QLabel(self.groupBox_2)
        self.K_n.setGeometry(QtCore.QRect(100, 100, 100, 16))
        self.K_n.setTextFormat(QtCore.Qt.AutoText)
        self.K_n.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.K_n.setObjectName("K_n")
        self.L_n = QtWidgets.QLabel(self.groupBox_2)
        self.L_n.setGeometry(QtCore.QRect(100, 130, 100, 16))
        self.L_n.setTextFormat(QtCore.Qt.AutoText)
        self.L_n.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.L_n.setObjectName("L_n")
        self.C_n = QtWidgets.QLabel(self.groupBox_2)
        self.C_n.setGeometry(QtCore.QRect(100, 160, 100, 16))
        self.C_n.setTextFormat(QtCore.Qt.AutoText)
        self.C_n.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.C_n.setObjectName("C_n")
        self.Location = QtWidgets.QLabel(self.groupBox_2)
        self.Location.setGeometry(QtCore.QRect(100, 190, 100, 16))
        self.Location.setTextFormat(QtCore.Qt.AutoText)
        self.Location.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Location.setObjectName("Location")
        self.editButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.editButton_2.setGeometry(QtCore.QRect(10, 260, 93, 28))
        self.editButton_2.setObjectName("editButton_2")
        self.DeleteButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.DeleteButton_2.setGeometry(QtCore.QRect(120, 260, 93, 28))
        self.DeleteButton_2.setObjectName("DeleteButton_2")
        self.Table.addTab(self.S_Table, "")
        self.G_Table = QtWidgets.QWidget()
        self.G_Table.setObjectName("G_Table")
        self.actionEdit_3 = QtWidgets.QPushButton(self.G_Table)
        self.actionEdit_3.setGeometry(QtCore.QRect(680, 460, 111, 31))
        self.actionEdit_3.setObjectName("actionEdit_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.G_Table)
        self.groupBox_3.setGeometry(QtCore.QRect(700, 90, 221, 311))
        self.groupBox_3.setStyleSheet("#groupBox_3{\n"
"background : rgb(237, 255, 254);\n"
"}")
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.Mnolabel = QtWidgets.QLabel(self.groupBox_3)
        self.Mnolabel.setGeometry(QtCore.QRect(10, 40, 80, 15))
        self.Mnolabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Mnolabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Mnolabel.setObjectName("Mnolabel")
        self.Mnamelabel_2 = QtWidgets.QLabel(self.groupBox_3)
        self.Mnamelabel_2.setGeometry(QtCore.QRect(10, 70, 80, 15))
        self.Mnamelabel_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Mnamelabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Mnamelabel_2.setObjectName("Mnamelabel_2")
        self.Msexlabel = QtWidgets.QLabel(self.groupBox_3)
        self.Msexlabel.setGeometry(QtCore.QRect(10, 100, 80, 16))
        self.Msexlabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Msexlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Msexlabel.setObjectName("Msexlabel")
        self.Magelabel = QtWidgets.QLabel(self.groupBox_3)
        self.Magelabel.setGeometry(QtCore.QRect(10, 130, 80, 15))
        self.Magelabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Magelabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Magelabel.setObjectName("Magelabel")
        self.Mphonelabel = QtWidgets.QLabel(self.groupBox_3)
        self.Mphonelabel.setGeometry(QtCore.QRect(10, 160, 80, 15))
        self.Mphonelabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Mphonelabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Mphonelabel.setObjectName("Mphonelabel")
        self.Mno = QtWidgets.QLabel(self.groupBox_3)
        self.Mno.setGeometry(QtCore.QRect(100, 40, 100, 16))
        self.Mno.setTextFormat(QtCore.Qt.AutoText)
        self.Mno.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Mno.setObjectName("Mno")
        self.Mname_2 = QtWidgets.QLabel(self.groupBox_3)
        self.Mname_2.setGeometry(QtCore.QRect(100, 70, 100, 16))
        self.Mname_2.setTextFormat(QtCore.Qt.AutoText)
        self.Mname_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Mname_2.setObjectName("Mname_2")
        self.MSex = QtWidgets.QLabel(self.groupBox_3)
        self.MSex.setGeometry(QtCore.QRect(100, 100, 100, 16))
        self.MSex.setTextFormat(QtCore.Qt.AutoText)
        self.MSex.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MSex.setObjectName("MSex")
        self.Mage = QtWidgets.QLabel(self.groupBox_3)
        self.Mage.setGeometry(QtCore.QRect(100, 130, 100, 16))
        self.Mage.setTextFormat(QtCore.Qt.AutoText)
        self.Mage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Mage.setObjectName("Mage")
        self.MPhone = QtWidgets.QLabel(self.groupBox_3)
        self.MPhone.setGeometry(QtCore.QRect(100, 160, 100, 16))
        self.MPhone.setTextFormat(QtCore.Qt.AutoText)
        self.MPhone.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MPhone.setObjectName("MPhone")
        self.editButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.editButton_3.setGeometry(QtCore.QRect(10, 260, 93, 28))
        self.editButton_3.setObjectName("editButton_3")
        self.DeleteButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.DeleteButton_3.setGeometry(QtCore.QRect(120, 260, 93, 28))
        self.DeleteButton_3.setObjectName("DeleteButton_3")
        self.TableFrame_3 = QtWidgets.QFrame(self.G_Table)
        self.TableFrame_3.setGeometry(QtCore.QRect(-1, 69, 671, 431))
        self.TableFrame_3.setStyleSheet("")
        self.TableFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TableFrame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TableFrame_3.setObjectName("TableFrame_3")
        self.Mtable = QtWidgets.QTreeWidget(self.TableFrame_3)
        self.Mtable.setGeometry(QtCore.QRect(3, 0, 661, 421))
        self.Mtable.setAcceptDrops(False)
        self.Mtable.setStyleSheet("#Mtable\n"
"{\n"
"    background : rgb(237, 255, 254);\n"
"    border:2px solid rgb(172, 172, 172);\n"
"}")
        self.Mtable.setObjectName("Mtable")
        self.SearchFrame_3 = QtWidgets.QFrame(self.G_Table)
        self.SearchFrame_3.setGeometry(QtCore.QRect(0, 20, 671, 31))
        self.SearchFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SearchFrame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SearchFrame_3.setObjectName("SearchFrame_3")
        self.SearchEdit_3 = QtWidgets.QLineEdit(self.SearchFrame_3)
        self.SearchEdit_3.setGeometry(QtCore.QRect(3, 0, 471, 31))
        self.SearchEdit_3.setObjectName("SearchEdit_3")
        self.SearchBox_3 = QtWidgets.QComboBox(self.SearchFrame_3)
        self.SearchBox_3.setGeometry(QtCore.QRect(470, 0, 81, 31))
        self.SearchBox_3.setBaseSize(QtCore.QSize(0, 0))
        self.SearchBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SearchBox_3.setEditable(False)
        self.SearchBox_3.setObjectName("SearchBox_3")
        self.SearchBox_3.addItem("")
        self.SearchBox_3.addItem("")
        self.SearchBox_3.addItem("")
        self.SearchBox_3.addItem("")
        self.SearchBox_3.addItem("")
        self.SearchButton_3 = QtWidgets.QPushButton(self.SearchFrame_3)
        self.SearchButton_3.setGeometry(QtCore.QRect(564, 0, 101, 31))
        self.SearchButton_3.setObjectName("SearchButton_3")
        self.Table.addTab(self.G_Table, "")
        MainWindow.setCentralWidget(self.widget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.Student = QtWidgets.QAction(MainWindow)
        self.Student.setObjectName("Student")

        self.retranslateUi(MainWindow)
        self.Table.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Table, self.SearchEdit_1)
        MainWindow.setTabOrder(self.SearchEdit_1, self.SearchBox_1)
        MainWindow.setTabOrder(self.SearchBox_1, self.SearchButton_1)
        MainWindow.setTabOrder(self.SearchButton_1, self.actionEdit_1)
        MainWindow.setTabOrder(self.actionEdit_1, self.editButton_1)
        MainWindow.setTabOrder(self.editButton_1, self.DeleteButton_1)
        MainWindow.setTabOrder(self.DeleteButton_1, self.SearchEdit_2)
        MainWindow.setTabOrder(self.SearchEdit_2, self.SearchBox_2)
        MainWindow.setTabOrder(self.SearchBox_2, self.SearchButton_2)
        MainWindow.setTabOrder(self.SearchButton_2, self.actionEdit_2)
        MainWindow.setTabOrder(self.actionEdit_2, self.ShusheTable)
        MainWindow.setTabOrder(self.ShusheTable, self.editButton_2)
        MainWindow.setTabOrder(self.editButton_2, self.DeleteButton_2)
        MainWindow.setTabOrder(self.DeleteButton_2, self.actionEdit_3)
        MainWindow.setTabOrder(self.actionEdit_3, self.editButton_3)
        MainWindow.setTabOrder(self.editButton_3, self.DeleteButton_3)
        MainWindow.setTabOrder(self.DeleteButton_3, self.Mtable)
        MainWindow.setTabOrder(self.Mtable, self.SearchEdit_3)
        MainWindow.setTabOrder(self.SearchEdit_3, self.SearchBox_3)
        MainWindow.setTabOrder(self.SearchBox_3, self.SearchButton_3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生宿舍管理"))
        self.X_table.setStatusTip(_translate("MainWindow", "学生管理"))
        self.actionEdit_1.setStatusTip(_translate("MainWindow", "添加学生信息"))
        self.actionEdit_1.setText(_translate("MainWindow", "添加学生..."))
        self.SearchEdit_1.setStatusTip(_translate("MainWindow", "快速检索信息"))
        self.SearchBox_1.setItemText(0, _translate("MainWindow", "学号"))
        self.SearchBox_1.setItemText(1, _translate("MainWindow", "姓名"))
        self.SearchBox_1.setItemText(2, _translate("MainWindow", "性别"))
        self.SearchBox_1.setItemText(3, _translate("MainWindow", "楼号"))
        self.SearchBox_1.setItemText(4, _translate("MainWindow", "宿舍号"))
        self.SearchBox_1.setItemText(5, _translate("MainWindow", "宿管"))
        self.SearchBox_1.setItemText(6, _translate("MainWindow", "联系方式"))
        self.SearchButton_1.setStatusTip(_translate("MainWindow", "对多个属性进行检索"))
        self.SearchButton_1.setText(_translate("MainWindow", "高级搜索..."))
        self.groupBox_1.setTitle(_translate("MainWindow", "学生信息"))
        self.SIDlable.setText(_translate("MainWindow", "学号"))
        self.Snamelabel.setText(_translate("MainWindow", "姓名"))
        self.Ssexlabel.setText(_translate("MainWindow", "性别"))
        self.Lnolabel.setText(_translate("MainWindow", "楼号"))
        self.Snolabel.setText(_translate("MainWindow", "宿舍号"))
        self.Mnamelabel.setText(_translate("MainWindow", "宿管ID"))
        self.SID.setText(_translate("MainWindow", "学号"))
        self.Sname.setText(_translate("MainWindow", "姓名"))
        self.Ssex.setText(_translate("MainWindow", "性别"))
        self.Lno.setText(_translate("MainWindow", "楼号"))
        self.Sno.setText(_translate("MainWindow", "宿舍号"))
        self.MID.setText(_translate("MainWindow", "宿管ID"))
        self.editButton_1.setStatusTip(_translate("MainWindow", "修改当前学生信息"))
        self.editButton_1.setText(_translate("MainWindow", "修改..."))
        self.DeleteButton_1.setStatusTip(_translate("MainWindow", "一旦删除无法恢复"))
        self.DeleteButton_1.setText(_translate("MainWindow", "删除"))
        self.Mname.setText(_translate("MainWindow", "宿管"))
        self.Mnamelabel_3.setText(_translate("MainWindow", "宿管"))
        self.studentTable.setStatusTip(_translate("MainWindow", "双击修改"))
        self.studentTable.headerItem().setText(0, _translate("MainWindow", "学号"))
        self.studentTable.headerItem().setText(1, _translate("MainWindow", "姓名"))
        self.studentTable.headerItem().setText(2, _translate("MainWindow", "性别"))
        self.studentTable.headerItem().setText(3, _translate("MainWindow", "楼号"))
        self.studentTable.headerItem().setText(4, _translate("MainWindow", "宿舍号"))
        self.studentTable.headerItem().setText(5, _translate("MainWindow", "宿管ID"))
        self.studentTable.headerItem().setText(6, _translate("MainWindow", "宿管"))
        self.Table.setTabText(self.Table.indexOf(self.X_table), _translate("MainWindow", "学生管理"))
        self.S_Table.setStatusTip(_translate("MainWindow", "宿舍管理"))
        self.SearchEdit_2.setStatusTip(_translate("MainWindow", "快速检索信息"))
        self.SearchBox_2.setItemText(0, _translate("MainWindow", "楼号"))
        self.SearchBox_2.setItemText(1, _translate("MainWindow", "宿舍号"))
        self.SearchBox_2.setItemText(2, _translate("MainWindow", "可容纳数"))
        self.SearchBox_2.setItemText(3, _translate("MainWindow", "入住人数"))
        self.SearchBox_2.setItemText(4, _translate("MainWindow", "剩余空位"))
        self.SearchBox_2.setItemText(5, _translate("MainWindow", "位置"))
        self.SearchButton_2.setStatusTip(_translate("MainWindow", "对多个属性进行检索"))
        self.SearchButton_2.setText(_translate("MainWindow", "高级搜索..."))
        self.actionEdit_2.setStatusTip(_translate("MainWindow", "添加宿舍信息"))
        self.actionEdit_2.setText(_translate("MainWindow", "添加宿舍..."))
        self.ShusheTable.setStatusTip(_translate("MainWindow", "双击修改信息"))
        self.ShusheTable.headerItem().setText(0, _translate("MainWindow", "楼号"))
        self.ShusheTable.headerItem().setText(1, _translate("MainWindow", "宿舍号"))
        self.ShusheTable.headerItem().setText(2, _translate("MainWindow", "可容纳人数"))
        self.ShusheTable.headerItem().setText(3, _translate("MainWindow", "入住人数"))
        self.ShusheTable.headerItem().setText(4, _translate("MainWindow", "剩余空位"))
        self.ShusheTable.headerItem().setText(5, _translate("MainWindow", "位置"))
        self.groupBox_2.setTitle(_translate("MainWindow", "宿舍信息"))
        self.Lnolabel_2.setText(_translate("MainWindow", "楼号"))
        self.Snolabel_2.setText(_translate("MainWindow", "宿舍号"))
        self.K_nlabel.setText(_translate("MainWindow", "可容纳人数"))
        self.L_nlabel.setText(_translate("MainWindow", "入住人数"))
        self.C_nlabel.setText(_translate("MainWindow", "剩余空位"))
        self.Locationlabel.setText(_translate("MainWindow", "位置"))
        self.Lno_2.setText(_translate("MainWindow", "楼号"))
        self.Sno_2.setText(_translate("MainWindow", "宿舍号"))
        self.K_n.setText(_translate("MainWindow", "可容纳人数"))
        self.L_n.setText(_translate("MainWindow", "入住人数"))
        self.C_n.setText(_translate("MainWindow", "剩余空位"))
        self.Location.setText(_translate("MainWindow", "位置"))
        self.editButton_2.setStatusTip(_translate("MainWindow", "修改当前宿舍信息"))
        self.editButton_2.setText(_translate("MainWindow", "修改..."))
        self.DeleteButton_2.setStatusTip(_translate("MainWindow", "一旦删除无法恢复"))
        self.DeleteButton_2.setText(_translate("MainWindow", "删除"))
        self.Table.setTabText(self.Table.indexOf(self.S_Table), _translate("MainWindow", "宿舍管理"))
        self.actionEdit_3.setStatusTip(_translate("MainWindow", "添加宿管信息"))
        self.actionEdit_3.setText(_translate("MainWindow", "添加宿管..."))
        self.groupBox_3.setTitle(_translate("MainWindow", "宿管信息"))
        self.Mnolabel.setText(_translate("MainWindow", "工号"))
        self.Mnamelabel_2.setText(_translate("MainWindow", "姓名"))
        self.Msexlabel.setText(_translate("MainWindow", "性别"))
        self.Magelabel.setText(_translate("MainWindow", "年龄"))
        self.Mphonelabel.setText(_translate("MainWindow", "联系方式"))
        self.Mno.setText(_translate("MainWindow", "工号"))
        self.Mname_2.setText(_translate("MainWindow", "姓名"))
        self.MSex.setText(_translate("MainWindow", "性别"))
        self.Mage.setText(_translate("MainWindow", "年龄"))
        self.MPhone.setText(_translate("MainWindow", "联系方式"))
        self.editButton_3.setStatusTip(_translate("MainWindow", "修改当前宿管信息"))
        self.editButton_3.setText(_translate("MainWindow", "修改..."))
        self.DeleteButton_3.setStatusTip(_translate("MainWindow", "一旦删除无法恢复"))
        self.DeleteButton_3.setText(_translate("MainWindow", "删除"))
        self.Mtable.setStatusTip(_translate("MainWindow", "双击修改信息"))
        self.Mtable.headerItem().setText(0, _translate("MainWindow", "工号"))
        self.Mtable.headerItem().setText(1, _translate("MainWindow", "新建列"))
        self.Mtable.headerItem().setText(2, _translate("MainWindow", "姓名"))
        self.Mtable.headerItem().setText(3, _translate("MainWindow", "性别"))
        self.Mtable.headerItem().setText(4, _translate("MainWindow", "联系方式"))
        self.SearchEdit_3.setStatusTip(_translate("MainWindow", "快速检索信息"))
        self.SearchBox_3.setItemText(0, _translate("MainWindow", "工号"))
        self.SearchBox_3.setItemText(1, _translate("MainWindow", "姓名"))
        self.SearchBox_3.setItemText(2, _translate("MainWindow", "性别"))
        self.SearchBox_3.setItemText(3, _translate("MainWindow", "年龄"))
        self.SearchBox_3.setItemText(4, _translate("MainWindow", "联系方式"))
        self.SearchButton_3.setStatusTip(_translate("MainWindow", "对多个属性进行检索"))
        self.SearchButton_3.setText(_translate("MainWindow", "高级搜索..."))
        self.Table.setTabText(self.Table.indexOf(self.G_Table), _translate("MainWindow", "工作人员管理"))
        self.Student.setText(_translate("MainWindow", "增加学生"))
        self.Student.setStatusTip(_translate("MainWindow", "增加学生"))