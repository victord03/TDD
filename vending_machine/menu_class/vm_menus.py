from vending_machine.data import print_statements


class VmMenus:
    options: dict

    def __init__(self):
        self.options = dict()

    @staticmethod
    def display_menu():
        print(print_statements.main_menu)
        a = VmMenus.get_user_input()
        user_option = a['']
        return user_option

    @staticmethod
    def get_user_input() -> dict:
        dictionary = dict()
        dictionary['input'] = input(print_statements.user_input_deco)
        return dictionary
