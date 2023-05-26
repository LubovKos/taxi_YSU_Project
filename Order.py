class Order:
    """docstring"""
    def __init__(self, departure_point: str, arrival_point: str, tariff: str, cost: int) -> None:
        """Constructor with parameters"""
        self.departure_point = departure_point
        self.arrival_point = arrival_point
        self.tariff = tariff
        # self.cost = cost (cost will be counting by lower function - calc_cost) (?)

    def calc_cost(self):
        pass

    def payment_process(self):
        pass
