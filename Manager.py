from Clients_manager import ClientsManager
from Taxists_manager import TaxistManager


class Manager:
    def __init__(self):
        self.__taxists_manager = TaxistManager()
        self.__clients_manager = ClientsManager()

    def clinet_releasing(self):
        for client in self.__clients_manager.busy_clients:
            for driver in self.__taxists_manager.busy_drivers:
                if client.get_order_id == driver.get_order_id:
                    return None
        return True

    def starting(self):
        self.__taxists_manager.download_drivers('data_file.json')
        self.__taxists_manager.activate_drivers()
        self.__clients_manager.download_clients('clients_data_file.json')
        self.__clients_manager.activate_clients()

        while True:
            self.__taxists_manager.tick()
            order = self.__clients_manager.create_order()
            print('Идёт поиск машины...')
            while self.__taxists_manager.search_free_driver(order) is None:
                self.__taxists_manager.tick()
