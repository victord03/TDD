from Vending_Machine.src import main as m
import pytest

def setup():
    return m.VendingMachine()

water = {'name': 'Water', 'cost': '0.5'}
coca_cola = {'name': 'Coca Cola', 'cost': '0.8'}
red_bull = {'name': 'Red Bull', 'cost': '2.0'}
soda = {'name': 'Soda', "cost": '0.6'}
lucozade = {'name': 'Lucozade', 'cost': '1.8'}
orange_juice = {'name': 'Orange Juice', 'cost': '1.2'}

param = pytest.mark.parametrize(
    'item1,item2,item3,result',
    [
        (water, coca_cola, red_bull, ['Water', 'Coca Cola', 'Red Bull']),
        (coca_cola, soda, orange_juice, ['Coca Cola', 'Soda', 'Orange Juice']),
        (soda, soda, soda, ['Soda']),
        (lucozade, lucozade, soda, ['Lucozade', 'Soda'])
    ],
)

def test_create_a_vending_machine():
    assert isinstance(setup(), m.VendingMachine)

def test_vending_machine_has_an_inventory_as_a_dict():
    assert isinstance(setup().inventory, dict)

def test_adding_items_to_inventory():
    machine_instance = setup()
    machine_instance.add_item(water)
    assert machine_instance.inventory['Water']

def test_adding_multiple_items_of_the_same_name_only_stores_one_dict_key():
    machine_instance = setup()
    machine_instance.add_item(water)
    machine_instance.add_item(water)
    assert list(machine_instance.inventory.keys()) == ["Water"]

def test_count_available_items():
    machine_instance = setup()
    assert machine_instance.count_items() == len(machine_instance.inventory.keys())

@param
def test_give_a_list_with_the_name_of_all_available_items(item1, item2, item3, result):
    machine_instance = setup()
    machine_instance.inventory = dict()
    machine_instance.add_item(item1)
    machine_instance.add_item(item2)
    machine_instance.add_item(item3)
    assert machine_instance.give_item_list() == result

