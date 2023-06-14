from unittest.mock import patch, MagicMock

from vending_machine.vm_class import vending_machine as m
from vending_machine.src.main import main
import pytest

# machine_instance = setup()

def setup():
    return m.VendingMachine()

water = {'name': 'Water', 'cost': 0.5}
coca_cola = {'name': 'Coca Cola', 'cost': 0.8}
red_bull = {'name': 'Red Bull', 'cost': 2.0}
soda = {'name': 'Soda', "cost": 0.6}
lucozade = {'name': 'Lucozade', 'cost': 1.8}
orange_juice = {'name': 'Orange Juice', 'cost': 1.2}

param_list_items = pytest.mark.parametrize(
    'item1,item2,item3,stock_amount,result',
    [
        (water, coca_cola, red_bull, 2, ['Water', 'Coca Cola', 'Red Bull']),
        (coca_cola, soda, orange_juice, 2, ['Coca Cola', 'Soda', 'Orange Juice']),
        (soda, soda, soda, 2, ['Soda']),
        (lucozade, lucozade, soda, 2, ['Lucozade', 'Soda'])
    ],
)

param_stock_amounts = pytest.mark.parametrize(
    'item,stock_amount,result',
    [
        (water, 3, 3),
        (water, 9, 9),
    ]
)

param_not_allowed_stock_amounts = pytest.mark.parametrize(
    'item,stock_amount,result',
    [
        (water, 0, ValueError),
        (water, -3, ValueError),
    ]
)

param_refill_requests = pytest.mark.parametrize(
    'item1,item2,item1_stock_amount,item2_stock_amount,result',
    [
        (water, coca_cola, 8, 6, []),
        (water, coca_cola, 2,  6, ['Water']),
        (water, coca_cola, 2,  1, ['Water', 'Coca Cola'])

    ]
)

param_sales_log = pytest.mark.parametrize(
    'item1,item2,item3,sales1,sales2,sales3,result',
    [
        (water,coca_cola,red_bull,2,1,1,{'Water': 2, 'Coca Cola': 1, 'Red Bull': 1}),
        (orange_juice,soda,water,4,2,9,{'Orange Juice': 4, 'Soda': 2, 'Water': 9}),
        (lucozade,red_bull,orange_juice,2,12,6,{'Lucozade': 2, 'Red Bull': 12, 'Orange Juice': 6}),
    ]
)

def test_create_a_vending_machine():
    assert isinstance(setup(), m.VendingMachine)

def test_vending_machine_has_an_inventory_as_a_dict():
    assert isinstance(setup().inventory, dict)

def test_adding_items_to_inventory():
    machine_instance = setup()
    stock_amount = 2
    machine_instance.add_item(water, stock_amount)
    assert machine_instance.inventory['Water']

def test_add_item_with_cost_not_as_string_tries_to_convert_it():
    machine_instance = setup()
    water_2 = {'name': 'Water', 'cost': '0.5'}
    stock_amount = 2
    machine_instance.add_item(water_2, stock_amount)
    assert isinstance(machine_instance.inventory['Water'], float)

def test_add_empty_item_fails():
    machine_instance = setup()
    water_2 = {'name': 'Water', 'cost': ''}
    stock_amount = 2
    with pytest.raises(ValueError):
        assert machine_instance.add_item(water_2, stock_amount)

def test_adding_multiple_items_of_the_same_name_only_stores_one_dict_key():
    machine_instance = setup()
    stock_amount = 2
    machine_instance.add_item(water, stock_amount)
    machine_instance.add_item(water, stock_amount)
    assert list(machine_instance.inventory.keys()) == ["Water"]

def test_count_available_items():
    machine_instance = setup()
    assert machine_instance.count_items() == len(machine_instance.inventory.keys())

@param_list_items
def test_give_a_list_with_the_name_of_all_available_items(item1, item2, item3, stock_amount, result):
    machine_instance = setup()
    machine_instance.inventory = dict()
    machine_instance.add_item(item1, stock_amount)
    machine_instance.add_item(item2, stock_amount)
    machine_instance.add_item(item3, stock_amount)
    assert machine_instance.give_item_list() == result

def test_machine_has_a_wallet():
    machine_instance = setup()
    assert isinstance(machine_instance.wallet, float)

def test_add_amount_to_machine_wallet():
    machine_instance = setup()
    amount = 100.0
    machine_instance.add_to_wallet(amount)
    assert machine_instance.wallet == amount

def test_add_negative_amount_to_machine_wallet_returns_value_error():
    machine_instance = setup()
    amount = -48.5

    with pytest.raises(ValueError):
        assert machine_instance.add_to_wallet(amount)

def test_purchase_item_increases_wallet_amount_by_item_cost():
    machine_instance = setup()
    initial_wallet = machine_instance.wallet
    stock_amount = 2
    machine_instance.add_item(water, stock_amount)
    machine_instance.purchase_item(water['name'])
    assert machine_instance.wallet == initial_wallet + float(water['cost'])

def test_purchase_item_decreases_stock_amount_by_one():
    machine_instance = setup()
    item_name = water['name']
    stock_amount = 2
    machine_instance.add_item(water, stock_amount)
    initial_stock_amount = machine_instance.stock[item_name]
    machine_instance.purchase_item(item_name)
    assert machine_instance.stock[item_name] == initial_stock_amount - 1

@param_stock_amounts
def test_stock_of_each_item(item, stock_amount, result):
    machine_instance = setup()
    machine_instance.add_item(item, stock_amount)
    assert machine_instance.available_stock('Water') == result

@param_not_allowed_stock_amounts
def test_adding_zero_or_negative_stock_amount_returns_value_error(item, stock_amount, result):
    machine_instance = setup()

    with pytest.raises(ValueError):
        assert machine_instance.add_item(item, stock_amount) == result

@param_refill_requests
def test_check_all_stock(item1,item2,item1_stock_amount,item2_stock_amount,result):
    machine_instance = setup()
    machine_instance.add_item(item1, item1_stock_amount)
    machine_instance.add_item(item2, item2_stock_amount)
    assert machine_instance.check_all_stock() == result

@param_sales_log
def test_sold_item_logged(item1,item2,item3,sales1,sales2,sales3,result):
    machine_instance = setup()
    stock_amount = 20

    machine_instance.add_item(item1, stock_amount)
    machine_instance.add_item(item2, stock_amount)
    machine_instance.add_item(item3, stock_amount)

    for _ in range(0, sales1):
        item_name = item1['name']
        machine_instance.purchase_item(item_name)

    for _ in range(0, sales2):
        item_name = item2['name']
        machine_instance.purchase_item(item_name)

    for _ in range(0, sales3):
        item_name = item3['name']
        machine_instance.purchase_item(item_name)

    assert machine_instance.sales_log == result

@patch('vending_machine.src.main.VendingMachine')
def test_main(mock_vending_machine):
    mock_vending_machine = MagicMock(spec=m.VendingMachine)
    main()
    assert isinstance(mock_vending_machine, m.VendingMachine)