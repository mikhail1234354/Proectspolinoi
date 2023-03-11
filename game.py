from Lib_of_game import *

from pictures import data

from about_us import About_us


class Painting(QWidget):
    def __init__(self, text):  # инициализирем класс
        super().__init__()
        self.name_of_picture = text
        '''name_of_picture: str
            аргумент нужен для выбора картинки'''

        self.initUI()

    def initUI(self):
        self.setFixedSize(1000, 800)
        self.move(150, 150)
        self.setWindowTitle(self.name_of_picture)  # создаем размеры и название окна
        button_list = data[self.name_of_picture][0]  # выбираем нужный список кнопок
        self.color_dict = data[self.name_of_picture][1]  # выбираем нужный словарь цветов

        for i in range(20):  # создаем поле для рисования из кнопок
            for j in range(20):
                if button_list[i][j] != '0':
                    self.button = QPushButton(button_list[i][j], self)
                    self.button.resize(30, 30)
                    self.button.move(100 + 28 * j, 100 + 28 * i)

                    self.button.clicked.connect(self.Draw)

        choose_color = QComboBox(self)  # создаем окно выбора цвета
        choose_color.addItems(self.color_dict.keys())
        choose_color.move(750, 120)
        choose_color.activated[str].connect(self.Activated)

        self.btn = QPushButton('Об авторах', self)  # добавляем кнопку про авторов
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(30, 20)

        self.btn.clicked.connect(self.open_second_form)

    def open_second_form(self):  # функция вызывает окно с информацией про авторов
        self.second_form = About_us()
        self.second_form.show()

    def Activated(self, text):  # функция считывает выбранный цвет
        self.color = text

    def Draw(self):  # функция раскрашивает кнопки
        if self.sender().text():
            self.sender().setStyleSheet(f"background-color:#{self.color_dict[self.color]}")
            if self.sender().text() == self.color.split(')')[0]:
                self.sender().setText('')
            else:
                if self.color.split()[1] == 'Черный' or "Темно" in self.color.split()[1]:
                    self.sender().setStyleSheet(f"background-color:#{self.color_dict[self.color]}; color: white")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Painting()
    ex.show()
    sys.exit(app.exec())
