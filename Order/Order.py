import math
import uuid

with open('../Data/names.txt') as file:
    points = [line.rstrip() for line in file]

tariff_list = ['economy class', 'comfort class', 'business class']


class Order:
    """
    A class that stores information
    about an order
    """

    def __init__(self):
        self.__departure_point: str = ""
        self.__arrival_point: str = ""
        self.__tariff: str = ""
        self.__id: uuid = uuid.uuid4()
        self.__start_time = None
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

    @property
    def get_start_time(self):
        return self.__start_time

    @property
    def get_duration(self):
        return self.__duration

    @property
    def get_cost(self):
        return self.__cost

    def set_start_time(self, time: int):
        self.__start_time = time

    def set_tariff(self, new_tariff):
        self.__tariff = new_tariff

    def set_depart_point(self, point: str):
        self.__departure_point = point

    def set_cost(self, cost: int):
        self.__cost = cost

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

    def calc_duration(self, distance: int):
        """
        Function that calculates travel time
        """
        self.__duration = math.ceil(distance / 8.61)

    def calc_cost(self):
        """
        Function that calculates the cost for each tariff
        """
        economy_m = 0.009
        economy_time = 4
        economy_landing = 90
        comfort_m = 0.01
        comfort_time = 4
        comfort_landing = 155
        business_m = 0.02
        business_time = 10
        business_landing = 320

        distance = (self.__duration * 8.61) / 60

        if self.__tariff == 'economy class':
            self.__cost = int(economy_landing + economy_time * self.__duration / 60 + \
                              economy_m * distance)
        elif self.__tariff == 'comfort class':
            self.__cost = int(comfort_landing + comfort_time * self.__duration / 60 + \
                              comfort_m * distance)
        else:
            self.__cost = int(business_landing + business_time * self.__duration / 60 + \
                              business_m * distance)
