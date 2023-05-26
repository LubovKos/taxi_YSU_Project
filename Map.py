from typing import TextIO


class MyMap(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MyMap, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Map(metaclass=MyMap):
    def __init__(self):
        self.__adj = [[]]

    def download(self, f: TextIO):
        pass