import json
import numpy

import Map
from Car import Car
from Order import Order
from Driver import Driver


class TaxistManager:
    def __init__(self):
        self.__inactive_drivers: list[Driver] = []
        self.__busy_drivers: list[Driver] = []
        self.__active_drivers: list[Driver] = []

    def download_drivers(self, file: str) -> None:
        with open(file, "r") as read_file:
            data = json.load(read_file)
        for person in data:
            car = person["car"]
            driver_car = Car(car["license_plate"], car["color"], car["brand"],
                             car["child_seat_availability"], car["category"])
            driver = Driver(driver_car, person["full_name"], person["location"], person["bank"])
            self.__inactive_drivers.append(driver)

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
        for driver in self.__active_drivers:
            driver.print_info()

    def search_free_driver(self, order: Order, mapp: Map) -> Driver:
        if len(self.__active_drivers) != 0:
            driver_found = False
            minimal_dist = 1000000
            # может мы и не найдем нужного водилу (?)
            for driver in self.__active_drivers:
                if order.tariff == driver.get_category:
                    if mapp.calc_distance(driver.get_location, order.get_departure_point()) < minimal_dist:
                        minimal_dist = mapp.calc_distance(driver.get_location, order.get_departure_point())
                        suitable_driver = driver

            if driver_found is False:
                if order.tariff == "economy class":
                    order.tariff = "comfort class"
                elif order.tariff == "comfort class":
                    order.tariff = "business class"
                else:
                    for driver in self.__active_drivers:
                        if map.calc_distance(driver.get_location, order.get_departure_point()) < minimal_dist:
                            minimal_dist = map.calc_distance(driver.get_location, order.get_departure_point())
                            suitable_driver = driver
            return suitable_driver
        else:
            while len(self.__active_drivers) == 0:
                self.__tick()
                # делаем поиск самого близкого водителя
                # потом можно накатить поиск с учетом предсказаний

    def __tick(self):
        for driver in self.__busy_drivers:
            if driver.is_finished:
                driver.release()
                self.__busy_drivers.remove(driver)
                self.__active_drivers.append(driver)
        for driver in self.__active_drivers:
            pass
            # сделать рандомизацию передвижения незанятых водителей
