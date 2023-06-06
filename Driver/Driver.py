import time
import uuid

from Order.Order import Order
from Driver.Car import Car
import Manager


class Driver:
    """docstring"""

    def __init__(self,
                 car: Car,
                 full_name: str,
                 location: str, bank: str,
                 start_time: float = None) -> None:
        """Constructor with parameters"""
        self.__car = car
        self.__full_name = full_name
        self.__location = location
        # bank or driver's bank account (?)
        self.__bank = bank
        self.__start_time = start_time
        self.__order_id = None
        self.__is_busy = False
        self.__duration_trip = None

    # занять водителя
    def pick_up(self, new_order: Order):
        self.__order_id = new_order.get_id
        self.__is_busy = True
        self.starting_trip()

    # освободить водителя
    def release(self):
        for key in Manager.orders.order_dict.keys():
            if key == self.__order_id:
                self.set_location(Manager.orders.order_dict[key].get_arrival_point)
                break
        self.__order_id = None
        self.__is_busy = False

    # начало поездки
    def starting_trip(self):
        self.__start_time = time.time()

    @property
    def get_location(self):
        return self.__location

    @property
    def get_duration_trip(self):
        return self.__duration_trip

    @property
    def get_full_name(self):
        return self.__full_name

    @property
    def get_category(self):
        return self.__car.get_category

    @property
    def get_order_id(self):
        return self.__order_id
    
    @property
    def get_car(self):
        return self.__car

    def set_location(self, location: str):
        self.__location = location

    def set_duration_trip(self, dist_to_client, order_duration):
        self.__duration_trip = dist_to_client / (8.61 * 60) + order_duration

    def __update_location(self):
        pass

    @property
    def is_finished(self) -> bool:
        test_time_start = time.localtime(self.__start_time)
        test_time_finish = time.localtime(self.__start_time + self.__duration_trip)
        if time.time() - self.__start_time > self.__duration_trip:
            return True
        return False

    def print_info(self):
        self.__car.print_info()
        print("Driver: ", self.__full_name, self.__location, self.__bank, sep=' | ')
