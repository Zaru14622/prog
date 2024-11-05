def Mat(a):
    mas = []
    for i in range(0,a):
        mas.append([])
        for j in range(0,a):
            mas[i].append(0)
    return mas

def Main(a):
    mas = Mat(a)
    num = 1
    x1=0
    y1=0
    x2=0
    y2=0
    for i in range(0,20):
        for j in range(0,a):
            if i%4 == 0 and mas[a-1-x1][a-1-j] == 0:
                mas[a-1-x1][a-1-j] = num
                num += 1
            elif i%4 == 1 and mas[a-1-j][y1] ==0:
                mas[a-1-j][y1] = num
                num += 1
            elif i%4 == 2 and mas[x2][j]==0:
                mas[x2][j] = num
                num += 1
            elif i%4 == 3 and  mas[j][a-1-y2]==0:
                mas[j][a-1-y2] = num
                num += 1
        if i % 4 == 0:
            x1 +=1
        if i % 4 == 1:
            y1 +=1
        if i % 4 == 2:
            x2 +=1
        if i % 4 == 3:
            y2 +=1


    for i in mas:
        for j in i:
            if 0 <= j <= 9:
                print(j, end="    ")
            elif j==100:
                print(j, end=" ")
            else:
                print(j, end="  ")
        print("")

Main(10)