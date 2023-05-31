class Client:
    """docstring"""
    def __init__(self, requisites: str, selected_points: list, phone_number: str,
                 location: str, bonuses: int) -> None:
        """Constructor with parameters"""
        self.requisites = requisites
        self.selected_points = selected_points
        self.bonuses = bonuses
        self.phone_number = phone_number
        self.location = location

    def __update_location(self):
        # self.location += random(x, y)
        pass

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
