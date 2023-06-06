import uuid
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

    def add_order(self, new_order: Order):
        self.order_dict[new_order.get_id] = new_order

    def delete_order(self, del_id: str):
        self.order_dict.pop(del_id)

    def output_orders(self):
        for key, value in self.order_dict.items():
            print(key)
            
    def is_in_base(self, search_id: uuid) -> bool:
        return search_id in self.order_dict
