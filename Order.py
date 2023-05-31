import uuid


class Order:
    """docstring"""
    def __init__(self):
        self.departure_point: str = ""
        self.arrival_point: str = ""
        self.tariff: str = ""
        self.id: uuid = uuid.uuid4()
        # self.cost = cost (cost will be counting by lower function - calc_cost) (?)

    def get_id(self):
        return self.id

    def get_departure_point(self):
        return self.departure_point

    def get_arrival_point(self):
        return self.arrival_point

    def set_depart_point(self, point: str):
        self.departure_point = point

    def set_arrival_point(self, point: str):
        self.arrival_point = point

    def set_tariff(self, tar: str):
        self.tariff = tar

    def calc_cost(self):
        pass

    def payment_process(self):
        pass
