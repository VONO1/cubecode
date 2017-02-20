pl = int(input('Введите десятичное число: '))
def DV(i):
    i2 = ""
    while i > 0:
        ip = i / 2
        print(ip)
        i = i // 2
        print(i)
        if i == ip:
            i2 = "0" + i2
        else:
            i2 = "1" + i2
    print(i2)

DV(pl)