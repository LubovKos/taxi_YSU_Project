import json

import numpy

from Order import Order
from Client import Client


class ClientsManager:
    def __init__(self):
        self.__inactive_clients: list[Client] = []
        self.__busy_clients: list[Client] = []
        self.__active_clients: list[Client] = []

    def download_clients(self, file: str) -> None:
        with open(file, "r") as read_file:
            data = json.load(read_file)
        for person in data:
            client = Client(person["requisites"], person["phone_number"],
                            person["bonuses"], person["name"], person["location"])
            self.__inactive_clients.append(client)

    def activate_clients(self):
        if len(self.__inactive_clients) == 0:
            return
        random_integer_array = numpy.random.random_integers(0, len(self.__inactive_clients) - 1, 6)
        print(random_integer_array)
        i = len(self.__inactive_clients) - 1
        while i >= 0:
            clients = self.__inactive_clients[i]
            if i in random_integer_array:
                self.__active_clients.append(clients)
                self.__inactive_clients.remove(clients)
            i -= 1
        for clients in self.__active_clients:
            clients.print_info()

    # ??
    def __choose_client(self) -> int:
        while True:
            print("Выберите клиента из списка:")
            for i in range(len(self.__active_clients)):
                print("Клиент №{}: {}".format(i + 1, self.__active_clients[i].name))
            client_number = int(input())
            if 0 <= client_number < len(self.__active_clients):
                print("Клиент №{} выбран!".format(client_number))
                break
            print("Ошибка ввода, повторите!")
        return client_number

    # def __choose_arrival_point(self) -> str:
    #     while True:
    #         print("Введите конечную точку маршрута:")
    #         # for i in range(len(self.__active_clients)):
    #         #     print("Клиент №{}: {}".format(i + 1, self.__active_clients[i].name))
    #         arrival_point = input().lower().strip()
    #         # if 0 <= client_number < len(self.__active_clients):
    #         #     print("Клиент №{} выбран!".format(client_number))
    #         #    break
    #         print("Ошибка ввода, повторите!")
    #         break
    #     return arrival_point

    def create_order(self) -> Order:
        client_number = self.__choose_client()
        curr_client = self.__active_clients[client_number]
        self.__busy_clients.append(self.__active_clients.pop(client_number))

        print("Сформируйте заказ!")
        curr_order = Order()
        curr_client.set_order_id(curr_order.get_id())
        curr_order.set_depart_point(curr_client.location)
        curr_order.set_arrival_point()
        curr_order.set_tariff()
        print("Заказ сформирован")

        return curr_order

    def closing_order(self, order: Order):
        """
        order completion method:
        returning object to inactive pool
        """
        for i in range(len(self.__busy_clients)):
            if self.__busy_clients[i].get_order_id() == order.get_id():
                self.__inactive_clients.append(self.__busy_clients.pop(i))
                break
