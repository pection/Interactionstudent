# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testbutton.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, MainWindow):
        f = open("vote.txt",'w')
        f.close()
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(200,300)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bg = QtGui.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 200, 300))
        self.bg.setText(_fromUtf8(""))
        self.bg.setPixmap(QtGui.QPixmap(_fromUtf8("bg4")))
        self.bg.setObjectName(_fromUtf8("bg"))
        self.fra241 = QtGui.QLabel(self.centralwidget)
        self.fra241.setGeometry(QtCore.QRect(100, 40,400, 400))
        self.fra241.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.fra241.setText(_fromUtf8(""))
        self.fra241.setPixmap(QtGui.QPixmap(_fromUtf8("fra241.png")))
        self.fra241.setObjectName(_fromUtf8("fra241"))
        self.green = QtGui.QLabel(self.centralwidget)
        self.green.setGeometry(QtCore.QRect(0, 80, 200, 50))
        self.green.setText(_fromUtf8(""))
        self.green.setPixmap(QtGui.QPixmap(_fromUtf8("und_shift.png")))
        self.green.setObjectName(_fromUtf8("green"))
        self.red = QtGui.QLabel(self.centralwidget)
        self.red.setGeometry(QtCore.QRect(0, 130, 200, 50))
        self.red.setText(_fromUtf8(""))
        self.red.setPixmap(QtGui.QPixmap(_fromUtf8("con_shift.png")))
        self.red.setObjectName(_fromUtf8("red"))
        self.orange = QtGui.QLabel(self.centralwidget)
        self.orange.setGeometry(QtCore.QRect(0,180, 200, 50))
        self.orange.setText(_fromUtf8(""))
        self.orange.setPixmap(QtGui.QPixmap(_fromUtf8("ques_shift.png")))
        self.orange.setObjectName(_fromUtf8("orange"))
        self.blue = QtGui.QLabel(self.centralwidget)
        self.blue.setGeometry(QtCore.QRect(0, 230, 200,50))
        self.blue.setText(_fromUtf8(""))
        self.blue.setPixmap(QtGui.QPixmap(_fromUtf8("ask_tab.png")))
        self.blue.setObjectName(_fromUtf8("blue"))
        self.kaojai = QtGui.QPushButton(self.centralwidget)
        self.kaojai.setGeometry(QtCore.QRect(0, 80, 50, 50))
        self.kaojai.setStyleSheet(_fromUtf8("#kaojai {\n"
"background-color: transparent;\n"
"border-image: url(button_understand_B100x100.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#kaojai:pressed\n"
"{\n"
"border-image: url(button_understand_A100x100.png);\n"
"}"))
        self.kaojai.setText(_fromUtf8(""))
        self.kaojai.setCheckable(False)
        self.kaojai.setAutoDefault(False)
        self.kaojai.setObjectName(_fromUtf8("kaojai"))
        self.maikaojai = QtGui.QPushButton(self.centralwidget)
        self.maikaojai.setGeometry(QtCore.QRect(0, 130, 50, 50))
        self.maikaojai.setStyleSheet(_fromUtf8("#maikaojai {\n"
"background-color: transparent;\n"
"border-image: url(button_confuse_B100x100.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#maikaojai:pressed\n"
"{\n"
"border-image: url(button_confuse_A100x100.png);\n"
"}"))
        self.maikaojai.setText(_fromUtf8(""))
        self.maikaojai.setObjectName(_fromUtf8("maikaojai"))
        self.vote = QtGui.QPushButton(self.centralwidget)
        self.vote.setGeometry(QtCore.QRect(0, 180, 50, 50))
        self.vote.setStyleSheet(_fromUtf8("#vote {\n"
"background-color: transparent;\n"
"border-image: url(button_vote_B100x100.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#vote:pressed\n"
"{\n"
"border-image: url(button_vote_A100x100.png);\n"
"}"))
        self.vote.setText(_fromUtf8(""))
        self.vote.setObjectName(_fromUtf8("vote"))
        self.question = QtGui.QPushButton(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(0, 230, 50, 50))
        self.question.setStyleSheet(_fromUtf8("#question {\n"
"background-color: transparent;\n"
"border-image: url(button_question_B100x100.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#question:pressed\n"
"{\n"
"border-image: url(button_question_A100x100.png);\n"
"}"))
        self.question.setText(_fromUtf8(""))
        self.question.setObjectName(_fromUtf8("question"))
        self.fra241_2 = QtGui.QLabel(self.centralwidget)
        self.fra241_2.setGeometry(QtCore.QRect(350, 760, 51, 71))
        self.fra241_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.fra241_2.setText(_fromUtf8(""))
        self.fra241_2.setPixmap(QtGui.QPixmap(_fromUtf8("backbutton.png")))
        self.fra241_2.setObjectName(_fromUtf8("fra241_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

