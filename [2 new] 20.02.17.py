
sp = [1, 2, 3, 8, 14, 89, 45]
np = []
x = len(sp)
while x > 0:
    print(x)
    print(len(sp))
    z = sp[x - 1]
    np.append(z)
    x -= 1
#else:
print(np)
#print(len(sp))