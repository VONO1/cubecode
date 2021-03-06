# coding: utf-8
# нужен что бы русские символы работали во втором питоне
'''
__new__(cls) - настоящий конструктор
__init__(self) - конструктор инициализирующийся в момент создания
__del__() -деструктор, в момент когда удаляется объект
__int__, __float__, __str__, (__unicode__ - python 2)  - позволяет представлять класс в виде определённого типа данных



'''

from pprint import pprint

class Product(object):
    # метод описывающий документацию:
    """
    Здесь документация к классу
    """
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        #вызывается при конвертации объекта в строку (при принте)
        return self.title

    def __repr__(self):
        #полный контроль вывода на экран, вызывется функцией repr()  для получения строки формального представления объекта
        return   'Продукт "{}" стоимостью"{}" '.format(self.title, self.price)

    def __float__(self):
        #для конвертации объекта в float
        return self.price

class Cart(object):
    #обязательные атрибуты
    __slots__ = ['__current','products']
    def __init__(self):
        self.products = []
        self.__current = None
    def __iter__(self):
        return self

    def __next__(self):
        if self.__current is None:
            self.__current = 0
        if self.__current < len(self.products):
            self.__current = None
            raise StopIteration
        self.__current += 1
        return self.products[self.__current]

    def __len__(self):
        return len(self.products)

    def __getitem__(self, key):
        if key < len(self):
            return self.products[key]
        raise KeyError()

    def __setitem__(self, key, product):
        self.products[key] = product

    def __delitem__(self, key):
        if key < len(self):
            self.products[key].pop(key)


    def add(self, product):
        self.products.append(product)

book = Product('Объектно-ориетированное мышление', 999.13)
book2 = Product('Совершенный код', 750.13)
book3 = Product('Шаблоны проектирования', 999.13)

cart = Cart()
cart.add(book)
cart.add(book2)
cart.add(book3)

for p in cart:
    print('в корзине: {}'.format(p))

#print('Всего товаров в корзине: {}'.format(len(cart)))
#
# class A(object):
#     pass
# class B(object):
#     pass

#
#
# print('Имя класса: {}'.format(Product.__name__))
# print('Имя модуля: {}'.format(Product.__module__))
# print('базовый классов: {}'.format(Product.__base__))
# print('Кортеж базовых классов: {}'.format(Product.__bases__))

# print('словарь атрибутов класса')
# pprint(Product.__dict__)
#
#
#

#
# print('Класс на основе которого создан объект: {} '.format(book.__class__))

# print('атрибуты экземпляра:')
# pprint(book.__dict__)

#документация
# print(Product.__doc__)


print(float(book))





# a = 666
# b = 777
# del a, b

# перегрузка оператора

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Перегрузка операторов + """
        return Vector(self.x + other.x, self.y + other.y)


    def lenght(self):
        return (self.x ** 2 +self.y **2) ** 0.5


    def __sub__(self, other):
        """Перегрузка операторов - """
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """Перегрузка операторов * """
        return Vector(self.x * other.x, self.y * other.y)

    def __lt__(self, other):
        """Перегрузка операторов <"""
        return self.lenght() < other.lenght()

    def __eq__(self, other):
        """Перегрузка операторов = """
        return self.lenght() == other.lenght()

    def __repr__(self):
        return 'V({},{})'.format(self.x, self.y)



v1 = Vector(1,5)
v2 = Vector(1,8)

print('сумма векторов v2 и v2 равна: {}'.format(v1 + v2))
print('разность векторов v2 и v2 равна: {}'.format(v1 - v2))
print('произведение векторов v2 и v2 равна: {}'.format(v1 * v2))

print('{} < {} : {}'.format(v1,v2, v1 > v2))


