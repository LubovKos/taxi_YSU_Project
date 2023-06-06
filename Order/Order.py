import uuid

with open('Data/names.txt') as file:
    points = [line.rstrip() for line in file]

tariff_list = ['economy class', 'comfort class', 'business class']


class Order:
    """docstring"""

    def __init__(self):
        self.__departure_point: str = ""
        self.__arrival_point: str = ""
        self.__tariff: str = ""
        self.__id: uuid = uuid.uuid4()
        self.__duration = None
        self.__cost = None

    @property
    def get_id(self):
        return self.__id

    @property
    def get_departure_point(self):
        return self.__departure_point

    @property
    def get_arrival_point(self):
        return self.__arrival_point

    @property
    def get_tariff(self):
        return self.__tariff

    def set_tariff(self, new_tariff):
        self.__tariff = new_tariff

    def set_depart_point(self, point: str):
        self.__departure_point = point

    def input_arrival_point(self):
        print('Введите конечную точку маршрута:')
        while True:
            for i in range(len(points)):
                print('Пункт №{}: {}'.format(i + 1, points[i]))
            arrival_point = input().strip()
            if arrival_point in points:
                print('Конечный пункт {} выбран!'.format(arrival_point))
                self.__arrival_point = arrival_point
                break
            print('Ошибка ввода, повторите!')

    def input_tariff(self):
        print('Введите тариф:')
        for i in range(len(tariff_list)):
            print("Тариф №{}: {}".format(i + 1, tariff_list[i]))

        while True:
            tariff = int(input())
            if 1 <= tariff <= len(tariff_list) and tariff != '\n':
                print('Тариф {} выбран!'.format(tariff))
                self.__tariff = tariff_list[tariff - 1]
                break
            print('Ошибка ввода, повторите!')

    @property
    def get_duration(self):
        return self.__duration

    def calc_duration(self, distance: int):
        print(distance)
        self.__duration = float(distance / (8.61 * 60))

    def calc_cost(self):
        pass

    def payment_process(self):
        pass


"""
    def set_tariff(self, tar: str) -> str:
        while True:
            print("Введите тариф:")
            for i in range(len(self.__all_rate)): #
                print("Тариф №{}: {}".format(i + 1, self.__all_rate[i]))
            rate = input().lower().strip()
            if 0 <= rate < len(self.__all_rate):
                print("Тариф №{} выбран!".format(rate))
                break
            print("Ошибка ввода, повторите!")
            break
        return rate
"""
