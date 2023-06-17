from vending_machine.vm_class.vending_machine import VendingMachine


def main():
    water = {"name": "Water", "cost": 0.5}
    coca_cola = {"name": "Coca Cola", "cost": 0.8}
    red_bull = {"name": "Red Bull", "cost": 2.0}
    soda = {"name": "Soda", "cost": 0.6}
    lucozade = {"name": "Lucozade", "cost": 1.8}
    orange_juice = {"name": "Orange Juice", "cost": 1.2}

    vm = VendingMachine()

    vm.add_item(water, 2)
    vm.add_item(lucozade, 1)
    vm.add_item(orange_juice, 5)

    vm.menu_sequence()
    print(vm.sales_log)


if __name__ == "__main__":
    main()
