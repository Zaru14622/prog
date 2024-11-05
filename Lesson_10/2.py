#2) тоже дан рандомный одномерный список, сформировать словарь, ключ которого будут все различные элементы исходного списка, а значение их количество
from random import randint

mas = []
for i in range(30):
    mas.append(randint(0,9))
print(mas)
print("-"*100)

d = dict()
for i in mas:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)