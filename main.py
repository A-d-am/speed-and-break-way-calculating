import menu
import speed
import math
import break_way
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets

# Список коэффициентов сцепления автомобиля с дорогой ( в зависимости от типа покрытия )
INDEX_ICE = 0.1  # обледенение
INDEX_ROLLED_SNOW = 0.2  # укатанный снег
INDEX_DIRT_ROAD = 0.5  # грунтовка
INDEX_WET_ASPHALT = 0.4  # мокрый асфальт
INDEX_NORM_ASPHALT = 0.7  # обычный асфальт
# Список коэффициентов торможения автомобиля в зависимости от его вида
VEHICLE_PASS_CAR = 1  # легковой автомобиль
VEHICLE_TRUCK = 2  # грузовой автомобиль


def choice_road(index):
    if index == 1:
        return INDEX_ICE
    elif index == 2:
        return INDEX_ROLLED_SNOW
    elif index == 3:
        return INDEX_DIRT_ROAD
    elif index == 4:
        return INDEX_WET_ASPHALT
    elif index == 5:
        return INDEX_NORM_ASPHALT


def choice_vehicle(index):
    if index == 1:
        return VEHICLE_PASS_CAR
    elif index == 2:
        return VEHICLE_TRUCK


class Main(QtWidgets.QMainWindow, menu.Ui_MainWindow):  # main window

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.speedButton.clicked.connect(self.open_speed_wind)
        self.break_wayButton.clicked.connect(self.open_breakway_win)

    def open_speed_wind(self):
        self.close()
        self.w = CalcSpeed()
        self.w.show()

    def open_breakway_win(self):
        self.close()
        self.w = CalcBreakWay()
        self.w.show()


class CalcBreakWay(QtWidgets.QMainWindow, break_way.Ui_Form):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.back_to_menu_button.clicked.connect(self.back_to_menu)
        self.calculate_button.clicked.connect(self.calculate)

    def calculate(self):
        try:
            road_type = choice_road(int(self.road_type_line.text()))
            vehicle_type = choice_vehicle(int(self.vehicle_type_line.text()))
            speed = float(self.speed_line.text())
            speed_si = speed / 3.6
            reaction_time = float(self.reaction_time_line.text())
            temp1 = pow(speed, 2) * vehicle_type
            temp2 = 254 * road_type
            break_way = round(((temp1 / temp2) + (speed_si * reaction_time)), 2)
            self.print_result(break_way)
        except:
            self.print_error('Ошибка ввода, повторите попытку')

    def print_error(self, err):
        self.result_textBrowser.clear()
        self.result_textBrowser.setText(err)

    def print_result(self, result):
        self.result_textBrowser.clear()
        self.result_textBrowser.setText("Длина тормозного пути составляет " + str(result) + " м")

    def back_to_menu(self):
        self.close()
        self.w = Main()
        self.w.show()


class CalcSpeed(QtWidgets.QMainWindow, speed.Ui_Form):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.calculate_button.clicked.connect(self.calculate)
        self.back_to_menu_button.clicked.connect(self.back_to_menu)

    def calculate(self):
        try:
            road_type = choice_road(int(self.road_type_line.text()))
            vehicle_type = choice_vehicle(int(self.vehicle_type_line.text()))
            br_way = float(self.br_way_line.text())
            x1 = br_way * road_type * 254
            x2 = vehicle_type
            speed = round((math.sqrt(x1 / x2)), 2)
            self.print_result(speed)
        except:
            self.print_error('Ошибка ввода, повторите попытку')

    def print_error(self, err):
        self.result_textBrowser.clear()
        self.result_textBrowser.setText(err)

    def print_result(self, result):
        self.result_textBrowser.clear()
        self.result_textBrowser.setText("Скорость автомобиля равна " + str(result) + " км/ч")

    def back_to_menu(self):
        self.close()
        self.w = Main()
        self.w.show()


def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = Main()
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  
    main()  
