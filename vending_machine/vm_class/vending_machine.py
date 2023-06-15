from vending_machine.menu_class.vm_menus import VmMenus

class VendingMachine:
    inventory: dict
    wallet: float
    stock: dict
    sales_log: dict

    menu: VmMenus

    def __init__(self):
        self.inventory = dict()
        self.wallet = float()
        self.stock = dict()
        self.sales_log = dict()
        self.menu = VmMenus()
        self.menu.options['Display items'] = self.give_item_list

    def add_item(self, item: dict, stock_count: int) -> None:

        item_name = item['name']
        item_cost = item['cost']

        if not self.inventory.get(item_name):
            self.inventory[item_name] = float(item_cost)
        if stock_count > 0:
            self.stock[item_name] = stock_count
        else:
            raise ValueError('Cannot register 0 or negative stock amount.')

    def count_items(self) -> int:
        return len(self.inventory.keys())

    def give_item_list(self) -> list:
        return list(self.inventory.keys())

    def add_to_wallet(self, amount: float) -> None:
        if amount < 0:
            raise ValueError('Cannot add negative amount.')
        else:
            self.wallet += amount

    def purchase_item(self, item_name: str) -> None:
        self.wallet += self.inventory[item_name]
        self.stock[item_name] -= 1

        if self.sales_log.get(item_name):
            self.sales_log[item_name] += 1
        else:
            self.sales_log[item_name] = 1

    def available_stock(self, item_name: str) -> str:
        return self.stock[item_name]

    def check_all_stock(self) -> list:

        items_need_restock = list()

        for item_name in self.give_item_list():
            if self.stock[item_name] < 5:
                items_need_restock.append(item_name)

        return items_need_restock

