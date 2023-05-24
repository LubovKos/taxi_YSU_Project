class Location:
    # i don't think we should use this class (?)
    pass


class Client:
    """docstring"""

    def __init__(self):
        """Constructor"""
        self.requisites = None
        self.selected_points = None
        self.bonuses = None
        self.phone_number = None
        self.location = None

    def __init__(self, requisites: str, selected_points: list, phone_number: str,
                 location: Location, bonuses: int) -> None:

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
    def get_location(self) -> Location:
        self.__update_location()
        return self.location

    @property
    def set_location(self, new_location: Location) -> None:
        self.location = new_location
