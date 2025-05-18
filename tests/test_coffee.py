
import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("ab")

def test_average_price():
    c = Customer("Joe")
    coffee = Coffee("Americano")
    c.create_order(coffee, 5.0)
    c.create_order(coffee, 7.0)
    assert round(coffee.average_price(), 2) == 6.0