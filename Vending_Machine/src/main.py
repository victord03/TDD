
class VendingMachine:
    inventory: dict

    def __init__(self):
        self.inventory = dict()

    def add_item(self, item: dict):

        if not self.inventory.get(item['name']):
            self.inventory[item['name']] = item['cost']

    def count_items(self):
        return len(self.inventory.keys())

    def give_item_list(self):
        return list(self.inventory.keys())



