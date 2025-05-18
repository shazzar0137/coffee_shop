
import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_validation():
    c = Customer("John")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)
    with pytest.raises(TypeError):
        Order("not_customer", coffee, 2.0)
    with pytest.raises(TypeError):
        Order(c, "not_coffee", 2.0)
