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


    for i in range(0, a):
        for j in range(0, b):
            for k in range(0, a):
                if mas[j][i] > mas[k][i]:
                    c = mas[j][i]
                    mas[j][i] = mas[k][i]
                    mas[k][i] = c


    for i in mas:
        print(i)


Main(10,10)