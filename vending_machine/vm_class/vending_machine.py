
user_input_deco = f'\n> '

main_menu = f'\nMain Menu:\n\t1. Display items'

options_under_main_menu = f'\t1. Purchase'

choose_item = f'\nWhich item to purchase ?'


class VendingMachine:
    inventory: dict
    wallet: float
    stock: dict
    sales_log: dict

    def __init__(self) -> None:
        self.inventory = dict()
        self.wallet = float()
        self.stock = dict()
        self.sales_log = dict()

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

    @staticmethod
    def display_main_menu() -> str:
        return '\n' + main_menu

    @staticmethod
    def display_options_under_main_menu() -> str:
        return '\n' + options_under_main_menu

    @staticmethod
    def get_user_input(user_input='') -> str:
        if user_input == '':
            return input(user_input_deco)
        else:
            return user_input


    def menu_sequence(self, patch_main_menu_choice='', patch_sub_menu_choice='', patch_item_name_choice=''):

        print(self.display_main_menu())

        user_input = self.get_user_input(patch_main_menu_choice)

        header = '\n' + 'Available items:'
        print(header)


        sub_menu_option = {
            '1': self.compile_items_and_prices_list_for_display,

        }

        match user_input:
            case '1':
                items_with_prices = sub_menu_option['1']()

        print(items_with_prices)

        print(self.display_options_under_main_menu())

        sub_menu_choice = self.get_user_input(patch_sub_menu_choice)

        sub_menu_options = {
            '1': choose_item,

        }

        match sub_menu_choice:
            case '1': next_text = sub_menu_options['1']

        print(next_text)

        item_name = self.get_user_input(patch_item_name_choice)
        self.purchase_item(item_name.title())


    def compile_items_and_prices_list_for_display(self):

        items_and_prices = ''

        for item_name, cost in self.inventory.items():
            items_and_prices += f"\n\t\t{item_name}: {cost} EUR"

        return items_and_prices

