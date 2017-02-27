pl = input('Введите значение: ')
a = list(pl)
aa = a


bb = []
for a in reversed(a):
    bb.append(a)


print(aa, bb)
if aa == bb:
    print("По всей видимости это Палиндром")
else: print("По всей видимости это НЕ Палиндром")
