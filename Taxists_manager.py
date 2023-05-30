import json

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
        # print('\n')
        for person in data:
            car = person["car"]
            driver_car = Car(car["license_plate"], car["color"], car["brand"], car["capacity"],
                             car["child_seat_availability"], car["category"])
            driver = Driver(driver_car, person["full_name"], person["user_id"], person["location"], person["bank"])
            self.__free_drivers.append(driver)
            # driver.print_info()
            # print('\n')

    def __search_free_driver(self, order: Order):
        if len(self.__active_drivers) != 0:
            pass  # надо сделать поиск самого близкого водителя
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