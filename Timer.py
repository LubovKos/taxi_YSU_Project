import random


class SingletonTimer(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonTimer, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Timer(metaclass=SingletonTimer):
    """
    Performs real-time emulation.
    During initialization, the time of day is randomized in seconds.
    The class has a function to add one minute.
    """
    def __init__(self):
        self.__local_time: int = random.randint(0, 84000)

    def minute_tick(self):
        self.__local_time += 60

    @property
    def get_time(self):
        return self.__local_time
