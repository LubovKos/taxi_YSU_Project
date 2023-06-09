import uuid
from typing import Tuple, Dict
from Driver.Driver import Driver
from Clients.Client import Client
from Order.Order import Order


class OrderDataBase:
    """
    Database of orders.
    Order management class
    """

    def __init__(self):
        self.order_dict: Dict[uuid, Tuple[Driver, Client, Order]] = {}

    def add_order(self, order_triple: Tuple[Driver, Client, Order]):
        """A unique ID is created for the order
        and a client-driver pair is added to it"""
        self.order_dict[order_triple[2].get_id] = order_triple

    def delete_order(self, del_id: str):
        self.order_dict.pop(del_id)

    def output_orders(self):
        for key, value in self.order_dict.items():
            print(key)
            
    def is_in_base(self, search_id: uuid) -> bool:
        return search_id in self.order_dict
