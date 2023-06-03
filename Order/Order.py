import uuid

points: list = []
with open('names.txt') as file:
    points = [point.rstrip() for point in file]

tariff_list = ['economy class', 'comfort class', 'business class']


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

    def input_depart_point(self):
        print('Введите начальную точку маршрута:')
        while True:
            departure_point = input().strip()
            if departure_point in points:
                print('Начальный пункт {} выбран!'.format(departure_point))
                self.__departure_point = departure_point
                break
            print("Ошибка ввода, повторите!")

    def input_arrival_point(self):
        print('Введите конечную точку маршрута:')
        while True:
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
            tariff = int(input()).strip()
            if 1 <= tariff <= len(self.__all_rate):
                print('Тариф {} выбран!'.format(tariff))
                self.__tariff = tariff
                break
            print('Ошибка ввода, повторите!')

    def calc_cost(self):
        pass

    def payment_process(self):
        pass
