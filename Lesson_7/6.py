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

    for i in mas:
        print(i)

    print("-------------------------------------------")

    for i in range(0, a):
        dop.append([])
        for j in range(0, b):
            dop[i].append(mas[a - j-1][i])


    for i in dop:
        print(i)

Main(10,10)