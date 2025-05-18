
import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("A" * 16)

def test_create_order():
    c = Customer("TestUser")
    coffee = Coffee("Mocha")
    order = c.create_order(coffee, 5.5)
    assert order.customer == c
    assert order.coffee == coffee
