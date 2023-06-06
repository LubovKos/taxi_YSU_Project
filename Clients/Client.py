class Client:
    """This class stores data about the client"""
    def __init__(self,
                 requisites: str,
                 phone_number: str,
                 bonuses: int, name: str,
                 location: str = None):
        self.__order_id = -1
        self.__name = name
        self.__requisites = requisites
        self.__bonuses = bonuses
        self.__phone_number = phone_number
        self.__location = location

    @property
    def get_name(self):
        return self.__name

    @property
    def get_order_id(self):
        return self.__order_id

    @property
    def get_location(self):
        return self.__location

    def set_order_id(self, new_id):
        self.__order_id = new_id

    def set_location(self, location: str):
        self.__location = location


