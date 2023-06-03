from Clients.Clients_manager import ClientsManager
from Driver.Taxists_manager import TaxistManager
from Map import Map
from Order.Orders_database import OrderDataBase


class Manager:
    def __init__(self):
        self.__taxists_manager = TaxistManager()
        self.__clients_manager = ClientsManager()
        self.__map = Map()
        places = open('Data/graph.txt')
        self.__map.download_connection(places)
        names = open('Data/names.txt')
        self.__map.download_places(names)
        self.__orders = OrderDataBase()

    def starting(self):
        self.__taxists_manager.download_drivers('Data/data_file.json')
        self.__taxists_manager.activate_drivers()
        self.__clients_manager.download_clients('Data/clients_data_file.json')
        self.__clients_manager.activate_clients()

        while True:
            self.__taxists_manager.tick()
            if self.__clients_manager.have_seeking_clients:
                order = self.__clients_manager.create_order()
                order.calc_duration(self.__map.calc_distance(order.get_departure_point(), order.get_arrival_point()))
                self.__orders.add_order(order)
                print('Идёт поиск машины...')
                while self.__taxists_manager.search_free_driver(order) is None:
                    self.__taxists_manager.tick()
