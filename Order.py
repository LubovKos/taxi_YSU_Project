import uuid

points: list = []
with open('names.txt') as file:
    lines = [line.rstrip() for line in file]


class Order:
    """docstring"""

    def __init__(self):
        self.__departure_point: str = ""
        self.__arrival_point: str = ""
        self.__tariff: str = ""
        self.__id: uuid = uuid.uuid4()
        self.__cost = None

    def get_id(self):
        return self.__id

    def get_departure_point(self):
        return self.__departure_point

    def get_arrival_point(self):
        return self.__arrival_point

    @property
    def get_tariff(self):
        return self.__tariff

    def set_depart_point(self, point: str):
        self.__departure_point = point

    def input_arrival_point(self):
        while True:
            print("Введите конечную точку маршрута:")
            for i in range(len(points)):
                print("Пункт №{}: {}".format(i + 1, points[i]))
            arrival_point = input().lower().strip()
            if arrival_point in points:
                print("Конечный пункт {} выбран!".format(arrival_point))
                break
            print("Ошибка ввода, повторите!")
            break
        self.__arrival_point = arrival_point

    def calc_cost(self):
        pass

    def payment_process(self):
        pass

    def input_tariff(self, new_tariff='economy class'):
        self.__tariff = new_tariff

    @get_tariff.setter
    def get_tariff(self, value):
        self._get_tariff = value


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
