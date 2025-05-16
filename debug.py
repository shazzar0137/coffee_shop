from customer import Customer
from coffee import Coffee
from order import Order

# Create instances
alice = Customer("Alice")
bob = Customer("Bob")
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
order1 = alice.create_order(latte, 5.0)
order2 = bob.create_order(latte, 4.5)
order3 = alice.create_order(espresso, 3.0)

# Test methods
print("Alice's orders:", [o.coffee.name for o in alice.orders()])  # ['Latte', 'Espresso']
print("Latte orders count:", latte.num_orders())  # 2
print("Most aficionado for Latte:", Customer.most_aficionado(latte).name)  # Alice