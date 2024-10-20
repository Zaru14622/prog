from random import randint
def RandomMas(a,b):
    mas = []
    for i in range(0,a):
        mas.append([])
        for j in range(0,b):
            mas[i].append(randint(0,9))


    return mas

def main():
    mas = RandomMas(9,9)

    max = mas[0][0]
    for i in range(0,9):
        for j in range(0,9):
            if i<=j and i < 5 and j<(9-i):
                if max < mas[i][j]:
                    max = mas[i][j]
            elif i>=j and i >= 5 and (i+j)>=8:
                if max < mas[i][j]:
                    max = mas[i][j]

    print(max)

main()