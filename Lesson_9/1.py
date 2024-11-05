def Mat(a):
    mas = []
    for i in range(0,a):
        mas.append([])
        for j in range(0,a):
            mas[i].append(0)
    return mas

def Main(a):
    mas = Mat(a)
    num = 0
    for i in range(0,10):
        for j in range(0, 10):
            if i%2 == 0:
                mas[a - 1 - i][a - 1 - j] = num
            else:
                mas[a - 1 - i][j] = num
            num += 1

    for i in mas:
        for j in i:
            if 0 <= j <= 9:
                print(j, end="  ")
            else:
                print(j, end=" ")
        print("")


Main(10)
