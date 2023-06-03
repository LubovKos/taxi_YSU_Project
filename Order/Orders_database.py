import Order


class MyOrder(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MyOrder, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class OrderDataBase(metaclass=MyOrder):
    """Constructor"""

    def __init__(self):
        self.__order_dict = {}

    def add_order(self, new_order: Order):
        self.__order_dict[new_order.id] = Order

    def delete_order(self, del_id: str):
        self.__order_dict.pop(del_id)

    def output_orders(self):
        for key, value in self.__order_dict.items():
            print(key)
