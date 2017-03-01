#glav = int(input('\n 1. Вывести список задач \n 2. Добавить задачу \n 3. Отредактировать задачу \n 4. Завершить задачу \n 5. Начать задачу сначала \n 6. Выход'))
def list_sp():
    print("1")

def list_sp2():
    print("2")

menu_= {"start" : [
    {"Nu":1,"Name":"Вывести список задач","fun":list_sp},
    {"Nu":2,"Name":"Добавить задачу","fun":list_sp2}
    ]
}

a = 100

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
MENUS("start")