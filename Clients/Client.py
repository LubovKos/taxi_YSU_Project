class Client:
    """docstring"""
    def __init__(self,
                 requisites: str,
                 phone_number: str,
                 bonuses: int, name: str,
                 location: str = None):
        """Constructor with parameters"""
        self.__order_id = -1
        self.__name = name
        self.__requisites = requisites
        self.__bonuses = bonuses
        self.__phone_number = phone_number
        self.__location = location

    def __update_location(self):
        # self.location += random(x, y)
        pass

    @property
    def get_name(self):
        return self.__name

    @property
    def get_order_id(self):
        return self.__order_id

    def set_order_id(self, new_id):
        self.__order_id = new_id

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def get_location(self) -> str:
        self.__update_location()
        return self.__location
