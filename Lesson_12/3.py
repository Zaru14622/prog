#матрица 10на10 создать множество с рандомом того же диапозона получить словарь ключами которых будет их значение в множнстве, а значение словаря частота вхождения этих чисел
from random import randint
a =[[randint(0, 30) for i in range(0, 10)] for j in range(0, 10)]
d = dict()
for i in a:
    print(i)
    b = set(i)
    for j in b:
        if j in d:
            d[j] = d[j] + 1
        else:
            d[j] = 1
print("*"*200)
print(d)
