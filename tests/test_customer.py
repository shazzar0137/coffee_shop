import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("A" * 16)
    with pytest.raises(ValueError):
        Customer(123)
    cust = Customer("Alice")
    assert cust.name == "Alice"

def test_create_order():
    alice = Customer("Alice")
    latte = Coffee("Latte")
    order = alice.create_order(latte, 5.0)
    assert order.customer == alice
    assert order.coffee == latte
    assert order.price == 5.0

def test_most_aficionado():
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")
    Order(alice, latte, 5.0)
    Order(alice, latte, 3.0)
    Order(bob, latte, 4.0)
    assert Customer.most_aficionado(latte) == alice