



#массив содержащий события
tasks = []

#какие свойства должны быть у события (что бы можно было их добавить/ изменить / удалить без правки остального кода)
info = ["id", "name", "txt", "time", "status"]

#===============================================================================================================
# ФУНКЦИИ
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

            else: task["status"] = "good"
    else:
        print(task)
        tasks.append(task)
        print(tasks)
        MENUS("start")

#функция вывода задач на экран
def OTOBR():
    for o in tasks:
        print(o)
    else:
        MENUS("start")


#функция отображающая меню на экране
def MENUS(levels):
    #Переменная содержащая текст на экране
    txt = str
    #Цикл формирования меню
    for p in menu_ [levels]:
        txt = "{} \n {} . {}".format(txt, p["Nu"], p["Name"])
    else:
        #Запрашиваем ответ
        glav = int(input("Ежедневник \n {} \n Сделайте Ваш выбор:".format(txt)))
        #Проверяем выбор пользователя
        for z in menu_[levels]:
            if glav == z["Nu"]:
                z["fun"]()


# Функция удаления задания
def DEL_F():
    vib = int(input("введите id события для удаления"))
    for v in tasks:
        if vib == v["id"]:
            tasks.pop(v["id"] - 1)
            print("Задание удалено")
            MENUS("start")
            break
    else:
        print("нет такого задания, пожалуйста повторите")
        MENUS("start")

# Функция отмены задания
def OTM_F():
    vib = int(input("введите id события для отмены"))
    for v in tasks:
        if vib == v["id"]:
            v["status"] = "bad"
            print("Задание отменено")
            MENUS("start")
            break
    else:
        print("нет такого задания, пожалуйста повторите")
        MENUS("start")
# функция возобновления задания
def NEW_F():
    vib = int(input("введите id события для возобновления"))
    for v in tasks:
        if vib == v["id"]:
            v["status"] = "good"
            print("Задание возобновлено")
            MENUS("start")
            break
    else:
        print("нет такого задания, пожалуйста повторите")
        MENUS("start")

# Меню программы. Сделано что бы можно было добавлять дополнительные меню без дополнительного кода
menu_ = {"start": [
    {"Nu": 1, "Name": "Вывести список задач", "fun":OTOBR},
    {"Nu": 2, "Name": "Добавить задачу", "fun": ADD_F},
    {"Nu": 3, "Name": "Отредактировать задачу", "fun":ADD_F},
    {"Nu": 4, "Name": "Удалить задачу", "fun":DEL_F},
    {"Nu": 5, "Name": "Отменить задание", "fun":OTM_F},
    {"Nu": 6, "Name": "Возобновить задание", "fun":NEW_F}

]
}
#Вызываем стартовое меню
MENUS("start")