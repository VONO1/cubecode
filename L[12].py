# # Шаблоны проектирования
# # Singleton - одиночка
# import sqlite3
# class DB(object):
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls._instance = super().__new__(cls)
#
#         return cls._instance
#
#     def __init_(self, dbname):
#
#             self.conn = sqlite3.connect(dbname)
#
# class Singleton(type):
#     __instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls.__instances:
#             cls.__instances[cls] = super().__call__(*args, **kwargs)
#         return cls.__instances[cls]
#
# class DB2(metaclass = SingletonMeta):
#     def __init__(self, dbname):
#         self.conn = sqlite3.connect(dbname)
#
#
# def singleton(cls):
#     instances = {}
#     def get_instance(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args,**kwargs)
#         return get_instances[cls]
#     return get_instance
#
# @singleton
# class Config(object):
#     pass



#
# db1 = DB(":memory:")
# db2 = DB(':memory:')
#
# # print(db1 ==  db2)
# config1 = config()
# config2 = config()


# command - команда

from abc import ABCMeta, abstractmethod
class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

class GetVersionCommand(Command):
    def execute(self, *args, **kwargs):
        print('1.0')

class HelpCommand(Command):
    def execute(self):
        print('i need help')

commands = {
    'version':GetVersionCommand,
    'help' :HelpCommand
}

from random import  randrange




class Subject(object):
    def __init__(self):
        self._observers = []

    def add_observer(self,observer):
        if isinstance(observer,Observer):
            self._observers.append(observer)


    def remove_observer(self,observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.handle_event()

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def handle_event(self):
        pass


# Observer - наблюдатель
class LoginHandler(Subject):
    def authorize(self):
        #Результаты работы: 1- успешный вход 2- ошибка при входе
        #Требования - логировать все успешные входы и попытки Ошибка провайдера отсылаем куки
        result = randrange(2)
        if result == 0:
            print('успешный вход')
        elif result == 1:
            print('невыерный логин/пароль')

        self.notify()

class LoggerObserver(Observer):
    pass

class ErrorObserver(Observer):
    pass

class CookieObserver(Observer):
    pass


loggin_handler = LoginHandler()
loggin_handler.add_observer(LoggerObserver())
loggin_handler.add_observer(ErrorObserver())
loggin_handler.add_observer(CookieObserver())

loggin_handler.authorize()