
import sys
from SQLL import storage

# Подключение к базе
conn = storage.connect('tasks.db')
storage.initialize(conn)

#массив содержащий события
tasks = []

#какие свойства должны быть у события
info = ["id", "name", "txt", "time", "status"]

#===============================================================================================================
# ФУНКЦИИ
# Функция поиска
def S_F():
    vib = int(input("введите id события"))
    for v in tasks:
        if vib == v["id"]:
            return (v)
            MENUS("start")
            break
    else:
        print("нет такого задания, пожалуйста повторите")
        MENUS("start")
#Функция проверки информации
# def PROV_F(ob,tip):
#     if tip != dt:
#         if ob = tip:
#             return(True)
#         else:
#             return(False)
#     else:
#         ob.split(".")

#функция добавления информации
def ADD_F():
    #превращаем имя свойства в переменную
    import __main__
    #список для добавления
    task = {}
    for n in info:
        #если значение не формируется автоматически, то запрашиваем его у пользователя:
        if n != "id" and n != "status":
            glav = input("введите {}".format(n))
            #превращаем имя свойства в переменную
            setattr(__main__, n, glav)
            #добавляем пременную в массив
            task[n] = glav
        else:
            #если значение id или status то формируем его автоматически
            if n == "id":
                task["id"] =  len(tasks)+1

            else: task["status"] = "Не выполнено"
    else:
        tasks.append(task)
        #записываем в БД
        print(task)
        storage.add_task(conn,task['name'],task['time'],task['txt'])
        MENUS("start")

#функция вывода задач на экран
def OTOBR():
    #Старая не SQL версия
    # for o in tasks:
    #     s = ""
    #     if o["status"] == "bad":
    #         s = "Активно"
    #     else: s = "Не активно"
    #     print("id задания: {} \n Имя задания: {} \n Дата задания {} \n Статус задания {} \n Что нужно сделать {}".format(o["id"], o["name"], o["time"], s, o['txt']))
    #
    # else:
    #     MENUS("start")
    all_tasks = storage.all_tasks(conn)
    for task in all_tasks:
        print('{:*^101}'.format(' id: {task[id]} '.format(task=task)),\
              '\nНазвание задачи: {task[task_name]} Дата: {task[task_date]} Статус: {task[status]}'.format(task=task),\
              '\n{:=^101}'.format(' Текст задачи '), '\n{task[text]}'.format(task=task), \
              '\n{:=^101}\n'.format(' Текст задачи '))
    else:
        MENUS("start")

#функция отображающая меню на экране
def MENUS(levels):
    #Переменная содержащая текст на экране
    txt = ""
    #Цикл формирования меню
    for p in menu_ [levels]:
        txt = "{} \n {} . {}".format(txt, p["Nu"], p["Name"])
    else:
        #Запрашиваем ответ
        glav = int(input("Ежедневник \n {} \n \n Сделайте Ваш выбор: " .format(txt)))
        #Проверяем выбор пользователя
        for z in menu_[levels]:
            if glav == z["Nu"]:
                if z["Arg"] != None:
                    z["fun"](z["Arg"])
                else:
                    z["fun"]()


# Функция удаления задания
def DEL_F():
    i = S_F()
    tasks.pop(i["id"] - 1)
    print("Задание удалено")
    MENUS("start")


# Функция отмены задания
def OTM_F():
    # i = S_F()
    # i["status"] = "Выполнено"
    # print("Задание отменено")
    nom = input('id: ')
    storage.close_task(conn, nom)
    MENUS("start")

# функция возобновления задания
def NEW_F():
    nom = input('id: ')
    storage.re_task(conn, nom)
    MENUS("start")
# Функция выхода
def EX_F():
    sys.exit()

# Функция редактирования
def ED_F(property):
    idx = input('\nid задачи: ')
    task = storage.find_by_id(conn, idx)
    print('Название: {task[task_name]}; Дата: {task[task_date]}; Текст: {task[text]}'.format(task=task))
    task_name = input('\nНовое название задачи:')
    task_date = input('\nНовая дата выполнения:')
    text = input('Новый текст задачи:\n')
    #storage.update_task(conn, task['name'], task['time'], task['txt'], task['id'])

    storage.update_task(conn, task_name, task_date, text, idx)

    # i = S_F()
    # n = input("введите новое значение")
    # i[property] = n
    # storage.update_task(conn, i['name'], i['time'], i['txt'], i[id])
    print("Значение изменено")
    MENUS("start")
# Меню программы. Сделано что бы можно было добавлять дополнительные меню без дополнительного кода
menu_ = {"start": [
    {"Nu": 1, "Name": "Вывести список задач", "fun":OTOBR ,"Arg":None},
    {"Nu": 2, "Name": "Добавить задачу", "fun": ADD_F ,"Arg":None},
    {"Nu": 3, "Name": "Отредактировать задачу", "fun":MENUS, "Arg":"edit" },
    {"Nu": 4, "Name": "Удалить задачу", "fun":DEL_F ,"Arg":None},
    {"Nu": 5, "Name": "Отменить задание", "fun":OTM_F ,"Arg":None} ,
    {"Nu": 6, "Name": "Возобновить задание", "fun":NEW_F ,"Arg":None},
    {"Nu": 7, "Name": "Выход из программы", "fun":MENUS, "Arg":"exit" }
    ],
        "exit": [
    {"Nu": 1, "Name": "да. мусор а не программа", "fun": EX_F,"Arg":None},
    {"Nu": 2, "Name": "нет. создам ещё пару задач", "fun":MENUS, "Arg":"start"}
    ],
        "edit": [
    {"Nu": 1, "Name": "Редактировать имя", "fun":ED_F, "Arg":"name"},
    {"Nu": 2, "Name": "Редактировать текст задачи", "fun":ED_F, "Arg":"txt"},
    {"Nu": 3, "Name": "Редактировать дату", "fun":ED_F, "Arg":"time"},
    ]

}
#Вызываем стартовое меню
MENUS("start")