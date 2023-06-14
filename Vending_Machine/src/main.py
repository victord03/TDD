
class VendingMachine:
    inventory: dict
    wallet: float
    stock: dict

    def __init__(self):
        self.inventory = dict()
        self.wallet = float()
        self.stock = dict()

    def add_item(self, item: dict, stock_count: int):

        item_name = item['name']
        item_cost = item['cost']

        if not self.inventory.get(item_name):
            self.inventory[item_name] = float(item_cost)
        if stock_count > 0:
            self.stock[item_name] = stock_count
        else:
            raise ValueError("Cannot register 0 or negative stock amount.")

    def count_items(self):
        return len(self.inventory.keys())

    def give_item_list(self):
        return list(self.inventory.keys())

    def add_to_wallet(self, amount: float):
        if amount < 0:
            raise ValueError('Cannot add negative amount.')
        else:
            self.wallet += amount

    def purchase_item(self, item_name: str):
        self.wallet += self.inventory[item_name]
        self.stock[item_name] -= 1

    def available_stock(self, item_name: str):
        return self.stock[item_name]
