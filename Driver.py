import Car


class Driver:
    """docstring"""
    def __init__(self, car: Car, full_name: str, user_id: str, location: str, bank: str) -> None:
        """Constructor with parameters"""
        self.car = car
        self.full_name = full_name
        self.user_id = user_id
        self.location = location
        # bank or driver's bank account (?)
        self.bank = bank

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    def __update_location(self):
        pass
