def COR(x,y):
    if y == 0:
        if x == 0:
            print("Точка находится в центре")
        else:
            print("Точка лежит на оси координат Y")
    else:
        if x == 0:
            print("Точка лежит на оси координат X")

        else:
            if y > 0:
                if x > 0:
                    print("Точка находится в квадрате 1")
                else:
                    print("Точка находится в квадрате 2")
            else:
                if x > 0:
                    print("Точка находится в квадрате 4")
                else:
                    print("Точка находится в квадрате 3")

xx = int(input('Введите Х: '))
yy = int(input('Введите Y: '))
COR(xx,yy)