from order import Order  # Imported inside methods to avoid circular imports

class Customer:
    def __init__(self, name: str):
        self._name = None
        self.name = name  # Triggers the setter

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order._all_orders if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price: float):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        orders = [order for order in Order._all_orders if order.coffee == coffee]
        if not orders:
            return None
        customer_totals = {}
        for order in orders:
            customer = order.customer
            customer_totals[customer] = customer_totals.get(customer, 0) + order.price
        if not customer_totals:
            return None
        max_total = max(customer_totals.values())
        max_customers = [cust for cust, total in customer_totals.items() if total == max_total]
        return max_customers[0] if max_customers else None