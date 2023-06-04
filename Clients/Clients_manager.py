import json
import uuid
import numpy

from Order.Order import Order
from Clients.Client import Client
from Map import Map


class ClientsManager:
    def __init__(self):
        self.__inactive_clients: list[Client] = []
        self.busy_clients: list[Client] = []
        self.__active_clients: list[Client] = []
        self.__map: Map = Map()

    @property
    def have_seeking_clients(self) -> bool:
        if len(self.__active_clients) == 0:
            return False
        return True

    def __choose_client(self) -> int:
        while True:
            print('Выберите клиента из списка:')
            for i in range(len(self.__active_clients)):
                print('Клиент №{}: {}'.format(i + 1, self.__active_clients[i].get_name))
            client_number = int(input())
            if 1 <= client_number <= len(self.__active_clients):
                print('Клиент №{} выбран!'.format(client_number))
                break
            print('Ошибка ввода, повторите!')
        return client_number - 1

    def download_clients(self, file: str) -> None:
        with open(file, "r") as read_file:
            data = json.load(read_file)
        for person in data:
            client = Client(person['requisites'], person['phone_number'],
                            person['bonuses'], person['name'], person['location'])
            self.__inactive_clients.append(client)

    def activate_clients(self):
        if len(self.__inactive_clients) == 0:
            return
        random_integer_array = numpy.random.random_integers(0, len(self.__inactive_clients) - 1, 6)
        i = len(self.__inactive_clients) - 1
        while i >= 0:
            clients = self.__inactive_clients[i]
            if i in random_integer_array:
                self.__active_clients.append(clients)
                self.__inactive_clients.remove(clients)
            i -= 1

    def create_order(self) -> Order:
        client_number = self.__choose_client()
        curr_client = self.__active_clients[client_number]
        self.busy_clients.append(self.__active_clients.pop(client_number))

        print('Сформируйте заказ!')
        curr_order = Order()
        curr_client.set_order_id(curr_order.get_id)
        curr_order.set_depart_point(curr_client.location)
        curr_order.input_arrival_point()
        curr_order.input_tariff()
        print('Заказ сформирован')

        return curr_order

    def closing_order(self, client: Client):
        """
        order completion method:
        returning object to inactive pool
        """
        self.__inactive_clients.append(client)
        self.busy_clients.remove(client)
        # тут надо что-то с оплатой придумать

    def is_id_in_busy_clients(self, srch_id: uuid) -> bool:
        for client in self.busy_clients:
            if srch_id == client.get_order_id():
                return True
        return False
