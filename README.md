# coffee_shop
# Coffee Shop Domain Model Project

Welcome to the Coffee Shop Domain Model project! This Python application models a coffee shop domain using object-oriented programming principles. It consists of three main entities: `Customer`, `Coffee`, and `Order`, with defined relationships between them.

## Table of Contents
- [Project Overview](#project-overview)
- [Setup and Installation](#setup-and-installation)
- [Domain Model](#domain-model)
- [Class Descriptions](#class-descriptions)
- [Usage](#usage)
- [Testing](#testing)
- [Debugging](#debugging)
- [Folder Structure](#folder-structure)
- [License](#license)

## Project Overview

This project aims to model a coffee shop domain where:
- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.

The system implements proper validation, relationships, and aggregation methods to ensure data integrity and provide useful insights.

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone [your-repository-url]
   cd coffee_shop
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Install Dependencies:**
   ```bash
   pipenv install pytest
   ```

## Domain Model

The domain model consists of three main classes with the following relationships:
- `Customer` and `Coffee` have a many-to-many relationship through `Order`.
- Each `Order` is associated with one `Customer` and one `Coffee`.

## Class Descriptions

### Customer Class (`customer.py`)

- **Attributes:**
  - `name`: String between 1 and 15 characters.

- **Methods:**
  - `orders()`: Returns a list of all orders for the customer.
  - `coffees()`: Returns a unique list of coffees the customer has ordered.
  - `create_order(coffee, price)`: Creates a new order associated with the customer and a coffee.

- **Class Method:**
  - `most_aficionado(coffee)`: Returns the customer who has spent the most on a specific coffee.

### Coffee Class (`coffee.py`)

- **Attributes:**
  - `name`: String with at least 3 characters.

- **Methods:**
  - `orders()`: Returns a list of all orders for the coffee.
  - `customers()`: Returns a unique list of customers who have ordered the coffee.
  - `num_orders()`: Returns the total number of orders for the coffee.
  - `average_price()`: Returns the average price of orders for the coffee.

### Order Class (`order.py`)

- **Attributes:**
  - `customer`: Customer instance.
  - `coffee`: Coffee instance.
  - `price`: Float between 1.0 and 10.0.

- **Relationships:**
  - Links a customer and a coffee through an order.

## Usage

### Creating Instances

```python
from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
order1 = alice.create_order(latte, 5.0)
order2 = Order(bob, latte, 4.5)
order3 = Order(alice, espresso, 3.0)
```

### Accessing Relationships

```python
# Get customer's orders
print(alice.orders())  # [order1, order3]

# Get coffee's orders
print(latte.orders())  # [order1, order2]

# Get unique coffees for a customer
print(alice.coffees())  # [latte, espresso]

# Get unique customers for a coffee
print(latte.customers())  # [alice, bob]
```

### Using Aggregate Methods

```python
# Get number of orders for a coffee
print(latte.num_orders())  # 2

# Get average price for a coffee
print(latte.average_price())  # 4.75

# Find most aficionado customer for a coffee
print(Customer.most_aficionado(latte).name)  # Alice
```

## Testing

To ensure the functionality of the project, we use pytest for testing.

1. **Navigate to Project Directory:**
   ```bash
   cd coffee_shop
   ```

2. **Run Tests:**
   ```bash
   pytest
   ```

Test files are located in the `tests` directory and cover validation, relationships, and methods for each class.

## Debugging

For interactive debugging and testing, use the `debug.py` file:

```bash
python debug.py
```

This file contains example usage and can be modified to test different scenarios.

## Folder Structure

```
coffee_shop/
├── coffee.py
├── customer.py
├── order.py
├── debug.py
├── tests/
│   ├── test_coffee.py
│   ├── test_customer.py
│   └── test_order.py
└── README.md
```

## License

This project is licensed under the MIT License. Feel free to use and modify the code as needed for your projects.

---
