from Lib_of_MainWindow import *

from game import Painting


class MainWindow(QMainWindow):
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
        self.label.resize(270, 30)

        self.spisok = QComboBox(self)  # мы создали выдающий список для выбора картины
        self.spisok.addItem('Пикачу')
        self.spisok.addItem('Вишня')
        self.spisok.addItem('Панда')
        self.spisok.addItem('Пирожное')
        self.spisok.addItem('Овечка')  # добавили варианты в наш список

        self.spisok.move(10, 30)
        self.spisok.activated[str].connect(self.click)  # мы подключили наш виджет к функции

    def click(self, text):  # эта функция будет перекидывать нас на выбранный вариант

        self.game = Painting(text)
        self.game.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())

