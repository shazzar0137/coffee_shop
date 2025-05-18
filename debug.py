
from customer import Customer
from coffee import Coffee
from order import Order

# Sample interactive testing
c1 = Customer("Alice")
c2 = Customer("Bob")
cof1 = Coffee("Latte")
cof2 = Coffee("Espresso")

o1 = c1.create_order(cof1, 5.0)
o2 = c2.create_order(cof1, 6.0)
o3 = c1.create_order(cof2, 7.5)

print(c1.orders())
print(c1.coffees())
print(cof1.orders())
print(cof1.customers())
print(cof1.num_orders())
print(cof1.average_price())
print(Customer.most_aficionado(cof1).name)