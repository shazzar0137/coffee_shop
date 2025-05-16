from customer import Customer
from coffee import Coffee

class Order:
    _all_orders = []

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order._all_orders.append(self)

    @property
    def customer(self) -> Customer:
        return self._customer

    @customer.setter
    def customer(self, value: Customer):
        if not isinstance(value, Customer):
            raise ValueError("Customer must be a Customer instance")
        self._customer = value

    @property
    def coffee(self) -> Coffee:
        return self._coffee

    @coffee.setter
    def coffee(self, value: Coffee):
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        self._coffee = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be a number")
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = float(value)