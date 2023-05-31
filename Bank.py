class Bank:
    def __init__(self, client_base=None):
        if client_base is None:
            client_base = []
        self.client_base = client_base

    def add_client(self, client):
        self.client_base.append(client)

    # i have at least 0 ideas for this class
