class Client:
    """docstring"""
    def __init__(self, requisites: str, phone_number: str,
                 location: str, bonuses: int, name: str) -> None:
        """Constructor with parameters"""
        self.order_id = -1
        self.name = name
        self.requisites = requisites
        self.bonuses = bonuses
        self.phone_number = phone_number
        self.location = location

    def __update_location(self):
        # self.location += random(x, y)
        pass

    def get_order_id(self):
        return self.order_id

    def set_order_id(self, identif):
        self.order_id = identif

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def get_location(self) -> str:
        self.__update_location()
        return self.location
