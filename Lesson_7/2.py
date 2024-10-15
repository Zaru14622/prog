from random import randint
def RandomMas(a,b):
    mas = []
    for i in range(0,a):
        mas.append([])
        for j in range(0,b):
            mas[i].append(randint(0,9))

    return mas


def Main(a,b):
    mas = RandomMas(a,b)
    dop = []
    for i in range(0,a):
        dop.append([])
        for j in range(0,b):
            dop[i].append(mas[j][i])

    sum = 0
    for i in dop:
        sum += min(i)
    print(sum)


Main(10,10)