import time

from Bank import Bank
from Clients.Client import Client
from Clients.Clients_manager import ClientsManager
from Driver.Driver import Driver
from Driver.Taxists_manager import TaxistManager
from Order.Orders_database import OrderDataBase
from Order.Order import Order
from Map import Map
from Drawer import Drawer
from Timer import Timer


def create_order() -> Order:
    print('Create the order!')
    curr_order = Order()
    curr_order.input_arrival_point()
    curr_order.input_tariff()
    print('Order was created')
    return curr_order


class Manager:
    """
    The class manages the application, writes off funds,
    starts and ends the trip, keeps track of time
    """
    def __init__(self):
        self.__taxists_manager = TaxistManager()
        self.__clients_manager = ClientsManager()
        self.__map = Map()
        places = open('Data/graph.txt')
        self.__map.download_connection(places)
        names = open('Data/names.txt')
        self.__map.download_places(names)
        self.__timer = Timer()
        self.orders = OrderDataBase()
        self.bank = Bank()

    def payment_process(self, order: Order, client: Client, driver: Driver):
        """
        A function that manages payment and write-offs
        """
        print('Cost of trip is:', order.get_cost)
        print('Choose the way of payment:', '1. Cash',
              '2. Card', sep='\n')

        while True:
            payment_method = int(input())
            if payment_method == 1 or payment_method == 2:
                break
            else:
                print('Incorrect input!')

        print('Number of bonuses:', client.get_bonuses)
        print('Write off bonuses?', '1. Yes', '2. No')
        while True:
            is_used_bonus = int(input())
            if is_used_bonus == 1 or is_used_bonus == 2:
                break
            else:
                print('Incorrect input!')
        if is_used_bonus == 1:
            if client.get_bonuses < int(order.get_cost / 2):
                order.set_cost(order.get_cost - client.get_bonuses)
                client.set_bonuses(0)
            else:
                order.set_cost(int(order.get_cost / 2))
                client.set_bonuses(client.get_bonuses - int(order.get_cost))
        else:
            client.set_bonuses(client.get_bonuses + int(order.get_cost / 100 * 5))
            print('You get bonuses:', client.get_bonuses)

        self.bank.money_transfer(order.get_cost, client.get_requisites, driver.get_bank)

        print('Payment has been made!')

    def tick(self):
        """
        A function that simulates the process of a trip
        """
        self.__timer.minute_tick()
        i = 0
        while i < len(self.__taxists_manager.busy_drivers):
            driver = self.__taxists_manager.busy_drivers[i]
            if driver.is_finished:
                curr_id = driver.get_order_id
                client = self.orders.order_dict[curr_id][1]
                self.payment_process(self.orders.order_dict[curr_id][2], client, driver)
                client.set_location(self.orders.order_dict[curr_id][2].get_arrival_point)
                driver.set_location(self.orders.order_dict[curr_id][2].get_arrival_point)
                self.__taxists_manager.closing_order(driver)
                self.__clients_manager.closing_order(client)
                self.orders.delete_order(curr_id)
                i -= 1
                print('\033[44mDriver {} has completed the trip!\033[0m'.format(driver.get_full_name))
            i += 1

    def starting(self):
        """
        The function that launches the program
        """
        self.__taxists_manager.download_drivers('Data/data_file.json')
        self.__taxists_manager.activate_drivers()
        self.__clients_manager.download_clients('Data/clients_data_file.json')
        self.__clients_manager.activate_clients()
        while True:
            self.tick()
            if self.__clients_manager.have_seeking_clients:
                client = self.__clients_manager.choose_client()
                order = create_order()
                order.set_start_time(self.__timer.get_time)
                order.set_depart_point(client.get_location)
                order.calc_duration(self.__map.calc_distance(order.get_departure_point, order.get_arrival_point))
                print('Searching for driver...')
                driver = self.__taxists_manager.search_free_driver(order)
                while driver is None:
                    self.tick()
                    driver = self.__taxists_manager.search_free_driver(order)
                order.calc_cost()
                drawer = Drawer(driver, order)
                drawer.draw_order()
                self.orders.add_order((driver, client, order))
            else:
                self.tick()
                time.sleep(5)
                if len(self.orders.order_dict) == 0:
                    print('No orders')
                    break
