import uuid
from typing import Tuple
from Order.Order import Order


class MyOrder(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MyOrder, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class OrderDataBase(metaclass=MyOrder):
    """Constructor"""

    def __init__(self):
        self.order_dict = {}

    def add_order(self, order_pair: Tuple):
        """A unique ID is created for the order
        and a client-driver pair is added to it"""
        order_id = uuid.uuid4()
        self.order_dict[order_id] = order_pair

    def delete_order(self, del_id: str):
        self.order_dict.pop(del_id)

    def output_orders(self):
        for key, value in self.order_dict.items():
            print(key)
            
    def is_in_base(self, search_id: uuid) -> bool:
        return search_id in self.order_dict
