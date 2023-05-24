import Car


class Location:
    # i don't think we should use this class (?)
    pass


class Driver:
    """docstring"""

    def __init__(self):
        """Constructor"""
        self.car = None
        self.full_name = None
        self.user_id = None
        self.location = None
        # bank or driver's bank account (?)
        self.bank = None

    def __init__(self, car: Car, full_name: str, user_id: str, location: Location, bank: str) -> None:
        """Constructor with parameters"""
        self.car = car
        self.full_name = full_name
        self.user_id = user_id
        self.location = location
        # bank or driver's bank account (?)
        self.bank = bank

    def __update_location(self):
        # self.location += random(x, y)
        pass

    @property
    def get_location(self) -> Location:
        self.__update_location()
        return self.location

    @property
    def set_location(self, new_location: Location) -> None:
        self.location = new_location
