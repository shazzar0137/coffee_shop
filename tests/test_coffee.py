import pytest
from coffee import Coffee
from order import Order
from customer import Customer

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("Te")  # Name too short
    with pytest.raises(ValueError):
        Coffee(123)  # Invalid type
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_orders_method():
    latte = Coffee("Latte")
    alice = Customer("Alice")
    bob = Customer("Bob")
    
    Order(alice, latte, 5.0)
    Order(bob, latte, 4.5)
    
    assert len(latte.orders()) == 2

def test_coffee_customers_method():
    latte = Coffee("Latte")
    alice = Customer("Alice")
    bob = Customer("Bob")
    
    Order(alice, latte, 5.0)
    Order(bob, latte, 4.5)
    
    customers = latte.customers()
    assert len(customers) == 2
    assert alice in customers
    assert bob in customers

def test_coffee_num_orders_method():
    latte = Coffee("Latte")
    alice = Customer("Alice")
    
    Order(alice, latte, 5.0)
    Order(alice, latte, 4.5)
    
    assert latte.num_orders() == 2

def test_coffee_average_price_method():
    latte = Coffee("Latte")
    alice = Customer("Alice")
    
    Order(alice, latte, 5.0)
    Order(alice, latte, 4.5)
    
    assert latte.average_price() == 4.75