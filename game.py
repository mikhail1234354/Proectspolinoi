from Lib_of_game import *

from pictures import data

from about_us import About_us


#
# button_list = ['00000000000000000000',
#                '00011000000000000000',
#                '00011100000000000000',
#                '00011110000000000000',
#                '00012211000000000000',
#                '00012221000001110000',
#                '00012211110111110000',
#                '00001122221222110000',
#                '00001222221222110000',
#                '00013222222222100000',
#                '00011222222211100000',
#                '00042222312210000000',
#                '00001222114410000000',
#                '00001122224100110000',
#                '00001211111101111000',
#                '00000121122211111100',
#                '00000112222110011000',
#                '00000122221100000000',
#                '00000011221000000000',
#                '00000000110000000000']
#
# color_dict = {'*) Ластик': 'e0e1e2', "1) Черный": '000000', "2) Желтый": 'ffff00', "3) Белый": 'ffffff',
#               "4) Розовый": 'ffa9dd'}


class Painting(QWidget):
    def __init__(self, text):  # инициализирем класс
        super().__init__()
        self.name_of_picture = text # название картинки -> str
        self.initUI()

    def initUI(self):
        self.setFixedSize(1000, 800)
        self.move(150, 150)
        self.setWindowTitle("рисунок1")  # создаем размеры и название окна
        button_list = data[self.name_of_picture][0] # выбираем нужный список кнопок
        self.color_dict = data[self.name_of_picture][1] # выбираем нужный словарь цветов

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

        self.btn = QPushButton('Об авторах', self) # добавляем кнопку про авторов
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(10, 10)

        self.btn.clicked.connect(self.open_second_form)

    def open_second_form(self): # функция вызывает окно с информацией про авторов
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
