a = [45, 17, 28, 34, 100]  # исходный массив
b = [] #новый массив



def superfunction():
    i = 0  # индекс, счётчик
    nmin = i  # номер минимального элемента
    min = a[nmin]  # собственно минимальный элемент
    while (i < len(a)):
        if (a[i] < min):
            nmin = i
            min = a[nmin]


            print("11")
            b.append(min)
            a.pop(nmin)
        i += 1

    print(a)
    print(b)

#while len(a) != len(b):
superfunction()
superfunction()
superfunction()
superfunction()
superfunction()
