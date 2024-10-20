from random import randint
def RandomMas(a,b):
    mas = []
    for i in range(0,a):
        mas.append([])
        for j in range(0,b):
            mas[i].append(randint(0,9))

    return mas

mas = RandomMas(10,10)
# for i in mas:
#     print(i)
# print("---------------------------")

def Main(a,b):
    for i in range(0,a):
        for j in range(0,b):
            for k in range(0,a):
                if mas[i][j] > mas[i][k]:
                    c = mas[i][j]
                    mas[i][j] = mas[i][k]
                    mas[i][k] = c
    # print(i)

    for i in mas:
        print(i)




Main(10,10)

