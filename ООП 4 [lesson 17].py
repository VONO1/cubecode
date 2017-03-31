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
    def __init__(self):
        self.products = []


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
cart[0]  = book2
print('Всего товаров в корзине: {}'.format(len(cart)))
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

