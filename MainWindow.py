import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox


class MainWindow(QWidget):
    '''
    мы создаем класс главного окна
    '''

    def __init__(self):  # инициализируем наш класс
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(500, 300)
        self.setWindowTitle('Sandbox')  # задаем размеры и название окна

        self.label = QLabel(self)
        self.label.setText("Выберите поле, на котором хотите рисовать:")
        self.label.move(10, 5)  # создаем текст приветствия

        self.spisok = QComboBox(self)  # мы создали выдающий список для выбора картины
        self.spisok.addItem('текст13433434543')
        self.spisok.addItem('текст2')
        self.spisok.addItem('текст3')
        self.spisok.addItem('текст4')
        self.spisok.addItem('текст5')
        self.spisok.addItem('текст6')
        self.spisok.addItem('текст7')  # добавили варианты в наш список

        self.spisok.move(10, 30)
        self.spisok.activated[str].connect(self.click)  # мы подключили наш виджет к функции

    def click(self, text):  # эта функция будет перекидывать нас на выбранный вариант

        self.second_form = SecondForm(self, text)
        self.second_form.show()


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Вторая форма')

        self.lbl = QLabel(args[-1], self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
