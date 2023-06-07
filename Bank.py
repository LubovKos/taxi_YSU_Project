import json


def download_base() -> dict:
    with open('Data/bank_account.json', "r") as read_file:
        data = json.load(read_file)
    client_base = {}
    for elem in data:
        client_base[elem['requisites']] = elem['sum']
    return client_base


class Bank:
    """
    Class for changing the account
    of the client and the driver
    """
    def __init__(self):
        self.__client_base = download_base()

    def money_transfer(self, money_amount: int, client_card: str, driver_card: str) -> None:
        print(self.__client_base[client_card], self.__client_base[driver_card])
        self.__client_base[client_card] -= money_amount
        self.__client_base[driver_card] += money_amount
        print(self.__client_base[client_card], self.__client_base[driver_card])
