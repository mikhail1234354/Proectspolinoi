from Lib_of_about_us import *


class About_us(QWidget):  # инициализируем класс
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(1000, 800)
        self.move(150, 150)
        self.setWindowTitle('Об авторах')

        self.pixmap_M = QPixmap('Misha1.jpeg')  # Размещаем фото Милаила
        self.image_M = QLabel(self)
        self.image_M.move(150, 50)
        self.image_M.resize(267, 400)
        self.image_M.setPixmap(self.pixmap_M)

        self.pixmap_P = QPixmap('Polina1.jpeg')  # Размещаем фото Полины
        self.image_P = QLabel(self)
        self.image_P.move(550, 50)
        self.image_P.resize(300, 400)
        self.image_P.setPixmap(self.pixmap_P)

        self.text1 = QLabel(self)  # Размещаем текст про Михаила
        self.text1.move(100, 480)
        self.text1.setText("Лучший программист на свете")
        self.text1.setFont(QFont("Times", 16))

        self.text2 = QLabel(self)  # Размещаем текст про Полину
        self.text2.move(550, 480)
        self.text2.setText("Лучшая программистка на свете")
        self.text2.setFont(QFont("Times", 16))

        self.text3 = QLabel(self)  # И еще один текст, про то какие мы молодцы
        self.text3.move(100, 630)
        self.text3.setText("Эти прекрасные люди трудились над созданием этого " + '\n'
                                                                                  "приложения, согласитесь, они милашки")
        self.text3.setFont(QFont("Times", 20))

