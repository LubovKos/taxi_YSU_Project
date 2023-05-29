from Order import Order
from Driver import Driver


class TaxistManager:
    def __init__(self):
        self.__inactive_drivers: list[Driver] = []
        self.__busy_drivers: list[Driver] = []
        self.__active_drivers: list[Driver] = []

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

