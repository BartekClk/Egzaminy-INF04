import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QRadioButton, QTextEdit, QMessageBox
from PyQt6.uic import loadUi
from PyQt6.QtGui import QPixmap

class MyApp(QMainWindow):
    images = []
    

    def __init__(self):
        super().__init__()
        loadUi("untitled.ui", self)
        self.setWindowTitle("Nadaj Przesyłkę. PESEL: 00000000000")

        self.images.append(QPixmap("./list.png"))
        self.images.append(QPixmap("./paczka.png"))
        self.images.append(QPixmap("./pocztowka.png"))

        self.radioButton_1.setChecked(True)

        self.image.setPixmap(self.images[2])
        self.image.resize(self.images[2].width(), self.images[2].height())

        self.price.setText("Cena:")

        self.checkPrice.clicked.connect(self.priceCheck)

        self.confirm.clicked.connect(self.confirmAll)

    
    def priceCheck(self):
        if self.radioButton_1.isChecked():
            self.price.setText("Cena: 1zł")
            self.image.setPixmap(self.images[2])
            self.image.resize(self.images[2].width(), self.images[2].height())
        elif self.radioButton_2.isChecked():
            self.price.setText("Cena: 1,5zł")
            self.image.setPixmap(self.images[0])
            self.image.resize(self.images[0].width(), self.images[0].height())
        elif self.radioButton_3.isChecked():
            self.price.setText("Cena: 10zł")
            self.image.setPixmap(self.images[1])
            self.image.resize(self.images[1].width(), self.images[1].height())

    def confirmAll(self):
        msg = QMessageBox() #trzeba zaimportowac from PyQt6.QtWidgets import QMessageBox
        msg.setWindowTitle("")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        text = self.postal.text()

        if(len(text)!=5):
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Nieprawidłowa liczba cyfr w kodzie pocztowym")
        else:
            try:
                int(text)
                msg.setIcon(QMessageBox.Icon.NoIcon)
                msg.setText("Dane przesyłki zostały wprowadzone")
            except:
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText("Kod pocztowy powinien się składać z samych cyfr")
            


        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())