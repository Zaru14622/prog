from random import randint

sp = [[[randint(0, 9) for i in range(0, 10)] for j in range(0, 10)] for k in range(0, 10)]
d = dict()
for i in range(0,len(sp)):
    Sum = 0
    for j in range(0,len(sp)):
        for k in range(0,len(sp)):
            Sum += sp[i][j][k]
    d[i+1] = Sum
print(d)



