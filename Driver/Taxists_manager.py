import json
import sys
import numpy

from Map import Map
from Driver.Car import Car
from Order.Order import Order
from Driver.Driver import Driver


class TaxistManager:
    """
    Taxi driver activity management class
    """
    def __init__(self):
        self.__inactive_drivers: list[Driver] = []
        self.busy_drivers: list[Driver] = []
        self.__active_drivers: list[Driver] = []
        self.__map: Map = Map()

    def download_drivers(self, file: str) -> None:
        with open(file, "r") as read_file:
            data = json.load(read_file)
        for person in data:
            car = person['car']
            driver_car = Car(car['license_plate'], car['color'], car['brand'],
                             car['child_seat_availability'], car['category'], car['image'])
            driver = Driver(driver_car, person['full_name'], person['location'], person['bank'])
            self.__inactive_drivers.append(driver)
        for elem in self.__inactive_drivers:
            elem.print_info()

    def activate_drivers(self) -> None:
        """
        Activates drivers from the
        inactive pool to active ones
        """
        if len(self.__inactive_drivers) == 0:
            return
        random_integer_array = numpy.random.random_integers(0, len(self.__inactive_drivers) - 1, 6)
        print(random_integer_array)
        i = len(self.__inactive_drivers) - 1
        while i >= 0:
            driver = self.__inactive_drivers[i]
            if i in random_integer_array:
                self.__active_drivers.append(driver)
                self.__inactive_drivers.remove(driver)
            i -= 1
        for elem in self.__active_drivers:
            elem.print_info()

    def search_free_driver(self, order: Order):
        """
        The function is looking for a free driver to
        complete the order. If there is no free driver of
        the selected type to complete the order,
        then selects an available driver from another tariff
        """
        if len(self.__active_drivers) != 0:
            driver_found = False
            minimal_dist = sys.maxsize
            suitable_driver = self.__active_drivers[0]
            for driver in self.__active_drivers:
                curr_dist = self.__map.calc_distance(driver.get_location, order.get_departure_point)
                if order.get_tariff == driver.get_category and curr_dist < minimal_dist:
                    minimal_dist = curr_dist
                    suitable_driver = driver
                    driver_found = True

            if driver_found is False:
                if order.get_tariff == 'economy class':
                    print('Economy class cars were not found. We offer you a '
                          'comfort class car. We are already looking for it...')
                    order.set_tariff('comfort class')
                elif order.get_tariff == 'comfort class':
                    print('Comfort class cars were not found. We offer you a '
                          'business class car. We are already looking for it...')
                    order.set_tariff('business class')
                else:
                    print('Business class cars were not found. We offer you a '
                          'economy class car. We are already looking for it...')
                    order.set_tariff('economy class')
                return None

            self.busy_drivers.append(suitable_driver)
            self.__active_drivers.remove(suitable_driver)
            suitable_driver.pick_up(order)
            suitable_driver.set_duration_trip(minimal_dist, order.get_duration)
            print('Driver has been found!')
            suitable_driver.print_info()
            return suitable_driver
        return None

    def closing_order(self, driver: Driver):
        driver.release()
        self.busy_drivers.remove(driver)
        self.__active_drivers.append(driver)
