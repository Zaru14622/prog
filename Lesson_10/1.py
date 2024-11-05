#1)Дан рандомный одномерный список, сформировать словарь, в качестве ключей использовать числа с еденицы, а в качестве значений элементы списка
from random import randint

mas = []
for i in range(30):
    mas.append(randint(0,9))
print(mas)
print("-"*100)

d = dict()
for i in range(1,31):
    d[i] = int(mas[i-1])
print(d)

