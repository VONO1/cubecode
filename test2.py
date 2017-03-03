#массив содержащий события
tasks = []

#какие свойства должны быть у события (что бы можно было их добавить)
info = ["id", "name", "txt", "time", "status"]
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



ADD_F()
ADD_F()

