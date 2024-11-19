#2 списк 10на10(генератор) вывесте все элементы которые есть в 1-ом списке и нет во 2-ом
from random import randint
a =[[randint(0, 100) for i in range(0, 10)] for j in range(0, 10)]
b =[[randint(0, 100) for i in range(0, 10)] for j in range(0, 10)]
m1 = []
m2 = []
for i in a:
    for j in i:
        m1.append(j)
for i in b:
    for j in i:
        m2.append(j)
m1 = set(m1)
m2 = set(m2)
print(m1)
print(m2)
print("*"*40)
print(m1 - m2)


