import uuid

points: list = []
with open('names.txt') as file:
    points = [point.rstrip() for point in file]

tariff_list = ['economy class', 'comfort class', 'business class']


class Order:
    """docstring"""
    def __init__(self):
        self.departure_point: str = ""
        self.arrival_point: str = ""
        self.tariff: str = ""
        self.id: uuid = uuid.uuid4()

    def get_id(self):
        return self.id

    def get_departure_point(self):
        return self.departure_point

    def get_arrival_point(self):
        return self.arrival_point

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

        while True:
            tariff = input().strip()
            if tariff in tariff_list:
                print('Тариф {} выбран!'.format(tariff))
                self.__tariff = tariff
                break
            print('Ошибка ввода, повторите!')

    def calc_cost(self):
        pass

    def payment_process(self):
        pass
