import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_initialization():
    alice = Customer("Alice")
    latte = Coffee("Latte")
    
    with pytest.raises(ValueError):
        Order(alice, latte, 0.5)  # Price too low
    
    with pytest.raises(ValueError):
        Order(alice, latte, 10.5)  # Price too high
    
    with pytest.raises(ValueError):
        Order("NotACustomer", latte, 5.0)  # Invalid customer
    
    with pytest.raises(ValueError):
        Order(alice, "NotACoffee", 5.0)  # Invalid coffee
    
    order = Order(alice, latte, 5.0)
    assert order.price == 5.0

def test_order_relationships():
    alice = Customer("Alice")
    latte = Coffee("Latte")
    order = Order(alice, latte, 5.0)
    
    assert order.customer == alice
    assert order.coffee == latte