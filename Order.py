class Order:
    """docstring"""
    def __init__(self, departure_point: str, arrival_point: str, tariff: str, cost: int) -> None:
        """Constructor with parameters"""
        self.departure_point = departure_point
        self.arrival_point = arrival_point
        self.tariff = tariff
        # self.cost = cost (cost will be counting by lower function - calc_cost) (?)

    def calc_cost(self):
        pass

    def payment_process(self):
        pass

    def endpoint_setting(self) -> str:
        while True:
            print("Введите конечную точку маршрута:")
            for i in range(len(self.__all_arrival_points)): #
                print("Пункт №{}: {}".format(i + 1, self.__all_arrival_points[i]))
            arrival_point = input().lower().strip()
            if 0 <= arrival_point < len(self.__all_arrival_points):
                print("Конечный пункт №{} выбран!".format(arrival_point))
                break
            print("Ошибка ввода, повторите!")
            break
        return arrival_point

    def rate_setting(self) -> str:
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
