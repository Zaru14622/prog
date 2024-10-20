from random import randint
def RandomMas(a,b):
    mas = []
    for i in range(0,a):
        mas.append([])
        for j in range(0,b):
            mas[i].append(randint(0,9))


    return mas

def PrintMatrix(a):
    for i in a:
        for j in i:
            print(j,end=" ")
        print("")
    print("-" * 18)

def main():
    mas = RandomMas(9,9)

    PrintMatrix(mas)

    max = mas[0][0]
    for i in range(0,9):
        for j in range(0,9):
            if (3-i) < j and (5+i) > j and i < 5:
                print(mas[i][j], end=" ")
            elif i >= 5 and (i - 4) <=j and (i- 4 +j)<=8:
                print(mas[i][j], end=" ")
            else:
                print(" ", end=" ")
        print("")


main()