from order import Order  # Imported inside methods

class Coffee:
    def __init__(self, name: str):
        self._name = None
        self.name = name  # Triggers setter

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Coffee name must be a string")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order._all_orders if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self) -> int:
        return len(self.orders())

    def average_price(self) -> float:
        orders = self.orders()
        if not orders:
            return 0.0
        total = sum(order.price for order in orders)
        return total / len(orders)