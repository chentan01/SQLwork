# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_Sbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sbox(object):
    def setupUi(self, Sbox):
        Sbox.setObjectName("Sbox")
        Sbox.resize(262, 336)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../收藏夹/iCloud Photos/Downloads/2019/IMG_0574.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Sbox.setWindowIcon(icon)
        self.msg = QtWidgets.QLabel(Sbox)
        self.msg.setGeometry(QtCore.QRect(35, 7, 201, 16))
        self.msg.setObjectName("msg")
        self.label_3 = QtWidgets.QLabel(Sbox)
        self.label_3.setGeometry(QtCore.QRect(20, 126, 75, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.C_nEdit = QtWidgets.QLineEdit(Sbox)
        self.C_nEdit.setGeometry(QtCore.QRect(105, 202, 131, 21))
        self.C_nEdit.setClearButtonEnabled(True)
        self.C_nEdit.setObjectName("C_nEdit")
        self.okButton = QtWidgets.QPushButton(Sbox)
        self.okButton.setGeometry(QtCore.QRect(75, 287, 71, 28))
        self.okButton.setObjectName("okButton")
        self.LocationEdit = QtWidgets.QLineEdit(Sbox)
        self.LocationEdit.setGeometry(QtCore.QRect(105, 240, 131, 21))
        self.LocationEdit.setClearButtonEnabled(True)
        self.LocationEdit.setObjectName("LocationEdit")
        self.label_5 = QtWidgets.QLabel(Sbox)
        self.label_5.setGeometry(QtCore.QRect(20, 202, 71, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.Lnodit = QtWidgets.QLineEdit(Sbox)
        self.Lnodit.setGeometry(QtCore.QRect(105, 50, 131, 21))
        self.Lnodit.setReadOnly(False)
        self.Lnodit.setClearButtonEnabled(True)
        self.Lnodit.setObjectName("Lnodit")
        self.L_nEdit = QtWidgets.QLineEdit(Sbox)
        self.L_nEdit.setGeometry(QtCore.QRect(105, 164, 131, 21))
        self.L_nEdit.setClearButtonEnabled(True)
        self.L_nEdit.setObjectName("L_nEdit")
        self.K_nEdit = QtWidgets.QLineEdit(Sbox)
        self.K_nEdit.setGeometry(QtCore.QRect(105, 126, 131, 21))
        self.K_nEdit.setClearButtonEnabled(True)
        self.K_nEdit.setObjectName("K_nEdit")
        self.cancelButton = QtWidgets.QPushButton(Sbox)
        self.cancelButton.setGeometry(QtCore.QRect(165, 287, 71, 28))
        self.cancelButton.setObjectName("cancelButton")
        self.label_4 = QtWidgets.QLabel(Sbox)
        self.label_4.setGeometry(QtCore.QRect(20, 164, 71, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.SnoEdit = QtWidgets.QLineEdit(Sbox)
        self.SnoEdit.setGeometry(QtCore.QRect(105, 88, 131, 21))
        self.SnoEdit.setClearButtonEnabled(True)
        self.SnoEdit.setObjectName("SnoEdit")
        self.label_2 = QtWidgets.QLabel(Sbox)
        self.label_2.setGeometry(QtCore.QRect(20, 88, 71, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Sbox)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 71, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(Sbox)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Sbox)
        QtCore.QMetaObject.connectSlotsByName(Sbox)

    def retranslateUi(self, Sbox):
        _translate = QtCore.QCoreApplication.translate
        Sbox.setWindowTitle(_translate("Sbox", "宿舍信息盒"))
        self.msg.setText(_translate("Sbox", "提示信息"))
        self.label_3.setText(_translate("Sbox", "可容纳人数"))
        self.okButton.setText(_translate("Sbox", "确定"))
        self.label_5.setText(_translate("Sbox", "剩余空位"))
        self.cancelButton.setText(_translate("Sbox", "取消"))
        self.label_4.setText(_translate("Sbox", "入住人数"))
        self.label_2.setText(_translate("Sbox", "宿舍号"))
        self.label_6.setText(_translate("Sbox", "位置"))
        self.label.setText(_translate("Sbox", "楼号"))
