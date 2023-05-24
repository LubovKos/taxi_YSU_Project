from random import random
from typing import Optional


class Car:
    """docstring"""

    def __init__(self):
        """Constructor"""
        self.license_plate = None
        self.color = None
        self.brand = None
        self.capacity = None
        self.child_seat_availability = None
        self.category = None

    def __init__(self, license_plate: str, color: str, brand: str, capacity: int,
                 child_seat_availability: bool, category: str) -> None:

        """Constructor with parameters"""
        self.license_plate = license_plate
        self.color = color
        self.brand = brand
        self.capacity = capacity
        self.child_seat_availability = child_seat_availability
        self.category = category
