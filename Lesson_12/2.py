#2 списк 10на10(генератор) вывесте все элементы которые есть в 1-ом списке и нет во 2-ом
from random import randint
a =[randint(0, 100) for j in range(0, 10)]
b =[randint(0, 100) for i in range(0, 10)]
a = set(a)
b = set(b)
print(a)
print(b)
print("*"*40)
print(a-b)


