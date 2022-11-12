import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QFont


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Главная форма')

        self.btn = QPushButton('Об авторах', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 100)

        self.btn.clicked.connect(self.open_second_form)

    def open_second_form(self):
        self.second_form = About_us()
        self.second_form.show()


class About_us(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(1000, 800)
        self.move(150, 150)
        self.setWindowTitle('Об авторах')

        self.pixmap_M = QPixmap('Misha1.jpeg')
        self.image_M = QLabel(self)
        self.image_M.move(150, 50)
        self.image_M.resize(267, 400)
        self.image_M.setPixmap(self.pixmap_M)

        self.pixmap_P = QPixmap('Polina1.jpeg')
        self.image_P = QLabel(self)
        self.image_P.move(550, 50)
        self.image_P.resize(300, 400)
        self.image_P.setPixmap(self.pixmap_P)

        self.text1 = QLabel(self)
        self.text1.move(100, 480)
        self.text1.setText("Лучший программист на свете")
        self.text1.setFont(QFont("Times", 16))

        self.text2 = QLabel(self)
        self.text2.move(550, 480)
        self.text2.setText("Лучшая программистка на свете")
        self.text2.setFont(QFont("Times", 16))

        self.text3 = QLabel(self)
        self.text3.move(100, 630)
        self.text3.setText("Эти прекрасные люди трудились над созданием этого " + '\n'
                           "приложения, согласитесь, они милашки")
        self.text3.setFont(QFont("Times", 20))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())