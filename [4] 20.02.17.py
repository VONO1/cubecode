
def DV(i):
    i2 = ""
    while i > 0:
        ip = i / 2
        #print(ip)
        i = i // 2
        #print(i)
        if i == ip:
            i2 = "0" + i2
        else:
            i2 = "1" + i2
    print(i2)


def DS(g):
    i = list(str(g))
    #print(i)
    h = 0
    ot = 0
    for a in reversed(i):
        #print(a)
        ht = (2 ** h) * int(a)
        #print (ht)
        h+=1
        ot = ot + ht
    else:
        print(ot)


razd = int(input('Что бы перевести десятичное число в двоичное нажмите 0, наоборот нажмите 1: '))
if razd == 0:
    pl = int(input('Введите десятичное число: '))
    DV(pl)
if razd == 1:
    pl = int(input('Введите двоичное число: '))
    DS(pl)
