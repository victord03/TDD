
class VendingMachine:
    inventory: dict
    wallet: float

    def __init__(self):
        self.inventory = dict()
        self.wallet = float()

    def add_item(self, item: dict):

        if not self.inventory.get(item['name']):
            self.inventory[item['name']] = float(item['cost'])

    def count_items(self):
        return len(self.inventory.keys())

    def give_item_list(self):
        return list(self.inventory.keys())

    def add_to_wallet(self, amount: float):
        if amount < 0:
            raise ValueError('Cannot add negative amount.')
        else:
            self.wallet += amount

    def purchase_item(self, item: str):
        self.wallet += self.inventory[item]