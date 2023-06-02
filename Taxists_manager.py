import json

from Map import Map
from Car import Car
from Order import Order
from Driver import Driver


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
            car = person["car"]
            driver_car = Car(car["license_plate"], car["color"], car["brand"],
                             car["child_seat_availability"], car["category"])
            driver = Driver(driver_car, person["full_name"], person["location"], person["bank"])
            self.__inactive_drivers.append(driver)

    # переписать
    def activate_drivers(self):
        i = 0
        while i < len(self.__inactive_drivers):
            driver = self.__inactive_drivers[i]
            self.__active_drivers.append(driver)
            self.__inactive_drivers.remove(driver)
            i -= 1
            i += 1
            driver.print_info()
        print("_________________________")

    def search_free_driver(self, order: Order) -> Driver | None:
        if len(self.__active_drivers) != 0:
            driver_found = False
            minimal_dist = 1000000
            # может мы и не найдем нужного водилу (?)
            for driver in self.__active_drivers:
                if order.get_tariff == driver.get_category:
                    if self.__map.calc_distance(driver.get_location, order.get_departure_point()) < minimal_dist:
                        minimal_dist = self.__map.calc_distance(driver.get_location, order.get_departure_point())
                        driver.pick_up(order)
                        suitable_driver = driver
                        print('Водитель найден!')

            if driver_found is False:
                if order.get_tariff == 'economy class':
                    order.get_tariff = 'comfort class'
                elif order.get_tariff == 'comfort class':
                    order.get_tariff = 'business class'
                else:
                    for driver in self.__active_drivers:
                        if self.__map.calc_distance(driver.get_location, order.get_departure_point()) < minimal_dist:
                            minimal_dist = self.__map.calc_distance(driver.get_location, order.get_departure_point())
                            driver.pick_up(order)
                            suitable_driver = driver
                            print('Водитель найден!')
            return suitable_driver
        return None

    def tick(self):
        for i in range(len(self.busy_drivers)):
            driver = self.busy_drivers[i]
            if driver.is_finished:
                driver.release()
                self.busy_drivers.remove(driver)
                self.__active_drivers.append(driver)
                i -= 1
                print('Водитель {} завершил поездку!'.format(driver.get_full_name()))
                driver.set_order_id(None)

        for driver in self.__active_drivers:
            pass
            # сделать рандомизацию передвижения незанятых водителей
