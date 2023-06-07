class Client:
    """This class stores data about the client"""
    def __init__(self,
                 requisites: str,
                 phone_number: str,
                 bonuses: int, name: str,
                 location: str = None):
        self.__name = name
        self.__requisites = requisites
        self.__bonuses = bonuses
        self.__phone_number = phone_number
        self.__location = location

    @property
    def get_name(self):
        return self.__name

    @property
    def get_location(self):
        return self.__location

    @property
    def get_bonuses(self):
        return self.__bonuses

    @property
    def get_requisites(self):
        return self.__requisites

    def set_location(self, location: str):
        self.__location = location

    def set_bonuses(self, bonuses: int):
        self.__bonuses = bonuses
