from Clients.Clients_manager import ClientsManager
from Driver.Taxists_manager import TaxistManager
from Map import Map
from Order.Orders_database import OrderDataBase
from Drawer import Drawer
from Timer import Timer

orders = OrderDataBase()


class Manager:
    def __init__(self):
        self.__taxists_manager = TaxistManager()
        self.__clients_manager = ClientsManager()
        self.__map = Map()
        places = open('Data/graph.txt')
        self.__map.download_connection(places)
        names = open('Data/names.txt')
        self.__map.download_places(names)
        self.__timer = Timer()

    def tick(self):
        self.__timer.minute_tick()

        i = 0
        while i < len(self.__taxists_manager.busy_drivers):
            driver = self.__taxists_manager.busy_drivers[i]
            if driver.is_finished:
                driver.release() #TODO
                self.__taxists_manager.busy_drivers.remove(driver)
                self.__taxists_manager.add_to_active(driver)
                i -= 1
                print('\033[44mDriver {} has completed the trip!\033[0m'.format(driver.get_full_name))
            i += 1

        # прохожусь по базе заказов, если в бизи таксистах нет такого заказа - удаляю из базы заказ
        for key in orders.order_dict:
            if not self.__taxists_manager.is_id_in_busy_drivers(key):
                orders.delete_order(key)

        # прохожусь по бизи клиентам, если не нашел по айдишнику в базе заказов - для клиента закончилась поезка (списали бабки)
        for client in self.__clients_manager.busy_clients:
            if not orders.is_in_base(client.get_order_id()):
                self.__clients_manager.closing_order(client)

    def starting(self):
        self.__taxists_manager.download_drivers('Data/data_file.json')
        self.__taxists_manager.activate_drivers()
        self.__clients_manager.download_clients('Data/clients_data_file.json')
        self.__clients_manager.activate_clients()
        while True:
            self.tick()
            if self.__clients_manager.have_seeking_clients:
                client = self.__clients_manager.choose_client()
                order = self.__clients_manager.create_order()
                order.set_start_time(self.__timer.get_time)
                order.set_depart_point(client.get_location)
                order.calc_duration(self.__map.calc_distance(order.get_departure_point, order.get_arrival_point))
                print('Идёт поиск машины...')
                driver = self.__taxists_manager.search_free_driver(order)
                while driver is None:
                    self.tick()
                    driver = self.__taxists_manager.search_free_driver(order)
                drawer = Drawer(driver, order)
                drawer.draw_order()
                orders.add_order((client, driver))
            else:
                print('PEI PIVO')
                break
