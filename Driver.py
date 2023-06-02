import time
import uuid

from Order import Order
from Car import Car


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

    # занять водителя
    def pick_up(self, new_order: Order):
        self.__executable_order = new_order
        self.__is_busy = True

    # освободить водителя
    def release(self):
        self.__executable_order = None
        self.__is_busy = False

    # начало поездки
    def starting_trip(self):
        self.__start_time = time.time()

    @property
    def get_location(self):
        return self.__location

    @property
    def get_full_name(self):
        return self.__full_name

    @property
    def get_category(self):
        return self.__car.get_category

    @property
    def get_order_id(self):
        return self.__order_id

 #   def set_order_id(self, new_id):
 #       self.__order_id = new_id

    def set_location(self, location: str):
        self.__location = location

    def __update_location(self):
        pass

#добавить нормальный duration
    @property
    def is_finished(self, duration: float = None) -> bool:
        if time.time() - self.__start_time > duration:
            return True
        return False

    def print_info(self):
        self.__car.print_info()
        print("Driver: ", self.__full_name, self.__location, self.__bank, sep=' | ')
