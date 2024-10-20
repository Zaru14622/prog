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
    max = 0

    for i in range(0,9):
        for j in range(0,9):
            if j>3 and i < 5:
                if max < mas[i][j]:
                    max = mas[i][j]
                print(mas[i][j], end=" ")
            elif i>=j and i >= 5 and (i+j)>=8 and j < 5:
                if max < mas[i][j]:
                    max = mas[i][j]
                print(mas[i][j], end=" ")
            else:
                print("",end="  ")
        print("")
    print(max)

main()