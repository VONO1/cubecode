# class Person():
#     firstname  =  'ivan'
#     lastname = 'ivanov'
#     foot_amount = 2
#
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#     def say_name(self):
#         print('Я {} {}, привет!'.format(self.firstname, self.lastname))
#         print('у меня {} ножек!'.format(self.foot_amount))
#
#     @staticmethod
#     def take_lightsabre():
#         return 'lightsabre'
#
#     @classmethod
#     def correct(cls, person):
#         if person.foot_amount > cls.foot_amount:
#             person.foot_amount = 2
#
# class A(object):
#     def say_name():
#         pass
#
#
# class Developer(Person, A):
#     def __init__(self, firstname, lastname, skills):
#         #вызываем родительскую инициализацию
#         super().__init__(firstname, lastname)
#         self.skills = skills
#
#     def say_name(self):
#         super().say_name()
#         print("Я умею: {}".format(self.skills))

# dev1 = Developer('Linus','Torvalds', ['C++','C'])
# dev1.say_name()
#
#
# person1 = Person('ivan','ivanov')
# person2 = Person('anton', 'antonov')
# person3 = person1

# person3.firstname = 'Petrov'
#
# person2.foot_amount = 4
# person2.age = 1
#
# person2.take_lightsabre()
#
#
# person1.say_name()
# person2.say_name()
#
# #print(Person.foot_amount)
#
# Person.correct(person2)
# print(person2.foot_amount)

class Person(object):
    def __init__(self, firstname, lastname, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone


class Product(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ProductException(BaseException):
    pass


class Order(object):
    def __init__(self, person):
        self.person = person
        self.products = []

    def add(self, product):
        if not isinstance(product, Product):
            raise ProductException('Это не товар!')
        self.products.append(product)
    def get_cost(self):
        return sum([p.price for p in self.products])


person1 = Person('Ivan', 'Ivanov', '+6 666 66 66')
order1 = Order(person1)

product1 = Product('Говорящий хомяк', 700)
order1.add(product1)

product2 = Product('Нео куб', 2500)
order1.add(product2)

print ('стоимость', order1.get_cost())