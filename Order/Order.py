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

        economy_km = 0.09
        economy_time = 4
        economy_landing = 90
        comfort_km = 0.1
        comfort_time = 4
        comfort_landing = 155
        business_km = 0.2
        business_time = 10
        business_landing = 320

        distance = self.__duration * 8.61 * 60

        if self.__tariff == 'economy class':
            self.__cost = economy_landing + economy_time * self.__duration + \
                          economy_km * distance
        elif self.__tariff == 'comfort class':
            self.__cost = comfort_landing + comfort_time * self.__duration + \
                          comfort_km * distance
        else:
            self.__cost = business_landing + business_time * self.__duration + \
                          business_km * distance

    def payment_process(self):
        print('Стоимость поездки составила:', self.__cost)
        print('Выберите способ оплаты:', '1. Оплата наличными',
              '2. Оплата по карте', sep='\n')

        while True:
            payment_method = int(input())
            if payment_method == 1 or payment_method == 2:
                break
            else:
                print('Ошибка ввода!')

        print('Спасибо за оплату!')


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
