pl = int(input('Количество тарелок: '))
ms = plates = int(input('Количество моющего средства: '))
while ms > 0:
    pl -= 1
    ms -= 0.5
    print("Осталось %s  моющего средства" % ms)
    if pl == 0 and ms == 0:
        print ("По окончанию мытья не осталось ни тарелок, ни моющего средства")
        break
    if pl == 0:
        print("По окончанию мытья осталось  %s Моющего средства" % ms)
        break
    if ms == 0:
        print("По окончанию мытья осталось  %s  Тарелок" % pl)
        break