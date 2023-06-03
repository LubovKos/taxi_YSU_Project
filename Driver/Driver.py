import time
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
        self.__is_busy = False

    #занять водителя
    def pick_up(self):
        self.__is_busy = True

    #освободить водителя
    def release(self):
        self.__is_busy = False

    #начало поездки
    def starting_trip(self):
        self.__start_time = time.time()

    @property
    def get_location(self):
        return self.__location

    @property
    def get_category(self):
        return self.__car.get_category

    def set_location(self, location: str):
        self.__location = location

    def __update_location(self):
        pass

    @property
    def is_finished(self, duration: float = None) -> bool:
        if time.time() - self.__start_time > duration:
            return True
        return False

    def print_info(self):
        self.__car.print_info()
        print("Driver: ", self.__full_name, self.__location, self.__bank, sep=' | ')
