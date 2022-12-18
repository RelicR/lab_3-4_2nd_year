'''
Лабораторная работа №3, Вариант 1
Шифрование по алгоритму Гронсфельда, ключ – слово (до 10 символов).
'''
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys
from crypt import *


class Reg_Wind(QMainWindow):
    def __init__(self):
        super(Reg_Wind, self).__init__()
        loadUi("login_window.ui", self)
        self.plainTextEdit.setReadOnly(True)
        self.passI.setEchoMode(QtWidgets.QLineEdit.Password)
        self.action()
        #QtWidgets.QLineEdit.displayText()
    def action(self):
        self.loginB.clicked.connect(lambda: self.login())
        self.regB.clicked.connect(lambda: self.register())
    def register(self):
        self.passI.setEchoMode(QtWidgets.QLineEdit.Normal)
        file = open("logins.txt", "r+", encoding='UTF-8')
        users = [x.replace('login: ', '').replace('password: ', '').split('\n') for x in file.read().split('\n\n')]
        #print(users)
        logs = [[decrypt(z.split(' key: ')[0], z.split(' key: ')[1]) for z in x] for x in users]
        #print(logs[0][0])
        #pas =
        if self.loginI.text() == "" or self.passI.text() == "":
            self.plainTextEdit.setPlainText("ГЛАВНАЯ СТРАНИЦА\nНе задан логин или пароль!")
        elif 1 in [1 for x in logs if self.loginI.text() == x[0]]:
            self.plainTextEdit.setPlainText("ГЛАВНАЯ СТРАНИЦА\nПользователь с данным именем уже существует!")
        else:
            file.close()
            file = open("logins.txt", "a+", encoding='UTF-8')
            file.write(f"\n\nlogin: {encrypt(self.loginI.text())}\npassword: {encrypt(self.passI.text())}")
            #widget.addWidget(pers_acc)
            widget.setCurrentWidget(pers_acc)
    def login(self):
        file = open("logins.txt", "r+", encoding='UTF-8')
        users = [x.replace('login: ', '').replace('password: ', '').split('\n') for x in file.read().split('\n\n')]
        #print(users)
        logs = [[decrypt(z.split(' key: ')[0], z.split(' key: ')[1]) for z in x] for x in users]
        if self.loginI.text() == "" or self.passI.text() == "":
            self.plainTextEdit.setPlainText("ГЛАВНАЯ СТРАНИЦА\nНе задан логин или пароль!")
        elif 1 in [1 for x in logs if self.loginI.text() == x[0] and self.passI.text() == x[1]]:
            file.close()
            widget.setCurrentWidget(pers_acc)


class Pers_Acc(QDialog):
    def __init__(self):
        super(Pers_Acc, self).__init__()
        loadUi("lk_window.ui", self)
        self.plainTextEdit.setReadOnly(True)
        self.action()
    def action(self):
        self.CryptButton.clicked.connect(lambda: self.enc())
        self.DecryptButton.clicked.connect(lambda: self.dec())
        self.ExitButton.clicked.connect(lambda: widget.setCurrentWidget(exit_w))
    def enc(self):
        #if (self.CryptButton.clicked):
        #    print(1)
        with open("encrypted.txt", "w+", encoding='UTF-8') as res:
            if self.CryptInput.toPlainText():
                res.write(encrypt(self.CryptInput.toPlainText()))
                self.plainTextEdit.setPlainText("""	            ЛИЧНЫЙ КАБИНЕТ\n
                Удачно! Результат выведен в файл encrypted.txt""")
            else:
                self.plainTextEdit.setPlainText("""	            ЛИЧНЫЙ КАБИНЕТ\n
                Текстовое поле пусто!""")
    def dec(self):
        with open("result.txt", "w+", encoding='UTF-8') as res:
            if len([u for u in self.KeyI.text() if u.isdigit()]) != sum([1 for x in self.CryptInput.toPlainText() if x.isalpha()]) or sum([1 for x in self.KeyI.text() if x.isalpha()]) != 0:
                self.plainTextEdit.setPlainText("""	            ЛИЧНЫЙ КАБИНЕТ\n
                Задан неверный ключ или текстовое поле пусто!""")
            elif self.CryptInput.toPlainText() and self.KeyI.text():
                res.write(decrypt(self.CryptInput.toPlainText(), self.KeyI.text()))
                self.plainTextEdit.setPlainText("""	            ЛИЧНЫЙ КАБИНЕТ\n
                Удачно! Результат выведен в файл result.txt""")
            #else:
            #    self.plainTextEdit.setPlainText("""	            ЛИЧНЫЙ КАБИНЕТ\n
            #    Текстовое поле пусто!""")


class Exit(QDialog):
    def __init__(self):
        super(Exit, self).__init__()
        loadUi("exit_window.ui", self)
        self.plainTextEdit.setReadOnly(True)
        self.action()
    def action(self):
        self.YesButton.clicked.connect(lambda: self.ext())
        self.NoButton.clicked.connect(lambda: self.back())
        self.BackToMainButton.clicked.connect(lambda: self.to_main())
    def ext(self):
        sys.exit()
    def back(self):
        widget.setCurrentWidget(pers_acc)
    def to_main(self):
        widget.setCurrentWidget(login_w)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_w = Reg_Wind()
    pers_acc = Pers_Acc()
    exit_w = Exit()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(login_w)
    widget.addWidget(pers_acc)
    widget.addWidget(exit_w)
    widget.show()
    #login_w.show()
    app.exec_()


"""
class mywindow(QDialog):
    def __init__(self):
        super(mywindow, self).__init__()
        loadUi("exit_window.ui", self)
        self.come()
    def come(self):
        #self.button_yes = self.buttonBox.setStandardButtons()
        self.BackToMainButton.clicked.connect(lambda: self.plainTextEdit.setPlainText(f'{self.buttonBox.buttons()}'))
        #self.buttonBox.clicked.connect(lambda: self.plainTextEdit.setPlainText('321'))

class Regs(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(532, 485)
        self.LoginButton = QtWidgets.QPushButton(Dialog)
        self.LoginButton.setGeometry(QtCore.QRect(210, 320, 93, 28))
        self.LoginButton.setObjectName("LoginButton")
        self.RegButton = QtWidgets.QPushButton(Dialog)
        self.RegButton.setGeometry(QtCore.QRect(420, 430, 93, 28))
        self.RegButton.setObjectName("RegButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(150, 40, 231, 91))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.PassInput = QtWidgets.QCommandLinkButton(Dialog)
        self.PassInput.setGeometry(QtCore.QRect(170, 360, 151, 48))
        self.PassInput.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.PassInput.setObjectName("PassInput")
        self.LoginInput = QtWidgets.QLineEdit(Dialog)
        self.LoginInput.setGeometry(QtCore.QRect(120, 180, 291, 22))
        self.LoginInput.setObjectName("LoginInput")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 260, 291, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.LoginButton.setText(_translate("Dialog", "Вход"))
        self.RegButton.setText(_translate("Dialog", "PushButton"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "            ГЛАВНАЯ СТРАНИЦА\n"
"Для входа в систему введите свой логин и пароль в поля ниже"))
        self.PassInput.setText(_translate("Dialog", "Регистрация"))
        self.LoginInput.setPlaceholderText(_translate("Dialog", "Логин (Имя пользователя или Ваше ФИО)"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Пароль"))


class Pers_Acc(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(735, 574)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(180, 20, 381, 87))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.CryptInput = QtWidgets.QTextEdit(Dialog)
        self.CryptInput.setGeometry(QtCore.QRect(40, 150, 651, 271))
        self.CryptInput.setObjectName("CryptInput")
        self.CryptButton = QtWidgets.QPushButton(Dialog)
        self.CryptButton.setGeometry(QtCore.QRect(40, 460, 151, 28))
        self.CryptButton.setObjectName("CryptButton")
        self.SwitcherButton = QtWidgets.QPushButton(Dialog)
        self.SwitcherButton.setGeometry(QtCore.QRect(40, 520, 131, 28))
        self.SwitcherButton.setObjectName("SwitcherButton")
        self.ExitButton = QtWidgets.QPushButton(Dialog)
        self.ExitButton.setGeometry(QtCore.QRect(600, 520, 93, 28))
        self.ExitButton.setObjectName("ExitButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "                ЛИЧНЫЙ КАБИНЕТ\n"
"Здесь Вы можете зашифровать или расшифровать Ваш текст"))
        self.CryptInput.setPlaceholderText(_translate("Dialog", "Введите Ваш текст"))
        self.CryptButton.setText(_translate("Dialog", "Зашифровать текст"))
        self.SwitcherButton.setText(_translate("Dialog", "Сменить действие"))
        self.ExitButton.setText(_translate("Dialog", "Выйти"))


class Exit(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 140, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 70, 211, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.BackToMainButton = QtWidgets.QPushButton(Dialog)
        self.BackToMainButton.setGeometry(QtCore.QRect(150, 230, 93, 28))
        self.BackToMainButton.setObjectName("BackToMainButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Вы действительно хотите выйти?"))
        self.BackToMainButton.setText(_translate("Dialog", "На Главную"))
"""


