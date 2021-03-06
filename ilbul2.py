
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(245, 81)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon.fromTheme("logo.png")
        Form.setWindowIcon(icon)
        self.yazi = QtWidgets.QLabel(Form)
        self.yazi.setGeometry(QtCore.QRect(0, -10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.yazi.setFont(font)
        self.yazi.setObjectName("yazi")
        self.text = QtWidgets.QLineEdit(Form)
        self.text.setGeometry(QtCore.QRect(110, 0, 121, 31))
        self.text.setObjectName("text")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 42, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.clicked.connect(self.tikla)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def tikla(self):
        a = self.text.text()

        if a == '01':
            print("ADANA")

        elif a == '02':
            print("Adıyaman")


        elif a == '03':
            print("Afyon")

        elif a == '04':
            print("Ağrı")


        elif a == '68':
            print("Aksaray")

        elif a == '05':
            print("Amasya")

        elif a == '06':
            print("Ankara")

        elif a == '07':
            print("Antalya")

        elif a == '75':
            print("Ardahan")

        elif a == '08':
            print("Artvin")

        elif a == '09':
            print("Aydın")

        elif a == '10':
            print("Balıkesir")

        elif a == '74':
            print("Bartın")

        elif a == '72':
            print("Batman")

        elif a == '69':
            print("Bayburt")

        elif a == '11':
            print("Bilecik")

        elif a == '12':
            print("Bingöl")

        elif a == '13':
            print("Bitlis")

        elif a == '14':
            print("Bolu")

        elif a == '15':
            print("Burdur")

        elif a == '16':
            print("Bursa")

        elif a == '17':
            print("Çanakkale")

        elif a == '18':
            print("Çankırı")

        elif a == '19':
            print("Çorum")

        elif a == '20':
            print("Denizli")

        elif a == '21':
            print("Diyarbakır")

        elif a == '81':
            print("Düzce")

        elif a == '22':
            print("Edirne")

        elif a == '23':
            print("Elazığ")

        elif a == '24':
            print("Erzincan")

        elif a == '25':
            print("Erzurum")

        elif a == '26':
            print("Eskşehir")

        elif a == '27':
            print("Gaziantep")

        elif a == '28':
            print("Giresun")

        elif a == '29':
            print("Gümüşhane")

        elif a == '30':
            print("Hakkari")

        elif a == '31':
            print("Hatay")

        elif a == '76':
            print("Iğdır")

        elif a == '32':
            print("Isparta")

        elif a == '33':
            print("İçel")

        elif a == '34':
            print("İstanbul")

        elif a == '35':
            print("İzmir")

        elif a == '46':
            print("Kahramanmaraş")

        elif a == '78':
            print("Karabük")

        elif a == '70':
            print("Karaman")

        elif a == '36':
            print("Kars")

        elif a == '37':
            print("Kastamonu")

        elif a == '38':
            print("Kayseri")

        elif a == '39':
            print("Kırklareli")

        elif a == '71':
            print("Kırkkale")

        elif a == '40':
            print("Kırşehir")

        elif a == '79':
            print("Kilis")

        elif a == '41':
            print("Kocaeli")

        elif a == '42':
            print("Konya")

        elif a == '43':
            print("Kütahya")

        elif a == '44':
            print("Malatya")

        elif a == '45':
            print("Manisa")

        elif a == '47':
            print("Mardin")

        elif a == '48':
            print("Muğla")

        elif a == '49':
            print("Muş")

        elif a == '50':
            print("Nevşehir")

        elif a == '51':
            print("Niğde")

        elif a == '52':
            print("Ordu")

        elif a == '80':
            print("Osmaniye")

        elif a == '53':
            print("Rize")

        elif a == '54':
            print("Sakarya")

        elif a == '55':
            print("Samsun")

        elif a == '56':
            print("Siirt")

        elif a == '57':
            print("Sinop")

        elif a == '58':
            print("Sivas")

        elif a == '63':
            print("Şanlıurfa")

        elif a == '73':
            print("Şırnak")

        elif a == '59':
            print("Tekirdağ")

        elif a == '60':
            print("Tokat")

        elif a == '61':
            print("Trabzon")

        elif a == '62':
            print("Tunceli")

        elif a == '64':
            print("Uşak")

        elif a == '65':
            print("Van")

        elif a == '77':
            print("Yalova")

        elif a == '66':
            print("Yozgat")

        elif a == '67':
            print("Zonguldak")

        else:
            print("BULUNUMADI")
        




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "İL KODU"))
        self.yazi.setText(_translate("Form", "İL KODU :"))
        self.pushButton.setText(_translate("Form", "İL ARA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
