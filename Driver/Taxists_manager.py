import json
import sys
import uuid
import numpy

from Map import Map
from Driver.Car import Car
from Order.Order import Order
from Driver.Driver import Driver


class TaxistManager:
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

    def activate_drivers(self):
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

    def tick(self):
        i = 0
        while i < len(self.busy_drivers):
            driver = self.busy_drivers[i]
            if driver.is_finished:
                driver.release()
                self.busy_drivers.remove(driver)
                self.__active_drivers.append(driver)
                i -= 1
                print('\033[44mDriver {} has completed the trip!\033[0m'.format(driver.get_full_name))
            i += 1

        for driver in self.__active_drivers:
            pass
            # сделать рандомизацию передвижения незанятых водителей

    def is_id_in_busy_drivers(self, srch_id: uuid) -> bool:
        for driver in self.busy_drivers:
            if srch_id == driver.get_order_id():
                return True
        return False
