from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys, res2


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        Form.setFixedSize(450, 550)  # Prevent resizing the window
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowTitleHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 370, 480))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0.0113636 rgba(139, 2, 189, 236), stop:0.479904 rgba(255, 0, 0, 255), stop:0.522685 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgba( 255, 255, 255, 210);\n"
"    boder-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0.0113636 rgba(155, 49, 194, 126), stop:0.479904 rgba(255, 0, 0, 255), stop:0.522685 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
" \n"
"    background-color: rgb(99, 5, 83);\n"
"}\n"
"QPushButton#pushButton_5:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  color: rgb(115,128,142, 255);\n"
"}\n"
"QPushButton#pushButton_2{\n"
"    background-color: rgb(0,0, 0, 0);\n"
"    color: rgb(85,98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"    color: rgb(155,168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  color: rgb(115,128,142, 255);\n"
"}\n"
"QPushButton#pushButton_3{\n"
"    background-color: rgb(0,0, 0, 0);\n"
"    color: rgb(85,98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
"    color: rgb(155,168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  color: rgb(115,128,142, 255);\n"
"}\n"
"QPushButton#pushButton_4{\n"
"    background-color: rgb(0,0, 0, 0);\n"
"    color: rgb(85,98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_4:hover{\n"
"    color: rgb(155,168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_4:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  color: rgb(115,128,142, 255);\n"
"}\n"
"QPushButton#pushButton_4{\n"
"    background-color: rgb(0,0, 0, 0);\n"
"    color: rgb(85,98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_4:hover{\n"
"    color: rgb(155,168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_5:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  color: rgb(115,128,142, 255);\n"
"}\n"
"QPushButton#pushButton_5{\n"
"    background-color: rgb(0,0, 0, 0);\n"
"    color: rgb(85,98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_5:hover{\n"
"    color: rgb(155,168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_5:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  color: rgb(115,128,142, 255);\n"
"}\n"
"QPushButton#pushButton_6{\n"
"    background-color: rgb(0,0, 0, 0);\n"
"    color: rgb(85,98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_6:hover{\n"
"    color: rgb(155,168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_6:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  color: rgb(115,128,142, 255);\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label.setStyleSheet("border-image: url(:/image/picture.png);\n"
"border-radius:20px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label_2.setStyleSheet("border-radius:20px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(124, 14, 65, 61), stop:0.479904 rgba(255, 0, 0, 255), stop:0.522685 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 280, 390))
        self.label_3.setStyleSheet("background-color:rgba( 0, 0, 0, 100);\n"
"border-radius:20px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(135, 95, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(80, 165, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setStyleSheet("background-color:rgba( 0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba( 105, 118, 132, 255);\n"
"color:rgba( 255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(80, 230, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color:rgba( 0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba( 105, 118, 132, 255);\n"
"color:rgba( 255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(88, 358, 201, 21))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 380, 160, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 30, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Wingdings 2")
        font.setPointSize(20)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setObjectName("pushButton_6")
        Form.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        Form.setMenuBar(self.menubar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MainWindow"))
        self.label_4.setText(_translate("Form", "Login"))
        self.username.setPlaceholderText(_translate("Form", "User Name"))
        self.password.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Log In"))
        self.label_5.setText(_translate("Form", "Forgot your Username or Password?"))
        self.pushButton_3.setText(_translate("Form", "E"))
        self.pushButton_2.setText(_translate("Form", "H"))
        self.pushButton_4.setText(_translate("Form", "D"))
        self.pushButton_5.setText(_translate("Form", "h"))
        self.pushButton_6.setText(_translate("Form", "Í"))

class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.drag_position = None

        # Connect signals
        self.pushButton.clicked.connect(self.handle_login)
        self.pushButton_6.clicked.connect(self.Quit)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton and self.drag_position:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_position = None
        event.accept()

    def handle_login(self):

        username = self.username.text()
        password = self.password.text()
        if username == "admin" and password == "1234567":
            QtWidgets.QMessageBox.information(self, "Login Success", "Welcome admin")
        elif username=="staff" and password =="1234567":
            QtWidgets.QMessageBox.information(self, "Login Success", "Welcome user")
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def Quit(self):
        QApplication.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())