import math
import colorama

colorama.init(autoreset=True)


def instructions():
    print("""
    Данная программа производит расчет скорости автомобиля по длине тормозного пути.
    Вам нужно будет выбрать тип автомобиля ( легковой или грузовой ), а также тип покрытия,
    на котором замерялся тормозной путь.
    """)


def menu():
    print("""
    1 ==> Рассчет скорости автомобиля в начале торможения ( если известен тормозной путь) 
    2 ==> Рассчет тормозного пути автомобиля  ( если известна скорость в момент начала торможения) 
    3 ==> Завершение работы с програмой 
    """)


def road_type():
    print("""
    1 ==> обледенение
    2 ==> укатанный снег
    3 ==> грунтовка
    4 ==> мокрый асфальт
    5 ==> обычный асфальт
    """)


# Список коэффициентов сцепления автомобиля с дорогой ( в зависимости от типа покрытия )
INDEX_ICE = 0.1  # обледенение
INDEX_ROLLED_SNOW = 0.2  # укатанный снег
INDEX_DIRT_ROAD = 0.5  # грунтовка
INDEX_WET_ASPHALT = 0.4  # мокрый асфальт
INDEX_NORM_ASPHALT = 0.7  # обычный асфальт

# Список коэффициентов торможения автомобиля в зависимости от его вида
VEHICLE_PASS_CAR = 1  # легковой автомобиль
VEHICLE_TRUCK = 2  # грузовой автомобиль


def calculating_speed():
    flag = True
    while flag:
        try:
            print('Выберите тип дорожного покрытия')
            road_type()
            choice_road = int(input('Ваш выбор '))
            if choice_road == 1:
                choice_road = INDEX_ICE
            elif choice_road == 2:
                choice_road = INDEX_ROLLED_SNOW
            elif choice_road == 3:
                choice_road = INDEX_DIRT_ROAD
            elif choice_road == 4:
                choice_road = INDEX_WET_ASPHALT
            elif choice_road == 5:
                choice_road = INDEX_NORM_ASPHALT
            brake_way = float(input('Введите длину тормозного пути в метрах: '))
            choice_vehicle = int(input('Тип машины: легковой(введите 1) или грузовой (введите 2) '))
            if choice_vehicle == 1:
                choice_vehicle = VEHICLE_PASS_CAR
            else:
                choice_vehicle = VEHICLE_TRUCK
            x1 = brake_way * choice_road * 254
            x2 = choice_vehicle
            speed = round((math.sqrt(x1 / x2)), 2)
            print(f'Скорость автомобиля в начале торможения равна {speed} км/ч')
            print('------------------------------------')
            choise_to_continue = input('Повторить вычисления ( введите 1)  или вернуться в главное меню (введите 2) ? ')
            if choise_to_continue != '1':
                flag = False
                break
        except:
            print(colorama.Fore.RED + 'Ошибка ввода, проверьте вводимые данные и повторите попытку')


def calculating_brake_way():
    flag = True
    while flag:
        try:
            speed = float(input('Введите скорость автомобиля в км/ч '))
            speed_si = speed / 3.6
            print('Выберите тип дорожного покрытия')
            road_type()
            choice_road = int(input('Ваш выбор '))
            if choice_road == 1:
                choice_road = INDEX_ICE
            elif choice_road == 2:
                choice_road = INDEX_ROLLED_SNOW
            elif choice_road == 3:
                choice_road = INDEX_DIRT_ROAD
            elif choice_road == 4:
                choice_road = INDEX_WET_ASPHALT
            elif choice_road == 5:
                choice_road = INDEX_NORM_ASPHALT
            else:
                print('Такого пармаметра нет,проверьте строку ввода и повторите попытку')
                break
            choice_vehicle = int(input('Тип машины: легковой(введите 1) или грузовой (введите 2) '))
            if choice_vehicle == 1:
                choice_vehicle = VEHICLE_PASS_CAR
            else:
                choice_vehicle = VEHICLE_TRUCK
            x1 = pow(speed, 2) * choice_vehicle
            x2 = 254 * choice_road * 1.5
            total_break_way = round(((x1 / x2) + speed_si), 2)
            print(f'Торомзной путь автомобиля равен {total_break_way} м.')
            print('------------------------------------')
            choise_to_continue = input('Повторить вычисления ( введите 1)  или вернуться в главное меню (введите 2) ? ')
            if choise_to_continue != '1':
                flag = False
                break
        except:
            print(colorama.Fore.RED + 'Ошибка ввода, проверьте вводимые данные и повторите попытку')


def main():
    flag = True
    while flag:
        try:
            instructions()
            menu()
            choice = int(input('Ваш выбор: '))
            if choice == 1:
                calculating_speed()
            elif choice == 2:
                calculating_brake_way()
            elif choice == 3:
                print('Завершение сеанса')
                flag = False
        except:
            print(colorama.Fore.RED + 'Ошибка ввода, проверьте вводимые данные и повторите попытку')


main()
