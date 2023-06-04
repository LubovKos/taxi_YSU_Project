class Car:
    """docstring"""

    def __init__(self, license_plate: str, color: str, brand: str,
                 child_seat_availability: bool, category: str, image: str) -> None:
        """Constructor with parameters"""
        self.__license_plate = license_plate
        self.__color = color
        self.__brand = brand
        self.__child_seat_availability = child_seat_availability
        self.__category = category
        self.__image = image

    def print_info(self):
        print("Car:", self.__license_plate, self.__color, self.__brand,
              self.__child_seat_availability, self.__category, sep=' | ')

    @property
    def get_category(self):
        return self.__category
