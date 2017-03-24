from pony.orm import Database, Required, Optional ,Set, db_session, show

db = Database()

#категория
class Category(db.Entity):
    title = Required(str)
    products = Set('Product')

class Photo(db.Entity): #базовый класс для сущностей
    url = Required(str)
    alt = Optional(str) #альтернативное описание
    products = Set('Product')


#продукты
class  Product(db.Entity):
    title = Required(str)
    categories = Set('Category')
    price = Required(float)
    description = Optional(str)
    photos = Set(Photo)
    Order_items = Set('OrderItem')


# class StorageItem(db.Entity):
#     product = Product
#     ammouth = int
#
# class Storage():
#     storage_items = StorageItem[]

class Customer(db.Entity):
    username = Required(str) #почта / телефон
    password = Required(str)
    activated = Required(bool)
    orders = Set('Order')

class OrderItem(db.Entity):
    #продукт
    product = Required('Product')
    #количество
    amount = Optional(int)
    order = Optional('Order')

class Order(db.Entity):
    customer = Required(Customer)
    basket = Set(OrderItem)

db.bind('sqlite',':memory:')
db.generate_mapping(create_tables=True)


with db_session:
    customer = Customer(username = 'aa@rr,ru',
                        password = 'sdsad111',
                        activated = True,
                        orders = Set('Order')
                        )

    order = Order(customer=customer)