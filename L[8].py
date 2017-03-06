# # Исключения
# raise RuntimeError('')
# while True:
#     try:
#         i = int(input())
#         break
#         #rw()
#     except ValueError as e:
#         print(e)
#     except NameError:
#         print("функция")
#     except:
#         print("Всё плохо")
#     finally:
#         print("этот блок выполняется всегда")
#
#

## Итераторы и Генераторы
# s = 'Linus'
# lst = [1,2,3,4,5]
# person = {
#     'name' :'linus',
#     'age':48,
#     'is_dev': True
# }
#
# it = iter(s)
# while True:
#     try:
#         i = next(it)
#         print(i)
#     except StopIteration:
#         break
#
# def generator():
#     print('Шаг 1')
#     yield 1
#     print('Шаг 2')
#     yield 2
#     print('Шаг 3')
#
# gen = generator()
# #print(next(gen))
#
# for i in gen:
#     print(i)


# def countdown(n):
#     print('генератор стартовал')
#     while n:
#         yield n
#         n -= 1
#
# for i in countdown(5):
#     print('Генератор вернул{}'.format (i))
#
#
# def generator_range(first, last):
#     for i in range(first,last):
#         yield i
#
# #python >=3
# def generator_range(first, last):
#     yield from range(first, last)


# Генераторы списка / множеств /  словарей
numbers = [1,1,2,2,3,3]
squares = [i * i for i in numbers]
ood = [i for i in numbers if  i % 2]
points = [(x,y) for x in range(3) for y in range(2)]


# s = {i for i in numbers}
# keys = ['id', 'name', 'age']
# values = [1,'Linus', 47]
# #короткий способ
# #data = dict(zip(keys, values))
#
# #data = {k.upper(): v for i, k in enumerate(keys) for j, v in enumerate(values) if i ==j}
#
#
# data = {k.upper(): v for k, v in zip (keys, values)}
# print (data)

#убираем дубликаты из словаря
data = [
    {
        'id':1,
        'name':'linus',
        'age': 47
    },
    {
        'id':2,
        'name':'Richard Stallman',
        'age': 47
    },
    {
        'id':1,
        'name':'linus',
        'age': 47
    }
]

# persons = {d['id']: d for d in data}
# print(persons)
#
# #выражения генераторы
# gen_squares = (i * i for i in numbers)
# print(gen_squares)

#
# with open('L[8].py') as f:
#     lines = (line.strip() for line in f)
#     linuses = (l for l in lines if "linus" in l)
#     print(list(linuses))
#    linuses.throw(RuntimeError, 'моя ошибка')
#     linuses.close() # Выход из генератора

# Сопрограммы
def coroutine(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return wrapper

@coroutine
def echo():
print('генератор стартовал!')
while True:
    msg = (yield)
    print(msg)

e = echo()
next(e)
e.send('Hi!')

e.send('I like it')

