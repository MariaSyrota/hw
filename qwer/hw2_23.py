from peewee import *

# Підключення до бази даних SQLite
db = SqliteDatabase('store.db')

# Створення моделі для таблиці "Покупець"
class Customer(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = db

    def __init__(self, name, email):
        self.name = name
        self.email = email

# Створення моделі для таблиці "Товар"
class Product(Model):
    name = CharField()
    price = DecimalField(max_digits=8, decimal_places=2)
    manufacture_date = DateField()

    class Meta:
        database = db

    def __init__(self, name, price, manufacture_date):
        self.name = name
        self.price = price
        self.manufacture_date = manufacture_date

# Створення моделі для таблиці "Продавець"
class Seller(Model):
    name = CharField()
    address = CharField()

    class Meta:
        database = db

    def __init__(self, name, address):
        self.name = name
        self.address = address

# Створення моделі для таблиці "Чек"
class Purchase(Model):
    customer = ForeignKeyField(Customer)
    product = ForeignKeyField(Product)
    quantity = IntegerField()

    class Meta:
        database = db

    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

# Ініціалізуємо базу даних
db.connect()
db.create_tables([Customer, Product, Seller, Purchase])

# Додавання даних (для прикладу)
customers_data = [
    {'name': 'John Doe', 'email': 'john@example.com'},
    {'name': 'Jane Smith', 'email': 'jane@example.com'},
    {'name': 'Alice Johnson', 'email': 'alice@example.com'},
    {'name': 'Bob Brown', 'email': 'bob@example.com'},
    {'name': 'Emily Davis', 'email': 'emily@example.com'}
]

products_data = [
    {'name': 'Laptop', 'price': 1200.00, 'manufacture_date': '2023-01-15'},
    {'name': 'Smartphone', 'price': 800.00, 'manufacture_date': '2023-03-20'},
    {'name': 'Headphones', 'price': 150.00, 'manufacture_date': '2022-12-10'},
    {'name': 'Tablet', 'price': 500.00, 'manufacture_date': '2023-02-05'},
    {'name': 'Smartwatch', 'price': 300.00, 'manufacture_date': '2023-04-25'}
]

sellers_data = [
    {'name': 'Electronics World', 'address': '123 Main St, City'},
    {'name': 'Gadget Zone', 'address': '456 Elm St, Town'},
    {'name': 'Tech Universe', 'address': '789 Oak St, Village'},
    {'name': 'Digital Haven', 'address': '101 Pine St, Metropolis'},
    {'name': 'Device Emporium', 'address': '202 Cedar St, Township'}
]

purchases_data = [
    {'customer': 1, 'product': 1, 'quantity': 2},
    {'customer': 2, 'product': 2, 'quantity': 1},
    {'customer': 3, 'product': 3, 'quantity': 3},
    {'customer': 4, 'product': 4, 'quantity': 1},
    {'customer': 5, 'product': 5, 'quantity': 2}
]

Customer.insert_many(customers_data).execute()
Product.insert_many(products_data).execute()
Seller.insert_many(sellers_data).execute()
Purchase.insert_many(purchases_data).execute()
