from random import randint
def RandomMas(a,b):
    mas = []
    for i in range(0,a):
        mas.append([])
        for j in range(0,b):
            mas[i].append(randint(0,9))
    return mas

def RotateR(a,b,mas):
    dop = []
    for i in range(0, a):
        dop.append([])
        for j in range(0, b):
            dop[i].append(mas[a - j-1][i])
    return dop

def RotateL(a,b,mas):
    dop = []
    for i in range(0, a):
        dop.append([])
        for j in range(0, b):
            dop[i].append(mas[j][b - i-1])
    return dop

def Main(a,b):
    mas = RandomMas(a,b)
    num = int(input("Введите число от -3 до 3 ::: "))
    print("Изначальная матрица")
    for i in mas:
        print(i)
    print("_"*30)
    if -4 < num < 0:
        for i in range(num,0):
            mas = RotateL(a,b,mas)
        for i in mas:
            print(i)
    elif 4 > num > 0:
        for i in range(0, num):
            mas = RotateR(a, b, mas)
        for i in mas:
            print(i)
    else:
        print("матрица не изменилась")


Main(10,10)
