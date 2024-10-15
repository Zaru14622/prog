from random import randint
def RandomMas(a,b):
    mas = []
    for i in range(0,a):
        mas.append([])
        for j in range(0,b):
            mas[i].append(randint(0,9))

    return mas

def Main(a,b):
    mas = RandomMas(10,10)

    print("Изначальная матрица")
    for i in mas:
        print(i)

    print("-----------------------------------------")
    print("Отзеркаленая")

    for i in range(0,5):
        c = mas[i]
        mas[i] = mas[9-i]
        mas[9-i] = c


    for i in mas:
        print(i)

Main(10,10)