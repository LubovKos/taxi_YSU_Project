import uuid


class Order:
    """docstring"""
    def __init__(self):
        self.departure_point: str = ""
        self.arrival_point: str = ""
        self.tariff: str = ""
        self.id: uuid = uuid.uuid4()
        # self.cost = cost (cost will be counting by lower function - calc_cost) (?)

    def get_id(self):
        return self.id

    def get_departure_point(self):
        return self.departure_point

    def get_arrival_point(self):
        return self.arrival_point

    def input_depart_point(self):
        while True:
            print("Введите начальную точку маршрута:")
            depart_point = input().lower().strip()
            if 0 <= depart_point < len(self.__all_depart_points):
                print("Начальный пункт выбран!".format(depart_point))
                break
            print("Ошибка ввода, повторите!")
            break
        return depart_point

    def input_arrival_point(self) -> str:
        while True:
            print("Введите конечную точку маршрута:")
            arrival_point = input().lower().strip()
            if 0 <= arrival_point < len(self.__all_arrival_points):
                print("Конечный пункт выбран!".format(arrival_point))
                break
            print("Ошибка ввода, повторите!")
            break
        return arrival_point

    def input_tariff(self) -> str:
        while True:
            print("Введите тариф:")
            rate = input().lower().strip()
            if 0 <= rate < len(self.__all_rate):
                print("Тариф №{} выбран!".format(rate))
                break
            print("Ошибка ввода, повторите!")
            break
        return rate

    def calc_cost(self):
        pass

    def payment_process(self):
        pass
